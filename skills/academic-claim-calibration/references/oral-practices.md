# Oral-derived practices / Oral 论文启发的做法

## 目的 / Purpose

本文件把上游 `Adkid-Zephyr/oral-paper-skill` 公开文档中描述的七项编辑做法，重新整理成适合本项目的审查问题。它们用于帮助作者比较、改进和复盘，不用于预测录用，也不构成所有优秀论文的共同规律。

This document reframes the seven editorial practices described in the public documentation of the upstream `Adkid-Zephyr/oral-paper-skill` as review questions for this project. They support comparison, revision, and reflection. They do not predict acceptance or define universal properties of exemplary papers.

上游项目报告在六个会议周期的官方名单中处理了 884 个条目，其中 883 个被视为合格摘要，并说明其工作主要是摘要级的 AI 辅助提取、交叉综合和部分原文核查。这里的数字和范围是上游项目的自述，不是本项目重新完成的研究，也不是效果评估。

The upstream project reports processing 884 entries from six conference cycles, with 883 treated as eligible abstracts. It describes AI-assisted abstract-level extraction, cross-paper synthesis, and selected source checks. These counts and scope statements are reported by the upstream project; this repository did not reproduce the corpus analysis and does not treat them as an effectiveness evaluation.

## 七项做法 / Seven practices

| 做法 / Practice | 审查问题 / Review question | 重要边界 / Important boundary |
| --- | --- | --- |
| 研究张力 / Research tension | 哪个具体要求、观察或矛盾使这个问题值得研究？ / What concrete requirement, observation, or discrepancy makes the question worth studying? | 不制造现有方法失败，不把一般重要性写成未经支持的缺口。 / Do not invent a prior-work failure or an unsupported gap. |
| 贡献增量 / Contribution delta | 去掉方法名和“创新”后，究竟改变了什么？ / What changes after removing the method name and novelty label? | 发现、资源或描述性结果可以有自己的贡献形式，不必强行包装成新方法。 / Discoveries, resources, and descriptive findings need not be forced into a new-method frame. |
| 主张—证据匹配 / Claim–evidence match | 实际测量或证明的属性是否就是标题和摘要声称的能力？ / Is the measured or proved property the capability claimed in the title or abstract? | 代理指标、假设、计划和已报告结果必须分开。 / Keep proxies, hypotheses, plans, and reported findings distinct. |
| 有解释力的比较 / Meaningful comparison | 比较要解决哪个决策问题，哪些条件相同，哪些条件不同？ / What decision should the comparison resolve, and what stays fixed or changes? | 换比较口径不能用来逃避不利结果；不同口径回答的是不同问题。 / A changed comparator cannot be used to evade an unfavorable result; it answers a different question. |
| 结论带着条件 / Conditions beside conclusions | 哪个模型类别、人群、量词、保证条件、范围或数值口径不能省略？ / Which model class, population, quantifier, guarantee condition, scope, or numerical convention must remain visible? | 摘要没有写出的条件不能凭直觉补齐；实验结果不能写成形式保证。 / Do not fill missing conditions from intuition or turn empirical results into formal guarantees. |
| 资源能做什么 / What a resource enables | 数据、代码、基准或接口让别人具体能做什么？ / What can another researcher actually do with the data, code, benchmark, or interface? | 区分计划用途、已展示用途和已经发布的内容。 / Distinguish intended uses, demonstrated uses, and what is actually released. |
| 有边界的结论 / Bounded lesson | 读者应理解什么，什么条件会限制迁移？ / What should readers understand, and what condition would limit transfer? | 一项描述性结果不自动提供机制或普遍设计规则。 / A descriptive result does not automatically provide a mechanism or universal design rule. |

## 阅读层级 / Reading levels

- **摘要级 / Abstract level:** 可以支持问题框定、作者明确声称的贡献和摘要中报告的结果。
- **全文级 / Full-text level:** 才能检查实验细节、图表、证明、统计方法、数据处理和更细的限制。
- **一般性建议 / General guidance:** 找不到可核验来源时可以给出，但必须明确它不是某篇论文的做法。

- **Abstract level:** Supports framing, explicitly stated contributions, and results reported in the abstract.
- **Full-text level:** Needed for experimental details, figures, proofs, statistical methods, data handling, and finer limitations.
- **General guidance:** Allowed when no verifiable source is available, but it must be labeled as general guidance rather than attributed to a paper.

## 使用规则 / Use rules

1. 每次只选一到三项与作者当前问题直接相关的做法。
2. 每条来源型建议都记录论文链接、定位信息和阅读层级。
3. 分开写“来源观察”“为什么可能适用”“对当前稿件的具体修改动作”和“重要例外”。
4. 不把 Oral 身份、论文数量或来源论文的排名写成正确性、因果效果或录用保证。
5. 不用来源论文替代作者对自己数据、方法和研究目的的判断。

1. Select only one to three practices directly relevant to the author's current problem.
2. Record the paper link, locator, and reading level for every source-based recommendation.
3. Separate the source observation, why it may apply, the action for the current draft, and the important exception.
4. Do not present Oral status, corpus counts, or a source paper's ranking as proof of correctness, causality, or acceptance.
5. Do not use a source paper to replace the author's judgment about their own data, methods, or research purpose.

## 来源 / Source

上游项目：[Adkid-Zephyr/oral-paper-skill](https://github.com/Adkid-Zephyr/oral-paper-skill)，主分支固定提交 `a2c4bc41b3aa6946b2ccce1c844ce9936ef83308`（核验日期：2026-10-17）。该仓库公开文件列表中没有发现 LICENSE 文件；本项目没有复制其长段落或示例，只对公开概念做独立整理。其完整范围、误差记录和限制应以原仓库为准。

Upstream project: [Adkid-Zephyr/oral-paper-skill](https://github.com/Adkid-Zephyr/oral-paper-skill), main commit `a2c4bc41b3aa6946b2ccce1c844ce9936ef83308` (checked 2026-10-17). No LICENSE file was visible in the public file list inspected for that repository. This project does not copy long passages or examples; it independently reorganizes the public concepts. The upstream repository remains the source for its own scope, error records, and limitations.
