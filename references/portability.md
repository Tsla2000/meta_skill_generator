# 安装与移植说明：宿主支持矩阵

本生成器与它生成的 Skill 按「一份正文，多宿主可用」设计。宿主分两类：原生支持 Agent Skills 开放规范的，直接放文件；文案投喂型的，把生成的文案整份交给它执行。

## 原生 Skills 宿主

同一套文件（带 frontmatter 的 `SKILL.md` 加 `references/`、`examples/`、`tools/`），只有放置目录不同。文件夹名保持 kebab-case 并与 frontmatter 的 name 一致。

| 宿主 | 个人级目录 | 项目级目录 | 备注 |
|---|---|---|---|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` | 也可用 `npx skills add <owner/repo> -g -a '*'` 一键装 |
| OpenAI Codex | `~/.agents/skills/` | `.agents/skills/` | 启动时只读 name 与 description 渐进加载，描述里触发词靠前写 |
| Gemini CLI | `~/.gemini/skills/`（或别名 `~/.agents/skills/`） | `.gemini/skills/`（或别名 `.agents/skills/`） | 可用 `gemini skills install <git-url> --consent` 从 Git 仓安装，`/skills list` 查看已发现的技能，激活技能时有确认提示 |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` | 也兼容读取 `.claude/skills/` 与 `.agents/skills/` |
| GitHub Copilot / VS Code | `~/.copilot/skills/` | `.github/skills/` | 也读 `.claude/skills/` 与 `.agents/skills/` |
| 其他遵循 agentskills.io 的宿主 | 查该宿主文档的 skills 目录 | 同左 | 正文与 references 不改，只换目录 |

## Muse

- 位置：`~/workspace/custom-skills/<skill_name>/`，文件夹名用 snake_case。
- `SKILL.md` 不写 frontmatter，元数据放同目录 `skill.yaml`（name、title、description、category、include_in_prompt）。
- 装好后用 `muse.skill_search` 以目标关键词检索一次，命中才算安装成功。
- 本生成器在 Muse 里的安装版就是这套形态，与本仓库双向同步：仓库 SKILL.md 的 frontmatter 与 skill.yaml 的 name、description 必须一致，改一处同步另一处。

## 文案投喂型 Agent（非原生宿主）

这类宿主没有 Skills 目录机制，用法是先由任一原生宿主或 Muse 按本生成器产出模式 A 文案，再整份投喂。

| 宿主 | 用法 | 适配要点 |
|---|---|---|
| REA | 把模式 A 文案作为任务指令直接交给 REA 执行 | 文案中的证据与验收要求原样保留，这正是 REA 的工作方式 |
| Grok Bot（GrokBot） | 把 SKILL.md、skill.yaml、references 打包成 zip 投喂，或整份粘贴文案 | 在包的 README 里注明哪些是原宿主专有实现（如 Muse 的凭证与工具名），GrokBot 需映射成自己的等价能力 |
| 其他聊天型 Agent | 整份粘贴模式 A 文案作为会话指令 | 投喂前删掉指向本地路径与专有工具名的句子，换成该宿主的等价说法 |

## 已知限制

- 各宿主的发现方式不同：开放规范宿主靠 frontmatter 与目录扫描，Muse 靠 skill.yaml 与 skill_search。双投时两套元数据要同步改，漏一处会导致某个宿主搜不到。
- 部分宿主对 frontmatter 有私有扩展字段，这些字段跨宿主不携带。本生成器只使用 name 与 description 两个标准字段，保证最大可移植性。
- 本生成器只保证文案质量，不保证宿主的工具与权限。生成的 Skill 在新宿主首次使用时，先跑它自带的「开工前检查」一节再正式执行。
- Grok Bot 与 REA 是投喂型而非原生宿主，不要向用户宣称它们「安装」了 Skill，准确说法是「投喂了文案或技能包」。
