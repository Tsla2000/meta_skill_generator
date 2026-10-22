#!/usr/bin/env python3
"""Validate the meta-skill-generator project structure.

Checks:
  1. Required files exist.
  2. SKILL.md frontmatter has name == folder name and a description of sane length.
  3. Every references/*.md linked from SKILL.md / README.md exists.
  4. skill.yaml name matches the snake_case form of the folder name.
  5. Both validation examples exist and are non-trivial.
Exit code 0 = pass, 1 = fail (each failure printed).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)


required = [
    "SKILL.md",
    "skill.yaml",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "references/dissection-worksheet.md",
    "references/skill-anatomy.md",
    "references/output-templates.md",
    "references/quality-gate.md",
    "references/portability.md",
    "examples/example-1-chrome-extension-reverse.md",
    "examples/example-2-quarterly-portfolio-review.md",
]
for rel in required:
    check(os.path.isfile(os.path.join(ROOT, rel)), f"missing file: {rel}")

skill_md = ""
p = os.path.join(ROOT, "SKILL.md")
if os.path.isfile(p):
    skill_md = open(p, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", skill_md, re.S)
    check(m is not None, "SKILL.md: missing YAML frontmatter")
    if m:
        fm = m.group(1)
        name = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
        check(name is not None and name.group(1) == os.path.basename(ROOT),
              "SKILL.md: frontmatter name must equal folder name")
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        check(desc is not None and 40 <= len(desc.group(1)) <= 1024,
              "SKILL.md: description missing or length outside 40..1024")

readme = ""
rp = os.path.join(ROOT, "README.md")
if os.path.isfile(rp):
    readme = open(rp, encoding="utf-8").read()

for text, origin in ((skill_md, "SKILL.md"), (readme, "README.md")):
    for link in re.findall(r"(references/[\w.-]+\.md)", text):
        check(os.path.isfile(os.path.join(ROOT, link)),
              f"{origin}: linked reference missing: {link}")
    for link in re.findall(r"(examples/[\w.-]+\.md)", text):
        check(os.path.isfile(os.path.join(ROOT, link)),
              f"{origin}: linked example missing: {link}")

yp = os.path.join(ROOT, "skill.yaml")
if os.path.isfile(yp):
    y = open(yp, encoding="utf-8").read()
    expected = os.path.basename(ROOT).replace("-", "_")
    check(re.search(rf'^name:\s*"{expected}"', y, re.M) is not None,
          f"skill.yaml: name must be {expected}")

for rel in required:
    if rel.startswith("examples/"):
        fp = os.path.join(ROOT, rel)
        if os.path.isfile(fp):
            check(len(open(fp, encoding="utf-8").read()) > 1000,
                  f"{rel}: example too short to be a real validation sample")

if failures:
    print("FAIL")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("PASS: structure, frontmatter, links, yaml, examples all OK")
