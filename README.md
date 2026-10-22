# Meta-Skill Generator（专用 Skill 生成器）

> 丢一个关键词进来，出去一份能直接交给执行型 Agent 干活的专用 Skill。

一个生成其他 Skill 的元技能（Meta-Skill）。它不执行目标任务本身，而是先把输入解剖成真实任务，再反向设计出针对该目标定制的执行文案。

## 它解决什么问题

给 Agent 丢一个模糊词（一个产品名、一个技术名词、一句目标），通常有两种坏结果：要么它只做字面扩写，要么它套一个万能模板。这个生成器强制走完一条不同的路：

1. **语义解剖**：七问拆解关键词指向的对象、真实任务、核心机制、子问题、前置条件、易错点与完成特征。
2. **任务建模**：识别真实任务类型（研究、分析、实现、自动化、数据、内容、评估、诊断，可多选），按类型选方法，不强迫所有输入走同一条流水线。
3. **领域建模**：写出该领域真正有效的工作机制与专有失败模式，这是定制感的来源。
4. **反向设计**：从验收实物倒推执行阶段。每阶段必须有动作、判断条件、产出、失败处理四件。
5. **质量门**：输出前过九项检查，包括「换名自检」：把目标名换掉后全文还成立过半，说明是套模板，重做。

## 快速开始

把 `SKILL.md` 交给任何支持 Agent Skills 的宿主（Claude Code、Codex、Muse 等），然后给它一个关键词：

```text
给「LaunchMotion」生成一份专用 Skill
```

默认输出一份可直接复制给 REA 等执行型 Agent 的文案（模式 A）。明确要求文件版时，输出完整 Skill 目录（模式 B）。

## 目录

| 路径 | 内容 |
|---|---|
| `SKILL.md` | 主指令（开放规范版，带 YAML frontmatter） |
| `skill.yaml` | Muse 侧元数据，与 frontmatter 双投时保持同步 |
| `references/dissection-worksheet.md` | 语义解剖七问工作表与深度档位 |
| `references/skill-anatomy.md` | 专用 Skill 的十个设计维度与取舍规则 |
| `references/output-templates.md` | 模式 A 文案模板与模式 B 目录结构 |
| `references/quality-gate.md` | 输出前九项质量检查 |
| `references/portability.md` | 各宿主的安装与移植方法 |
| `examples/` | 两份验证样例：浏览器扩展逆向（技术类）、季度持仓复盘（研究类），结构故意不同构 |

## 安装

- **Muse**：把本目录复制到 `~/workspace/custom-skills/meta_skill_generator/`（文件夹名用下划线版），保留 `skill.yaml`，`SKILL.md` 去掉 frontmatter。用 skill_search 搜到即装好。
- **Claude Code / Codex**：保持本目录原样（kebab-case 文件夹名与 SKILL.md 的 frontmatter name 一致），放入宿主的 skills 目录。
- **REA / Grok Bot 等文案投喂型 Agent**：不需要装文件，让宿主按 SKILL.md 生成模式 A 文案后整份粘贴投喂。

自检：`python3 tools/validate.py` 检查目录结构、frontmatter、引用完整性与样例存在性。

## 设计原则

- 生成的 Skill 必须自包含，执行 Agent 不看生成现场的对话也能开工。
- 模糊动词一律翻译成「动作 + 可检查结果」，「深入研究」这类话不许进成品。
- 证据分级：已验证、推断、未知分开写。常见做法不等于目标的实际做法。
- 安全边界写进每份生成的 Skill：不绕过登录、付费与访问控制，不复制受保护代码与素材，花钱与对外动作先经用户批准。

## License

MIT，见 `LICENSE`。
