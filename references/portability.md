# 安装与移植说明

本生成器（meta_skill_generator）与它生成的 Skill，都按「一份正文，多处可用」设计。

## Muse（本机）

- 位置：`~/workspace/custom-skills/<skill_name>/`，含 `SKILL.md` 与 `skill.yaml`。
- `SKILL.md` 不写 frontmatter，元数据只放 `skill.yaml`：name 用 snake_case 且与文件夹同名，description 一句话写清产出与触发时机，category 用现有分类如 `Work and knowledge`，include_in_prompt 按是否需要常驻决定，生成器类与高频类设 true，长尾专用 Skill 设 false 靠 skill_search 命中即可。
- 装好后用 `muse.skill_search` 以目标关键词检索一次，命中才算安装成功。

## Claude Code / Codex / 其他遵循 Agent Skills 开放规范的宿主

- 文件夹改名为 kebab-case 并与技能名一致，如 `meta-skill-generator/`。
- 在 `SKILL.md` 顶部加 YAML frontmatter，只需两个字段：

```yaml
---
name: meta-skill-generator
description: 把关键词或模糊目标解剖成真实任务，再反向设计出可直接执行的专用 Skill。用户丢关键词要生成 Skill 时使用。
---
```

- 正文与 references 原样保留。skill.yaml 可留作 Muse 侧元数据，不影响其他宿主。

## REA 与 Grok Bot 等以文案投喂的 Agent

- 用模式 A 输出整份文案直接粘贴投喂，不需要文件结构。
- 投喂前删掉文案中指向 Muse 本地路径与工具名的句子，或改写为宿主的等价工具。文案的阶段、判断、产出、验收部分跨宿主不改。
- 打包成 zip 喂 GrokBot 的先例：SKILL.md、skill.yaml、references 一并打包，README 里注明哪些是 Muse 专有实现、宿主需自建等价物。

## 已知限制

- 各宿主对 Skill 的发现方式不同：Muse 靠 skill.yaml 与 skill_search，开放规范宿主靠 frontmatter 与目录扫描。双投时两套元数据要同步改，改一处漏一处会导致某个宿主搜不到。
- 本生成器只保证文案质量，不保证宿主的工具与权限。生成的 Skill 在新宿主首次使用时，应先跑它的「开工前检查」一节再正式执行。
