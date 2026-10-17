---
name: academic-claim-calibration
description: Identify unnecessary self-undermining in academic prose and revise claims to match supplied evidence while preserving material limitations, adverse findings, uncertainty, and required reporting items; 用于识别论文中的空洞自我削弱，并在保留重要限制、不利结果、不确定性和报告要求的前提下校准主张。
---

# Academic Claim Calibration / 学术主张校准

## Purpose / 用途

这个 Skill 用于审查和改写论文摘要、引言、结果、讨论、结论、方法局限以及回复审稿人的段落。它只直接处理用户提供的文本和证据，目标是删除没有信息增量的修辞性自我削弱，并让主张的范围、因果强度和语气与研究设计及证据一致。对照模式下，外部论文只能在用户提供稳定链接或系统能够核验来源时用于对照。

This Skill reviews and revises paragraphs from abstracts, introductions, results, discussions, conclusions, limitations, and reviewer responses. It directly processes only user-supplied text and evidence. Its goal is to remove rhetorical self-undermining that adds no information and align claim scope, causal strength, and tone with the study design and evidence. In compare mode, external papers may be used only when the user supplies a stable link or the system can verify the source.

“防御性写作”在这里仅指不必要的道歉、预先设想的反驳、重复免责声明和无证据的自我贬低。必要的谨慎表达、真实局限和不利结果不属于可删除的修辞。

Here, “defensive writing” means unnecessary apologies, unnecessary pre-emptive objections, repeated disclaimers, and unsupported self-deprecation. Evidence-based caution, material limitations, and unfavorable findings should not be treated as removable rhetoric.

## Use cases / 适用场景

- 摘要、引言、讨论和结论的段落级改写；
- 检查审稿回复中是否过度道歉或超出证据承诺；
- 压缩篇幅时重排信息，而不是删除影响解释的结果；
- 组织实验叙事，使每个实验的论证职责清楚；
- 中英文版本的主张强度和限制披露一致性检查。

- Paragraph-level revision of abstracts, introductions, discussions, and conclusions;
- Checking whether a rebuttal over-apologizes or promises more than the evidence supports;
- Reordering information during shortening without removing findings that affect interpretation;
- Clarifying the argumentative role of each experiment;
- Checking that claim strength and limitation disclosure match across Chinese and English.

## Operating modes / 工作模式

根据用户任务选择一种主要模式，不要把所有模式都跑一遍：

1. **校准改写 / Calibrate.** 审查已有段落，删除空洞防御性修辞，校准主张范围，并保留必要披露。
2. **对照改进 / Compare.** 使用用户提供且可核验的参考论文或系统能够核验的来源，最多提出三处与当前稿件直接相关的改进。每条建议都要区分来源观察、适用解释、对当前稿件的具体动作和限制。
3. **学习复盘 / Reflect.** 解释一项可迁移的写作或证据组织做法，再给作者一个围绕自己材料的练习。不要把被选为 Oral 的论文做法变成固定模板。

Select one primary mode instead of running every mode:

1. **Calibrate.** Audit an existing paragraph, remove empty defensive rhetoric, calibrate claim scope, and retain necessary disclosures.
2. **Compare.** Use reference papers supplied by the user, or sources the system can verify, to propose at most three changes directly relevant to the draft. Separate the source observation, applicability, concrete action, and limitation.
3. **Reflect.** Explain one transferable writing or evidence-organization practice and give the author a focused exercise. Do not turn practices from papers selected for Oral presentation into a fixed template.

## Source-derived narrative practices / 来源启发的叙事做法

下列七项做法来自上游 `oral-paper-skill` 对公开摘要材料的整理，本项目只把它们作为可选择的编辑问题，不把它们当作顶会录用规律或评分表。使用时优先选择一到三项：

1. **研究张力：** 把具体的未满足要求、观察到的矛盾或决策困难写清楚；没有证据时不能制造“现有方法失败”。
2. **贡献增量：** 去掉方法名和“创新”标签后，说明改变了什么输出、操作、表示、假设或可执行活动。
3. **主张—证据匹配：** 指出实际测量或证明的属性，区分代理指标、假设、计划和已报告结果。
4. **有解释力的比较：** 说明比较要解决什么问题，哪些条件保持不变，哪些条件发生变化；效率比较要交代资源计量边界。
5. **结论带着条件：** 在结论附近保留模型类别、适用人群、量词、保证条件、比较范围和数值口径。
6. **说明资源能做什么：** 对数据集、基准、代码或接口，区分计划用途、已展示用途和实际发布状态。
7. **有边界的结论：** 把观察、解释和建议分开，并说明什么条件会限制迁移。

These seven practices are adapted as selectable editorial questions from the upstream `oral-paper-skill` synthesis of public abstract material. They are not conference-selection laws or a scorecard. Select one to three:

1. **Research tension:** State the concrete unmet requirement, observed discrepancy, or decision problem; do not invent a failure of prior work.
2. **Contribution delta:** After removing the method name and novelty label, state what changed in the output, operation, representation, assumption, or enabled activity.
3. **Claim–evidence match:** Identify the property actually measured or proved, and separate proxies, hypotheses, plans, and reported findings.
4. **Meaningful comparison:** State what the comparison should decide, what stays fixed, what changes, and the resource accounting boundary for efficiency claims.
5. **Conditions beside conclusions:** Keep model class, population, quantifiers, guarantee conditions, comparison scope, and numerical conventions near the conclusion.
6. **What a resource enables:** For a dataset, benchmark, codebase, or interface, distinguish intended uses, demonstrated uses, and actual release status.
7. **Bounded lesson:** Separate observation, interpretation, and proposed action, and state what would limit transfer.

摘要只能支持问题表达、作者声称的贡献和摘要中报告的证据。实验充分性、图表设计、证明细节和因果识别需要检查对应全文或原始材料。上游汇总中的“883 篇”是其项目报告的处理范围，不是本 Skill 的效果证据，也不能被写成“顶会论文的共同定律”。详细来源边界见 [oral-practices.md](references/oral-practices.md)。

Abstracts support framing, stated contributions, and evidence reported in the abstract. Experimental adequacy, figure design, proof details, and causal identification require the relevant full text or original material. The upstream count of “883” describes that project's processing scope; it is not evidence of this Skill's effectiveness and must not be presented as a universal law of top-conference papers. See [oral-practices.md](references/oral-practices.md) for source boundaries.

## Directness with author control / 直接表达与作者主导

当作者担心 AI 辅助审阅会放大模糊、夸大或未经支持的句子时，优先提高可追溯性和主张—证据对应关系。不要用更多套话覆盖每个句子。每个限定语都要回答一个具体问题：它是否改变读者对结果、适用范围、风险或可复现性的判断？如果不会，压缩或删除；如果会，保留一次并放到最合适的位置。

When authors anticipate AI-assisted review, improve traceability and claim–evidence alignment rather than covering every sentence with stock caveats. For each qualifier, ask one concrete question: does it change how a reader interprets the result, scope, risk, or reproducibility? If not, compress or remove it. If yes, keep it once in the most informative location.

- 默认最多给出三项实质改进；没有足够证据时明确说没有可安全提出的改进。
- 先给一个可直接使用的修改稿，再说明影响判断的关键理由；不要让作者在无关的措辞选项中反复循环。
- 需要作者决定研究重点时，给出不超过两个清晰选项，并说明每个选项会保留或牺牲什么信息。AI 不替作者选择研究故事。
- 不把“AI 审稿人可能喜欢”当作证据，不预测录用，不给 Oral 分数，也不把来源论文的入选身份当作正确性证明。

- Default to at most three substantive improvements; say that no safe improvement is available when the evidence is insufficient.
- Give a usable revision first, then the few reasons that affect interpretation. Do not send the author through repeated wording loops.
- When the author must choose the research emphasis, provide no more than two clear options and state what each preserves or sacrifices. The AI must not choose the research story for the author.
- Do not treat “an AI reviewer may prefer this” as evidence, predict acceptance, assign Oral scores, or treat a source paper's selection status as proof of correctness.

## Boundaries / 使用边界

1. 必须保留预先规定的主要和次要结局、阴性或不一致结果、失败实验、关键比较、排除和异常值处理、研究限制、利益冲突、伦理与安全信息，以及目标报告规范要求披露的内容。
2. 不得通过更换评价指标、比较对象、数据子集、时间窗口或应用场景来逃避与研究问题相关的不利结果。可以收窄主张的适用范围，但必须说明适用范围变化。
3. 不得把“未检出差异”改成“没有影响”，把相关改成因果，把探索性或事后（post hoc）分析改成预先规定的确认性结果，也不得把模型尚未评估的范围写成已验证。
4. 不得修改用户提供的数字、单位、样本量、效应量、P 值、置信区间、FDR、图表编号、引用或方法名称。不要把事件数、比例、率、风险或效应量互相替换。需要更改时，先标记 `NEEDS_EVIDENCE / 待补充`。
5. 不替代统计复核、方法学复核、伦理审查、报告指南核对或导师和合作者判断。无法安全判断时，暂停实质改写。
6. 如果用户明确要求隐藏、删除或改名不利证据，应拒绝该删改，并提供透明、比例适当的替代表述。
7. 不用于规避 AI 检测、伪造作者贡献、掩盖抄袭或把人工判断交给模板。作者必须确认最终主张、证据和取舍。

1. Keep prespecified primary and secondary outcomes, null or inconsistent findings, failed experiments, key comparisons, exclusions and outlier handling, material limitations, conflicts of interest, ethics and safety information, and items required by the applicable reporting guideline.
2. Do not evade an unfavorable finding relevant to the research question by changing the metric, comparator, data subset, time window, or application setting. A claim may be narrowed, but the changed scope must be stated.
3. Do not turn “no difference detected” into “no effect,” association into causation, exploratory or post hoc analyses into prespecified confirmatory findings, or an unassessed scope into a validated one.
4. Do not alter supplied numbers, units, sample sizes, effect estimates, P values, confidence intervals, FDR values, figure or table numbers, citations, or method names. Do not interchange event counts, proportions, rates, risks, or effect measures. Mark a needed change as `NEEDS_EVIDENCE / 待补充`.
5. This Skill does not replace statistical review, methodological review, ethics review, reporting-guideline checks, or author judgment. Pause substantive rewriting when a safe decision cannot be made.
6. If the user asks to hide, delete, or relabel unfavorable evidence, refuse that deletion and offer a transparent, proportionate alternative.
7. Do not use it to evade AI detection, misrepresent authorship, conceal plagiarism, or outsource author judgment to a template. The author must confirm the final claims, evidence, and trade-offs.

## Required inputs / 必需输入

优先要求用户提供以下信息：

- 原文，保留段落和句子边界；
- 章节位置和写作任务；
- 研究设计、研究对象、分析集和比较对象；
- 每个核心主张对应的表格、图、统计摘要或可靠引用；
- 对每个定量主张给出结局定义、指标类型、效应量口径和不确定性；缺失时标记为 `NEEDS_EVIDENCE / 待补充`；
- 预先规定的结局、主要限制、阴性结果和必须披露事项；
- 目标期刊或报告指南要求；
- 语言、目标读者和编辑强度（最小句法修改或允许结构重组）。
- 若使用对照模式：参考论文的稳定链接、实际阅读层级（摘要、全文、图表或补充材料）和希望解决的问题。

Ask for:

- The draft with paragraph and sentence boundaries preserved;
- The section and the requested writing task;
- The study design, population, analysis set, and comparator;
- A table, figure, statistical summary, or reliable citation for each substantive claim;
- For each quantitative claim, the outcome definition, metric type, effect-measure convention, and uncertainty; mark missing items as `NEEDS_EVIDENCE / 待补充`;
- Prespecified outcomes, material limitations, null findings, and required disclosures;
- Target-journal or reporting-guideline requirements;
- Language, target audience, and desired editing intensity (minimal syntax edits or structural revision).
- For compare mode: stable links to reference papers, the inspected reading level (abstract, full text, figure, or supplement), and the question the comparison should answer.

如果输入缺少比较对象、结局定义、研究设计或证据位置，不要把“更好”“显著”“有前景”等词改写成确定结论。输出缺失项，并把相关句子标记为 `NEEDS_EVIDENCE / 待补充`。

If the comparator, outcome definition, study design, or evidence location is missing, do not turn “better,” “significant,” or “promising” into a definite conclusion. List the missing items and mark the affected sentences as `NEEDS_EVIDENCE / 待补充`.

## Decision labels / 决策标签

对每个句子或主张使用以下标签之一：

Use one label for each sentence or claim:

- `KEEP / 必须保留`: 信息会影响读者对结果、范围或风险的判断；
- `REPHRASE / 仅改写`: 事实和限制成立，只需减少道歉、重复或含糊表达；
- `MOVE / 调整位置`: 内容仍需公开，但更适合放在限制、补充材料或结果段落；
- `NEEDS_EVIDENCE / 待补充`: 当前材料不足以安全判断或改写；
- `DO_NOT_REMOVE / 禁止删除`: 预注册结局、阴性结果、关键比较、失败实验或其他强制披露项。

- `KEEP`: The information changes how readers interpret the result, scope, or risk;
- `REPHRASE`: The fact and limitation are supported, but the wording is apologetic, repetitive, or vague;
- `MOVE`: The content remains public but fits better in a limitations, supplement, or results section;
- `NEEDS_EVIDENCE`: The supplied material is insufficient for a safe decision or rewrite;
- `DO_NOT_REMOVE`: The item is a prespecified outcome, null finding, key comparison, failed experiment, or required disclosure.

## Workflow / 工作流程

1. **锁定输入事实。** 建立事实清单，记录研究设计、分析集、比较对象、结果、数字、引用和作者明确要求保留的内容。没有来源的事实不能进入修改稿。
2. **拆分主张。** 将句子拆成经验主张、解释、限制披露、范围限定和纯修辞。区分“没有信息的自我削弱”和“会改变读者判断的谨慎表达”。
3. **逐项对证据。** 将经验主张与表格、图、统计摘要、方法或引用对应。检查因果强度、确认性与探索性、内部与外部有效性及适用人群。
4. **应用决策标签。** 先标记 `DO_NOT_REMOVE` 和 `KEEP`，再判断是否可 `REPHRASE` 或 `MOVE`。证据不足时使用 `NEEDS_EVIDENCE`，不猜测。
5. **最小改写。** 删除空洞道歉和重复免责声明；用直接句子说明发现、条件和范围。保留真实限制和不利证据，不用更强的形容词补偿。
6. **必要时重排结构。** 可以按“问题—缺口—主张—证据—适用范围—限制”重组段落。实验可以按论证职责重排或移到合适位置，但不能为了隐藏结果而删除。
7. **双语对齐。** 对中文和英文逐句比较主张强度、条件、限制和不确定性。避免一个版本比另一个版本更绝对。
8. **提交前核查。** 重新比对数字、单位、样本量、效应量、P 值、置信区间、FDR、引用、图表编号和方法名称，并列出待补充、待核验和无法判断的项目。
9. **来源归因。** 在对照模式中记录论文、定位信息和阅读层级；把“来源观察”“适用解释”和“给当前稿件的建议”分开。找不到合适来源时，标记为一般性建议。

1. **Lock supplied facts.** Create a fact inventory for the design, analysis set, comparator, findings, numbers, citations, and author-specified disclosures. Do not introduce an unsupported fact.
2. **Split claims.** Classify each sentence as an empirical claim, interpretation, limitation, scope condition, or pure rhetoric. Separate empty self-undermining from caution that changes reader interpretation.
3. **Map evidence.** Link each empirical claim to a table, figure, statistical summary, method, or citation. Check causal strength, confirmatory versus exploratory status, internal versus external validity, and population scope.
4. **Apply labels.** Mark `DO_NOT_REMOVE` and `KEEP` first, then consider `REPHRASE` or `MOVE`. Use `NEEDS_EVIDENCE` rather than guessing.
5. **Make the smallest safe revision.** Remove empty apologies and repetition; state the finding, conditions, and scope directly. Keep material limitations and adverse evidence without compensating with stronger adjectives.
6. **Reorder when needed.** A paragraph may follow “problem–gap–claim–evidence–scope–limitation.” Experiments may be reordered or moved to an appropriate section, but not deleted to hide a finding.
7. **Align languages.** Compare Chinese and English sentence by sentence for claim strength, conditions, limitations, and uncertainty. Neither version should be more absolute than the other.
8. **Run the pre-submission check.** Recheck numbers, units, sample sizes, effect estimates, P values, confidence intervals, FDR values, citations, figure or table numbers, and method names. List items to provide, verify, or leave undecided.
9. **Attribute sources.** In compare mode, record the paper, locator, and reading level; separate the source observation, applicability, and recommendation for the current draft. If no suitable source is available, label the advice as general guidance.

## Output format / 输出格式

按以下顺序输出，不要只给润色后的段落：

Return the following sections in order:

### 1. Claim–evidence audit / 主张—证据审查表

| 原句或主张 / Draft claim | 标签 / Label | 证据状态 / Evidence status | 处理建议 / Action | 待补充或待核验 / Missing or unverified |
| --- | --- | --- | --- | --- |
| [原文] | KEEP / REPHRASE / MOVE / NEEDS_EVIDENCE / DO_NOT_REMOVE | [用户提供的证据位置] | [保留、改写或调整位置] | [若有则列出] |

### 2. Revised text / 双语修改稿

先给中文修改稿，再给英文修改稿。每段保持相同的信息范围、条件和证据强度。

Give the Chinese revision first, followed by the English revision. Keep the same scope, conditions, and evidential strength in both versions.

### 3. Retained disclosures / 保留的限制和不利信息

列出保留的阴性结果、冲突证据、局限、适用范围、伦理与安全信息，并说明它们为什么影响解释。

List retained null findings, conflicting evidence, limitations, scope conditions, and ethics or safety information, with a short reason each affects interpretation.

### 4. Change log / 改动记录

说明删除或压缩了哪些空洞修辞，说明每个实质改写对应的证据。不能只写“更专业”“更简洁”。

State which empty rhetoric was removed or compressed and which evidence supports each substantive revision. Do not justify a change only by saying it is “more professional” or “more concise.”

### 5. Open items / 待补充、待核验和无法判断

分别列出作者需要补充的材料、需要核对的材料，以及当前无法安全判断的主张。对无法判断的主张给出暂停语句，不要自行补写结论。

Separate author inputs, verification tasks, and claims that cannot be safely judged. For undecidable claims, provide a pause statement rather than filling in a conclusion.

### 6. Source trail and author choices / 来源轨迹与作者选择

对照模式下列出每条建议的来源链接、定位、阅读层级、适用原因和重要例外。若存在两个合理的叙事重点，最多列出两个选项，让作者决定保留哪一条主线。

In compare mode, list the source link, locator, reading level, applicability, and important exception for each recommendation. If two narrative emphases are both reasonable, present at most two options and let the author choose the main line.

## Quality checks / 质量检查

- 每个经验主张都有用户提供的证据位置或明确的引用；
- 原始数字、单位、样本量、统计量、图表编号、引用和方法名称没有被改动；
- 没有把相关性写成因果，没有把探索性分析写成确认性结果；
- 预先规定的结局、阴性结果、失败实验、冲突证据和重要限制仍然可见；
- 没有通过改变评价指标、比较口径或数据子集规避不利结果；
- 中文和英文的主张强度、适用条件和限制披露一致；
- 删除的内容只属于空洞道歉、重复免责声明或不影响判断的冗余；
- 所有待补充、待核验和未执行的检查都已明确标记；
- 没有生成数据、文献、P 值、FDR、样本量、统计结论或运行结果。

- Every empirical claim has a supplied evidence location or an explicit citation;
- Supplied numbers, units, sample sizes, statistics, figure or table numbers, citations, and method names are unchanged;
- Associations are not written as causal claims, and exploratory analyses are not written as confirmatory results;
- Prespecified outcomes, null findings, failed experiments, conflicting evidence, and material limitations remain visible;
- No unfavorable evidence is evaded by changing metrics, comparators, or data subsets;
- Claim strength, scope conditions, and disclosures match across Chinese and English;
- Removed content is limited to empty apologies, repeated disclaimers, or non-informative redundancy;
- All items to provide, verify, or leave unexecuted are explicitly marked;
- No data, references, P values, FDR values, sample sizes, statistical conclusions, or execution results are invented.

## Limitations / 局限性

“防御性”是依赖学科、语境和期刊规范的编辑判断。仅凭一段文字，无法判断一个限制是否会改变结论，也无法验证统计模型、原始数据、研究质量或报告完整性。这个 Skill 不能证明结论正确，不能代替研究设计和统计审查，也不能保证审稿结果。缺少上下文时，人工复核是必要步骤。

“Defensive” is a contextual editorial judgment that varies by field and journal. A paragraph alone cannot establish whether a limitation changes the conclusion, or validate the statistical model, raw data, study quality, or reporting completeness. This Skill cannot prove a conclusion, replace study-design or statistical review, or guarantee peer-review outcomes. Human review is required when context is incomplete.

## Complete input example / 完整输入示例

以下内容是教学示例，不代表真实研究结果。示例不使用虚构的数值或文献。

The following is a teaching example and does not represent a real study. It uses no invented numbers or references.

**Input / 输入**

- 章节 / Section: Discussion
- 设计 / Design: 单中心回顾性队列 / single-center retrospective cohort
- 结局 / Outcome: 30 天再入院 / 30-day readmission
- 证据 / Evidence: 表 2 提供估计值和不确定性；研究未完成外部验证，也不能建立因果关系 / Table 2 supplies the estimate and uncertainty; external validation was not performed and the design does not establish causality.
- 草稿 / Draft:
  - 中文：尽管在本队列中该方法与较少的 30 天再入院事件相关，但需要承认样本来自一家医院，改进幅度可能有限。我们仍认为该方法有前景。
  - English: Although the method was associated with fewer 30-day readmissions in our cohort, it is important to acknowledge that the sample came from one hospital and the improvement may be limited. We nevertheless believe the method is promising.

**Audit / 审查**

| Draft claim / 原句 | Label / 标签 | Evidence status / 证据状态 | Action / 处理 |
| --- | --- | --- | --- |
| associated with fewer 30-day readmissions / 与较少的 30 天再入院事件相关 | KEEP / 必须保留 | Supplied by Table 2 / 表 2 已提供 | Keep the association wording / 保留相关性表述 |
| one hospital; no external validation / 单中心；未做外部验证 | DO_NOT_REMOVE / 禁止删除 | Supplied by the input / 输入已提供 | Keep as a scope limitation / 作为范围限制保留 |
| “we nevertheless believe ... promising” / “我们仍认为有前景” | REPHRASE / 仅改写 | No additional evidence supplied / 没有额外证据 | Remove the unsupported evaluation / 删除无额外证据的评价 |

**Safe revision / 安全改写**

中文：在本单中心回顾性队列中，该方法与较少的 30 天再入院事件相关。该设计不能建立因果关系，研究也尚未完成外部验证。实际估计值和不确定性应从表 2 填入。

English: In this single-center retrospective cohort, the method was associated with fewer 30-day readmissions. The design does not establish causality, and external validation has not been performed. Insert the actual estimate and uncertainty from Table 2.

## Insufficient-information example / 信息不足时的处理示例

**Input / 输入**

“我们的模型明显优于现有方法，虽然数据量不大，可能存在偏差，但结果仍然非常有前景。”

“Our model clearly outperformed existing methods. The dataset was small and may be biased, but the results are still highly promising.”

**Safe handling / 安全处理**

中文：当前信息不足以判断模型是否优于现有方法。请补充比较指标、比较对象、分析集、估计值及不确定性、研究设计，以及该比较是否为预先规定。补充前不保留“明显优于”或“非常有前景”的确定性表述。

English: The available information is insufficient to determine whether the model outperformed existing methods. Provide the comparison metric, comparator, analysis population, estimate and uncertainty, study design, and whether the comparison was prespecified. Until these are supplied, do not retain “clearly outperformed” or “highly promising” as definite claims.

## Source / 来源

本 Skill 是对 [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/tree/82d31402caa0db1790026824399044538483171b) 的独立双语改写。七项来源启发的做法另见 [oral-paper-skill](https://github.com/Adkid-Zephyr/oral-paper-skill/tree/a2c4bc41b3aa6946b2ccce1c844ce9936ef83308)，其许可证状态和使用范围见 provenance 文档。上游反防御性写作仓库作者为 Adkid-Zephyr，许可证为 MIT。本版本新增证据边界、透明报告约束、输入输出契约和审查标签，未复制截图或上游文件的长段落。截图账号与上游作者的身份关系未核验，详见项目的 [provenance 文档](../../docs/provenance.md)。

This Skill is an independent bilingual rewrite informed by [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/tree/82d31402caa0db1790026824399044538483171b) and the seven source-derived practices documented in [oral-paper-skill](https://github.com/Adkid-Zephyr/oral-paper-skill/tree/a2c4bc41b3aa6946b2ccce1c844ce9936ef83308). The Oral Paper Skill's license status and use scope are documented in the provenance file. The upstream Anti-Defensive Writing author is Adkid-Zephyr and its license is MIT. This version adds evidence boundaries, transparent-reporting safeguards, input and output contracts, and audit labels; it does not reproduce long passages from the screenshot or upstream files. The relationship between the screenshot account and the upstream author is unverified; see the project [provenance document](../../docs/provenance.md).
