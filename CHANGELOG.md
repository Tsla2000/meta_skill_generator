# Changelog

## v1.1.0 - 2026-10-22

- SKILL.md 替换为用户定稿版（档位分型、安全与授权、独立性测试自检），并同步 Muse 安装版与 skill.yaml 描述。
- 宿主支持补全：portability.md 重写为宿主支持矩阵，覆盖 Claude Code、OpenAI Codex、Gemini CLI、Cursor、GitHub Copilot / VS Code、Muse 等原生宿主（附各自 skills 目录），以及 REA、Grok Bot 两个文案投喂型 Agent 的用法与适配要点。README 同步增加宿主表与一行安装命令。
- README 快速开始示例由 LaunchMotion 改为 REA。

## v1.0.0 - 2026-10-22

首个公开版。

- 七阶段生成流程：语义解剖、任务类型识别、领域建模、反向设计、执行优化、文案生成、质量门。
- 双输出模式：模式 A 可复制文案（默认，给 REA 等执行型 Agent），模式 B Agent Skills 文件版。
- 五份 references：解剖工作表、设计维度、输出模板、质量门、跨宿主移植。
- 两份验证样例（技术逆向类与研究决策类），验证非模板套用。
- 工程自检脚本 `tools/validate.py`。
