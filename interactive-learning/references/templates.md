# Interactive Learning Templates

## Short Diagnostic

In live tutoring mode, ask the most relevant question first, wait for the learner's answer, and use the remaining questions adaptively. Use the full list only when the learner requests a worksheet or asynchronous exercise.

1. What do you want to be able to do after learning this material?
2. What is your current familiarity: zero, rough idea, read once, or can explain parts?
3. Which parts feel confusing or most valuable?
4. What is the deadline and available daily time?
5. Do you want the output as a study plan, tutoring session, notes, quiz, or reusable skill?

## Source Skeleton

```markdown
# Source Skeleton

## Source
- Title:
- Author/speaker:
- Material type:
- Anchors used: line / page / timestamp / section

## Author's Original Order
| Anchor | Section | Main claim | Concepts | Evidence/examples | Notes |
|---|---|---|---|---|---|

## Concept Inventory
| Concept | Source anchor | Plain explanation | Prerequisites | Common misconception |
|---|---|---|---|---|

## Argument Map
| Claim | Supports | Depends on | Challenge question |
|---|---|---|---|
```

## Course Map

```markdown
# Personalized Course Map

## Learner Profile
- Goal:
- Current level:
- Constraints:
- Blind spots:

## Learner-First Order
| Unit | Why now | Source anchors | Outcome | Practice | Done when |
|---|---|---|---|---|---|
```

## Learning Unit

```markdown
# Unit N: <name>

## Outcome
After this unit, the learner can:

## Source Anchors
- 

## Start Here
Ask one prediction, comparison, or case question.

## Teach Through Questions
1. Prompt:
   - Hint 1:
   - Hint 2:
   - Explanation after attempt:
2. Prompt:
   - Hint 1:
   - Hint 2:
   - Explanation after attempt:

## Misconceptions
| Misconception | Diagnostic sign | Correction prompt |
|---|---|---|

## Transfer Check
Give a new example and ask the learner to apply the concept.
```

## Review Pack

```markdown
# Review Pack

## Active Recall
1.
2.
3.

## Application Tasks
1.
2.

## Memory Sheet
- Core idea:
- Key distinctions:
- Examples:
- Warning signs:

## Spaced Review
| When | Task |
|---|---|
| Tomorrow | |
| 3 days | |
| 7 days | |
```

## Agent Prompts

Use these when the environment supports parallel agents. Keep each task source-grounded.

### Skeleton Agent

Read the source and produce a source-grounded skeleton. Preserve anchors. Extract claims, concepts, definitions, examples, and assumptions. Do not summarize loosely.

### Misconception Agent

Read the source and infer likely learner misconceptions. For each misconception, provide a diagnostic question and a correction prompt.

### Course Designer Agent

Use the learner profile and source skeleton to reorder the material into learning units. Optimize for prerequisites, blind spots, and transfer.

### Socratic Tutor Agent

Turn one learning unit into an interactive tutoring script. Ask before explaining. Give hints before answers. End with a transfer check.
