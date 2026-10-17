# Academic Claim Calibration / 学术主张校准

[![Validate project](https://github.com/Qin-jiahao/academic-claim-calibration/actions/workflows/validate.yml/badge.svg)](https://github.com/Qin-jiahao/academic-claim-calibration/actions/workflows/validate.yml)

一个面向科研写作的双语 Skill 和 Prompt。它帮助研究者识别没有信息增量的自我削弱、重复免责声明和无证据的预先辩解，再把表述调整到证据能够支持的范围内。

A bilingual Skill and prompt for research writing. It identifies unhelpful self-undermining, redundant disclaimers, and unsupported pre-emptive defenses, then calibrates the wording to the supplied evidence.

## 项目定位 / Project scope

本项目把两个公开项目的可用思路重新整合：[Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/tree/82d31402caa0db1790026824399044538483171b) 提供直接、聚焦贡献的表达视角；[Adkid-Zephyr/oral-paper-skill](https://github.com/Adkid-Zephyr/oral-paper-skill/tree/a2c4bc41b3aa6946b2ccce1c844ce9936ef83308) 提供来源可追溯的论文对照和复盘思路。本项目把两者改写成“证据边界内的学术主张校准”，补充透明报告、不利结果保留和作者决策规则。项目没有复制截图或上游文件的长段落。

This project is an independent bilingual synthesis of two public projects: [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/tree/82d31402caa0db1790026824399044538483171b) contributes a direct, contribution-focused writing perspective, while [Adkid-Zephyr/oral-paper-skill](https://github.com/Adkid-Zephyr/oral-paper-skill/tree/a2c4bc41b3aa6946b2ccce1c844ce9936ef83308) contributes source-linked comparison and reflection. This project reframes both as evidence-bounded academic claim calibration and adds safeguards for transparent reporting, retention of adverse findings, and author control. It does not reproduce the screenshot or copy long passages from upstream files.

### 这个项目解决什么问题 / What it addresses

- 删除道歉式开场、重复的“可能存在局限”以及没有新信息的自我否定。
- 把每个关键主张和研究设计、比较对象、结果或可靠引用对应起来。
- 保留会改变读者判断的阴性结果、冲突证据、主要限制、适用范围和伦理与安全信息。
- 让中文和英文的证据强度保持一致。
- 用一到三项来源可核验的做法帮助作者对照被选为 Oral 的论文案例，但不把 Oral 身份当作评分或录用保证。
- 限制 AI 的反复套话：必要限定只出现一次，默认最多给出三项实质改进，研究主线由作者确认。

- Remove apology-like openings, repeated caveats, and self-undermining language that adds no information.
- Link each substantive claim to the study design, comparator, result, or reliable citation that supports it.
- Keep null findings, conflicting evidence, material limitations, scope conditions, and ethics or safety information that affect interpretation.
- Keep the evidential strength aligned across Chinese and English versions.
- Use one to three source-traceable practices to compare with papers selected for Oral presentation, without treating Oral status as a score or acceptance guarantee.
- Limit repetitive caveating in AI-assisted revisions: keep each necessary qualifier once, give at most three substantive improvements by default, and leave the research emphasis to the author.

### 明确边界 / Non-goals and guardrails

本项目不提供选择性报告策略。它不能指导用户隐藏、删除、改名或弱化预先规定的主要结局、阴性结果、失败实验、异常值处理、排除决定、关键比较、利益冲突、伦理风险或报告规范要求。它也不能把相关性改写成因果关系，把探索性分析写成确认性结论，或通过更换评价指标来规避不利证据。

This project does not provide a selective-reporting strategy. It must not hide, delete, relabel, or weaken prespecified primary outcomes, null findings, failed experiments, outlier handling, exclusion decisions, key comparisons, conflicts of interest, ethics or safety information, or required reporting items. It must not turn associations into causal claims, exploratory analyses into confirmatory conclusions, or change the metric to evade unfavorable evidence.

## 快速开始 / Quick start

### 作为 Skill 使用 / Use as a Skill

把 [skills/academic-claim-calibration/SKILL.md](skills/academic-claim-calibration/SKILL.md) 复制到你使用的 Agent 工具的 skills 目录。提交原文时，同时提供研究设计、比较对象、主要结果、重要限制和目标期刊要求。没有这些信息时，Skill 应该暂停实质改写，并列出“NEEDS_EVIDENCE / 待补充”项目。

Copy [skills/academic-claim-calibration/SKILL.md](skills/academic-claim-calibration/SKILL.md) into the skills directory used by your Agent tool. Supply the study design, comparator, key findings, material limitations, and journal requirements together with the draft. When these inputs are missing, the Skill should pause substantive rewriting and list “NEEDS_EVIDENCE / 待补充” items.

### 安装说明 / Installation

当前版本以 Markdown 文件分发，不提供自动安装器。安装时请保留 `SKILL.md` 与其 `references/` 子目录的相对位置。不同 Agent 工具的 skills 目录位置不同，请以所用工具的文档为准。

This version is distributed as Markdown files and has no automatic installer. Keep `SKILL.md` together with its `references/` subdirectory. Skill-directory locations differ across Agent tools, so follow the documentation for the tool you use.

以 Codex 为例，可以在仓库根目录执行：

For Codex, run the following from the repository root:

```sh
mkdir -p "$HOME/.codex/skills/academic-claim-calibration/references"
cp skills/academic-claim-calibration/SKILL.md "$HOME/.codex/skills/academic-claim-calibration/"
cp skills/academic-claim-calibration/references/oral-practices.md "$HOME/.codex/skills/academic-claim-calibration/references/"
```

安装后可以运行 `python3 scripts/validate_project.py` 和 `ruby scripts/validate_frontmatter.rb` 检查本地文件。其他工具请把同样的两个文件复制到该工具文档指定的 skills 目录。

After installation, run `python3 scripts/validate_project.py` and `ruby scripts/validate_frontmatter.rb` to check the local files. For other tools, copy the same two files into the skills directory documented by that tool.

### 作为 Prompt 使用 / Use as a prompt

可直接复制 [prompts/academic-claim-calibration.md](prompts/academic-claim-calibration.md) 到支持长文本的对话中。Prompt 只处理用户提供的材料，不会替用户补写数据、文献、统计量或运行结果。

Copy [prompts/academic-claim-calibration.md](prompts/academic-claim-calibration.md) into a long-context conversation. The prompt works only with supplied material and must not invent data, references, statistics, or execution results.

## 建议输入 / Recommended input

至少提供以下信息：

At minimum, provide:

1. 需要修改的原文和章节位置；
2. 研究设计、研究对象或分析集；
3. 关键主张对应的表格、图、统计摘要或可靠引用；
4. 对每个定量主张提供结局定义、指标类型、效应量口径和不确定性；
5. 预先规定的结局、阴性结果和必须披露的限制；
6. 目标读者、语言和期望编辑强度；
7. 对照模式下的参考论文、定位信息和阅读层级。

1. The draft text and section location;
2. The study design, population, or analysis set;
3. The table, figure, statistical summary, or reliable citation supporting each key claim;
4. For each quantitative claim, the outcome definition, metric type, effect-measure convention, and uncertainty;
5. Prespecified outcomes, null findings, and limitations that must be disclosed;
6. The target audience, language, and desired editing intensity;
7. For compare mode, the reference papers, locators, and reading levels.

## 输出内容 / Expected output

每次使用都应包括主张—证据审查表、双语修改稿、保留的限制和不利结果清单、未解决问题，以及对数字、比较对象、因果强度和引用的核查说明。

Each run should include a claim–evidence audit table, a bilingual revision, a list of retained limitations and unfavorable findings, unresolved questions, source trails when comparison is used, and checks on numbers, comparators, causal strength, and citations.

## 审慎但不绕圈子 / Cautious without circular prose

本项目采用一个简单的停止规则：先处理会改变读者判断的限定，再删除重复和没有证据的自我辩解。一个句子如果已经给出研究条件、结果和必要限制，就不再追加同义的“需要谨慎解释”“可能存在不足”等套话。模型默认给出一版可直接使用的文本和最多三条实质理由；只有在主张、证据或作者目标存在冲突时，才要求作者做选择。

The project uses a simple stopping rule: handle qualifiers that change reader interpretation first, then remove repetition and unsupported self-defense. Once a sentence states the study condition, finding, and necessary limitation, do not add synonymous caveats such as “should be interpreted cautiously” without new information. The model returns one usable revision and at most three substantive reasons by default; it asks the author to choose only when claims, evidence, or goals conflict.

## 仓库结构 / Repository layout

    skills/academic-claim-calibration/SKILL.md  # 可安装 Skill / installable Skill
    skills/academic-claim-calibration/references/oral-practices.md  # 按需加载的参考 / on-demand reference
    prompts/academic-claim-calibration.md      # 双语 Prompt / bilingual prompt
    docs/provenance.md                          # 来源与许可证 / provenance and licensing
    docs/reference-basis.md                     # 学术依据 / reference basis
    docs/oral-practices.md                      # Oral 做法的独立整理 / independent Oral-practice synthesis
    scripts/validate_project.py                 # 无依赖静态检查 / dependency-free validation
    scripts/validate_frontmatter.rb             # YAML frontmatter 检查 / YAML frontmatter check
    .github/workflows/validate.yml              # GitHub Actions 检查 / GitHub Actions checks
    CONTRIBUTING.md                             # 双语贡献说明 / bilingual contribution guide
    LICENSE                                     # 本项目原创文件的 MIT 许可 / MIT for original files
    THIRD-PARTY-NOTICES.md                      # 上游署名与许可 / upstream attribution

## 来源和许可证 / Provenance and license

截图显示社交平台账号 @不是文三石（AI版），目前没有找到可以核验的原始帖子、作者关系或授权记录。截图只作为发现线索，不作为作者证明，也不会作为项目资产上传。两个上游项目、作者和许可证记录见 [docs/provenance.md](docs/provenance.md)。

The screenshot displays the social-media account @不是文三石（AI版）. The original post, author relationship, and reuse permission could not be verified. The screenshot is treated only as a discovery lead and is not uploaded as a project asset. The two upstream projects, authors, and license records are documented in [docs/provenance.md](docs/provenance.md).

本项目新增的原创改写文件采用 MIT License。这个许可只覆盖本项目有权发布的原创改写内容；它不自动覆盖没有明确许可证的上游 Oral Paper Skill。已核验的上游 MIT 版权和许可文本保留在 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) 中。许可证不代表本 Skill 能替代统计复核、方法学审查、伦理审查或目标期刊的正式要求。

Original rewritten files in this project are released under the MIT License. That license covers only original rewritten material that this project is entitled to publish; it does not automatically cover the upstream Oral Paper Skill, whose license was not verified. The verified upstream MIT copyright and license text is retained in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). The license does not make this Skill a substitute for statistical review, methodological review, ethics review, or the target journal's formal requirements.

## 学术依据 / Reference basis

本项目把“减少空洞修辞”和“保持科学谨慎”分开处理。相关依据和链接见 [docs/reference-basis.md](docs/reference-basis.md)，包括 Hyland 关于科学论文 hedging 的研究、Simera 与 Altman 关于适用性和透明报告的讨论，以及 EQUATOR Network 的报告指南资源。

The project separates the removal of empty rhetoric from the preservation of scientifically justified caution. The sources and links are listed in [docs/reference-basis.md](docs/reference-basis.md), including Hyland's work on hedging in scientific articles, Simera and Altman's discussion of fit-for-purpose reporting, and the EQUATOR Network reporting resources.

## 当前状态 / Current status

当前版本是初始公开草案。它已经完成结构化审阅和静态检查，仓库会在 Push 和 Pull Request 时运行这些检查，但没有在真实论文上进行系统评估，也没有证明能够提高接收率、引用量或审稿结果。使用者仍需逐项核对原始数据、分析脚本、图表、引用和期刊要求。

This is an initial public draft. It has undergone structural review and static checks, and the repository runs those checks on pushes and pull requests. It has not been systematically evaluated on real manuscripts and does not demonstrate improvements in acceptance, citations, or peer-review outcomes. Users must still verify the original data, analysis code, figures, citations, and journal requirements.

## 验证范围 / Validation scope

`scripts/validate_project.py` 检查必需文件、Skill 和 Prompt 的双语章节、Markdown 围栏代码块、Skill frontmatter 的基本字段和仓库内的相对链接。`scripts/validate_frontmatter.rb` 使用 Ruby 的 YAML 解析器检查 frontmatter 是否能被解析，以及 `name` 和 `description` 是否符合项目规则。GitHub Actions 会在推送和 Pull Request 时运行这些检查。

这些检查不验证外部链接是否仍然可访问，不判断统计方法和数字是否正确，不证明中英文语义完全等价，也不执行 Skill 或 Prompt 的 Agent 运行效果。真实稿件仍需要作者、合作者或导师逐项复核。

`scripts/validate_project.py` checks required files, bilingual sections in the Skill and prompt, fenced Markdown code blocks, basic Skill frontmatter fields, and repository-relative links. `scripts/validate_frontmatter.rb` uses Ruby's YAML parser to check that the frontmatter parses and that `name` and `description` meet the project rules. GitHub Actions runs these checks on pushes and pull requests.

These checks do not verify that external links remain reachable, judge whether statistical methods or numbers are correct, prove full semantic equivalence between Chinese and English, or execute the Skill or prompt in an Agent. Authors, collaborators, or supervisors must still review real manuscripts.

## 贡献 / Contributing

欢迎提交能提高可审计性、双语一致性和证据边界的修改。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并在提交中说明来源、改动范围、检查结果和仍待核验的内容。

Contributions that improve auditability, bilingual consistency, and evidence boundaries are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first, and record the source, scope of change, checks performed, and unresolved items in each contribution.
