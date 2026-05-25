---
name: interactive-learning
description: Convert books, course transcripts, articles, papers, meeting notes, podcasts, or other static learning materials into a diagnosis-driven interactive learning system. Use when the user wants an AI-assisted reading method, "CC/Claude Code/Codex interactive learning", one-week book study, active recall, Socratic tutoring, personalized learning paths, book skeletons, course maps, or reusable study units from Markdown, TXT, DOCX, PDF text, notes, or transcripts.
---

# Interactive Learning

## Overview

Turn static material into a learnable system: diagnose the learner, build a source-grounded skeleton, reorder content around blind spots, and teach through Socratic questions instead of direct summaries.

Use this skill as a workflow. Keep answers source-grounded, line-referenced when possible, and optimized for retention and transfer.

## Workflow

1. **Prepare the source**
   - If the user provides `.md`, `.txt`, or `.docx`, optionally run `scripts/prepare_source.py` to produce normalized Markdown with line numbers.
   - If the source is a PDF, transcript, webpage, or video, first extract text with the best available local or browser workflow, then normalize it.
   - If the source is missing, ask for the file/text/link and offer to start with a diagnostic questionnaire.

2. **Diagnose the learner**
   - Ask 4-7 questions before building the final path.
   - Cover: learning goal, current familiarity, deadline, preferred output, real-world use case, confusing concepts, and desired difficulty.
   - If the user wants speed, use the short diagnostic in `references/templates.md`.

3. **Build the material skeleton**
   - Extract the author's structure, key claims, definitions, examples, evidence, and assumptions.
   - Preserve source anchors: section names, page numbers, timestamps, or generated line numbers.
   - Separate "what the author says" from "what the learner needs first".

4. **Switch into live tutoring mode**
   - Once the skeleton is ready, proactively ask the learner the first high-leverage question in chat.
   - Ask one focused question at a time unless the learner requests a worksheet or batch mode.
   - Base the next question on the learner's prior answer, using the source skeleton to challenge assumptions and reveal blind spots.
   - Do not hand the learner a list of questions as the main interaction when a conversational session is possible.

5. **Create a personalized course map**
   - Reorder the material by prerequisite logic and the learner's blind spots.
   - Produce 5-12 learning units.
   - For each unit include: goal, source anchors, core concepts, exercises, misconceptions, and completion check.

6. **Teach each unit interactively**
   - Start with a question, case, or prediction prompt.
   - Wait for the learner's answer before asking the next question in conversational mode.
   - After each answer, briefly identify the assumption or principle exposed, then ask a deeper question or give a source-grounded correction.
   - Give hints before answers. When the learner is wrong, ask from a different angle.
   - Use the minimum explanation needed, then test transfer with a new example.

7. **Consolidate**
   - End with an active-recall quiz, a one-page memory sheet, and next actions.
   - Track weak points and update the course map after each session.

## Output Standards

Default outputs:

- `learning_profile`: learner goal, current level, constraints, and blind spots.
- `source_skeleton`: source-grounded outline with anchors.
- `course_map`: reordered learning path.
- `learning_units`: interactive units with prompts, hints, checks, and source anchors.
- `review_pack`: recall questions, application tasks, and spaced review schedule.

Prefer Markdown tables for maps and compact numbered lists for units. Avoid long passive summaries. Make the learner do cognitive work.

## Interaction Rules

- Ask diagnostic questions before designing a full path unless the user explicitly asks for immediate processing.
- After a source skeleton already exists, initiate the learning conversation yourself; do not wait for the learner to select a question or fill a template.
- In live tutoring mode, present one primary question per turn and use later turns for adaptive follow-up.
- Convert each meaningful learner answer into a candidate personal standard or a tracked uncertainty before moving on.
- Ground every claim in the source when source material is available.
- Do not present a summary as learning. Convert claims into questions, exercises, and checks.
- Keep the author's order visible, then build a learner-first order separately.
- Use Socratic questioning: prompt, hint, deeper prompt, answer, transfer check.
- For difficult material, create four levels: intuition, mechanism, example, application.
- For multiple sources, create one shared concept map before making units.

## Resources

- Read `references/templates.md` when creating diagnostics, skeletons, course maps, learning units, review packs, or agent prompts.
- Run `scripts/prepare_source.py <input> --out <output.md>` to normalize `.md`, `.txt`, or `.docx` into line-numbered Markdown.
