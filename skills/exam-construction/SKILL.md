---
name: exam-construction
description: >
  Use this skill when the user asks to design, generate, review, revise, or assemble an examination paper, test blueprint, item bank, answer key, scoring rubric, or post-exam item analysis for a course. Best suited to higher-education and classroom assessments, including closed-book final exams, quizzes, formative tests, and course-level question banks. Do not use for unsupervised high-stakes certification, medical/legal licensing, admissions, employment selection, or psychometric instrument development without expert human review.
license: CC-BY-4.0
---

# Exam Construction Skill

## Core Principle

Construct examinations as evidence-based measurement instruments, not as loose collections of questions. Every item must be traceable to a learning objective, a content domain, and an intended cognitive process. Prioritize alignment, representativeness, score-interpretation clarity, reliability safeguards, validity evidence, fair difficulty, transparent scoring, and post-exam revision.

## Trigger Conditions

Use this skill when the user requests any of the following:

- “出一套试卷 / 设计试卷 / 生成考试题 / 编制题库 / 设计期末考试”
- “优化选择题 / 优化干扰项 / 检查试题质量 / 生成评分标准”
- “根据教学大纲、课件、教材或知识点生成考试”
- “制作 A/B 卷、答题纸、参考答案、评分细则、双向细目表”
- “分析考试结果、题目难度、区分度、信度或命题质量”

Do not use this skill for ordinary knowledge问答 unless the user is explicitly constructing or evaluating assessment materials.

## Required Inputs

Collect the following if available. If the user has already provided them, do not ask again.

1. Course name and target students.
2. Assessment purpose: final exam, midterm, quiz, diagnostic test, formative exercise, item bank, or review exercise.
3. Exam mode: closed-book, open-book, take-home, online, oral, or mixed.
4. Time limit and total score.
5. Teaching content: syllabus, lecture slides, textbook chapters, teacher notes, or knowledge-point list.
6. Question types and proportions: MCQ, multiple-select, true/false, fill-in, definition, short answer, essay, case analysis, calculation, data interpretation.
7. Desired cognitive distribution: remembering, understanding, application, analysis, evaluation, creation; or course-specific categories.
8. Difficulty distribution: easy / medium / hard, or expected percent correct.
9. Constraints: excluded topics, required topics, number of items, formatting, answer sheet needs, A/B卷 rules, anti-leakage requirements.
10. Intended score interpretation: criterion-referenced, norm-referenced, qualitative, diagnostic, or mixed.
11. Accessibility/fairness constraints: language level, accommodations, student background, and construct-irrelevant barriers.

If key inputs are missing and the task is still feasible, make conservative defaults and state them. For a typical closed-book university final exam, default to: 100 points, 90–120 minutes, broad coverage, moderate difficulty, criterion-referenced interpretation, and a mix of objective and application-oriented subjective items.

## Workflow

### Step 1: Establish the Assessment Claim and Score Interpretation

State what inference the exam should support. Examples:

- Students can accurately recall and explain core concepts.
- Students can distinguish related theories and developmental constructs.
- Students can apply course theories to educational or developmental cases.
- Students can analyze ambiguous real-world scenarios using course evidence.

Reject or revise items that do not contribute to this claim.

Specify whether the score will be interpreted as:

- Criterion-referenced: degree of mastery of defined course objectives.
- Norm-referenced: relative standing among students.
- Diagnostic: evidence about strengths, weaknesses, or misconceptions.
- Qualitative: descriptive performance categories or narrative feedback.

For classroom course exams, default to criterion-referenced interpretation unless the user explicitly requests relative grading. Do not mix achievement, effort, improvement, and attendance in a single exam score unless the grading policy explicitly defines that composite.

### Step 2: Build Educational Objectives and a Test Blueprint

Before generating items, create or infer educational objectives and then build a blueprint unless the user explicitly asks for only a small number of practice questions.

Objective-writing rules:

- Convert broad course aims into assessable outcomes.
- Prefer verbs that specify observable evidence: define, distinguish, explain, apply, analyze, evaluate, design.
- Classify objectives by cognitive domain by default; include affective or psychomotor objectives only when they are genuinely assessed.
- Avoid objectives that are too broad to sample fairly with the planned test length.

Blueprint dimensions:

- Content domain: chapters, lectures, themes, or learning objectives.
- Cognitive process: recall, understanding, application, analysis, evaluation.
- Item type: MCQ, short answer, essay, case, etc.
- Score weight and item count.
- Difficulty target.

Rules:

- Weight content by instructional emphasis: syllabus hours, lecture time, assignment emphasis, explicit exam focus, and course objectives.
- Avoid overrepresenting content merely because it is easy to turn into objective questions.
- Ensure that applied course objectives receive applied items, not only recall items.
- Present the blueprint before full exam generation when the user is designing a formal exam.

### Step 3: Define Item Specifications

For every generated or reviewed item, assign metadata:

- Item ID
- Content domain
- Learning objective
- Cognitive level
- Item type
- Expected difficulty
- Correct answer or scoring key
- Source basis: syllabus / lecture / textbook / user-provided material / teacher-added knowledge
- Quality status: draft / reviewed / needs revision / approved

Use `references/item_metadata_schema.md` if a structured metadata table is needed. Use `references/test_blueprint_template.md` when the user asks for a formal 双向细目表 or a reusable blueprint.

### Step 4: Generate Items

#### A. Multiple-Choice Questions

Prefer one-best-answer MCQs for formal exams.

Structure:

- Use 4 options when there are 3 plausible distractors; use 3 options only when a fourth plausible distractor would be artificial.
- The stem must pose a clear problem before the options are read.
- The item should test one concept, distinction, or application target.
- The correct answer must be defensibly best, not merely arguable.
- All distractors must be plausible for students with partial knowledge.
- Options should be parallel in length, specificity, and grammatical form.
- Vary the position of correct answers across the paper.

Prohibited or strongly discouraged formats:

- “以上都对 / 以上都不对 / all of the above / none of the above”
- Negative stems such as “以下哪项不是……” unless the construct truly requires exception recognition.
- Compound options such as “A 和 B 正确”.
- Overlapping options where one option logically contains another.
- Grammatical cues, length cues, absolute-term cues, and repeated-keyword cues.
- Trivial textbook sentence completion that tests surface memory only.

Distractor design for psychology / education courses:

Use at least two different distractor types per item:

- Concept confusion: mixes up related constructs, e.g., temperament vs. personality.
- Theory confusion: attributes a claim to the wrong theorist or school.
- Stage mismatch: uses a developmental stage but at the wrong age or with the wrong hallmark.
- Mechanism mismatch: states a true phenomenon but gives the wrong explanatory mechanism.
- Application error: applies a correct principle to an incompatible case.
- Causality error: treats correlation, maturation, or contextual association as direct causation.
- Overgeneralization: turns a probabilistic developmental tendency into an absolute rule.
- Surface-feature trap: focuses on an irrelevant but salient detail in the vignette.

For each MCQ, internally check:

1. Can the item be answered correctly without knowing the course content? If yes, revise.
2. Can the correct answer be guessed from length, wording, or option pattern? If yes, revise.
3. Are any distractors obviously irrelevant? If yes, replace.
4. Are two answers defensible? If yes, narrow the stem or revise options.

#### B. True/False, Matching, and Judgment Items

Use true/false items sparingly in formal exams because guessing probability is high and statements easily become ambiguous. Avoid vague quantifiers such as “often,” “generally,” or “may” unless the course explicitly taught the probabilistic claim. Require statements to be unambiguously true or false under course assumptions.

Use matching items only for homogeneous sets of terms, theorists, stages, methods, or examples. Keep the premise list and response list clear, provide more responses than premises when appropriate, and avoid heterogeneous matching sets that turn the item into a reading puzzle.

#### C. Fill-in and Definition Items

Use for key terminology only. Avoid obscure wording or low-value factual minutiae. For definitions, specify required elements and acceptable synonyms in the answer key.

#### D. Short-Answer Items

Use short-answer items for explanation, comparison, mechanism analysis, and concise educational implications.

Each item must include:

- Expected answer elements.
- Score allocation by element.
- Common partial-credit patterns.
- Maximum expected answer length if needed.

#### E. Essay, Case-Analysis, Performance, and Portfolio Items

Use case analysis to assess application and integration. Use performance assessment when the course target is authentic production, demonstration, classroom design, or applied decision-making. Use portfolios only when the purpose is longitudinal evidence, reflection, or growth documentation.

Case design rules:

- Use realistic but fictional scenarios unless the user requests real cases.
- Include sufficient facts to support analysis, but avoid irrelevant narrative inflation.
- Require students to identify relevant concepts, justify application, and propose reasonable implications.
- Avoid cases where the intended answer depends on information not given in the scenario or not taught in the course.

Rubric design:

- Separate concept identification, theoretical explanation, case evidence, reasoning quality, and practical implication.
- Use analytic rubrics for grading consistency.
- Define full-credit, partial-credit, and no-credit criteria.
- For extended-response tasks, create model answers before administration.
- For performance tasks, specify task instructions, performance criteria, evidence to be submitted, rating scale, and rater-error controls.
- For portfolios, specify required artifacts, selection rules, reflection requirements, scoring criteria, and revision policy.

### Step 5: Quality Assurance, Reliability, Validity, and Fairness Review

Run the checks in `references/quality_checklists.md` before finalizing.

Minimum QA gates:

1. Alignment check: every item maps to a course objective or key content domain.
2. Coverage check: item distribution matches the blueprint.
3. Cognitive-level check: the exam includes enough applied and analytic items for the course goal.
4. Single-answer check: objective items have one defensibly best answer.
5. Distractor-function check: distractors are plausible and diagnostically informative.
6. Difficulty check: difficulty comes from reasoning, discrimination, and transfer—not trick wording.
7. Fairness check: no item depends on irrelevant cultural, linguistic, or specialized background knowledge.
8. Redundancy check: no two items test exactly the same fact unless deliberate spiraling is intended.
9. Reading-load check: reading burden is proportionate to the construct being assessed.
10. Scoring check: subjective items have explicit scoring rubrics.
11. Reliability safeguard: important constructs are sampled by enough items or scored with robust rubrics.
12. Validity-evidence check: the exam has plausible content evidence and response-process plausibility for the intended use.
13. Accommodation check: item demands do not unintentionally penalize disability, language background, or irrelevant cultural knowledge.

When reviewing user-provided items, report issues as:

- Blocking: must revise before use.
- Major: likely reduces validity, fairness, or scoring reliability.
- Minor: wording or formatting improvement.

### Step 6: Output Contract and Administration Notes

For formal exam construction, provide the following sections:

1. Assumptions and constraints.
2. Test blueprint / 双向细目表.
3. Student-facing exam paper.
4. Answer key.
5. Scoring rubric.
6. Item metadata table.
7. Quality-review notes.
8. Administration and scoring notes.
9. Interpretation cautions: what the score can and cannot support.

For item revision tasks, provide:

1. Diagnosed problem.
2. Revised item.
3. Correct answer.
4. Why each distractor works or fails.
5. Recommended difficulty and cognitive level.

### Step 7: A/B Paper Generation

When creating A/B papers:

- Keep content domains, cognitive levels, total score, and difficulty distribution equivalent.
- Avoid merely reordering options if leakage risk is high.
- Use parallel but not identical scenarios.
- Maintain comparable reading load and rubric structure.
- Provide a mapping table between A and B items.

### Step 8: Post-Exam Analysis and Revision Loop

If student response data are provided, compute or request. Use `scripts/analyze_items.py` for simple objective-item analysis when the data are in CSV format:

```bash
python scripts/analyze_items.py --responses responses.csv --key answer_key.csv --out item_analysis.csv
```

Core outputs:

- Item difficulty: proportion correct.
- Item discrimination: corrected item-total correlation or high-low group difference.
- Distractor selection frequencies.
- Blank / nonresponse rate.
- Items to retain, revise, discard, rescore, or discuss in class.

If sample size is small, interpret cautiously and prioritize qualitative evidence from distractor patterns and student comments. Never describe a teacher-made exam as psychometrically validated from a single small class.

## Output Style

Use formal, concise academic Chinese by default. For student-facing materials, use clear and unambiguous language. Avoid meta-commentary about AI. Avoid saying that the generated exam is psychometrically validated unless adequate empirical response data and expert review have been analyzed.

## Supporting References in This Skill

- `references/measurement_assessment_additions.md`: reliability, validity evidence, score interpretation, item analysis, grading, accommodations, and fairness.
- `references/test_blueprint_template.md`: reusable blueprint / 双向细目表 template.
- `references/fairness_bias_review.md`: construct-irrelevant barriers, accommodations, and bias review.
- `references/post_exam_analysis_guide.md`: item analysis interpretation and revision rules.
- `references/quality_checklists.md`: pre-administration quality gates.
- `scripts/validate_mcq.py`: structural MCQ warning checker.
- `scripts/analyze_items.py`: simple objective-item analysis from response CSV and answer key CSV.

## Human Review Requirement

For summative, high-stakes, or official examinations, always mark the output as a draft requiring instructor review. The instructor must verify coverage, factual accuracy, fairness, answer uniqueness, and scoring standards before administration.
