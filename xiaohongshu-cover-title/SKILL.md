---
name: xiaohongshu-cover-title
description: Generate Xiaohongshu cover copy, post titles, cover composition plans, and real reference-case breakdowns from a spoken script, storyline, topic idea, rough outline, or content draft. Use when the user asks for Xiaohongshu title ideas, cover text, thumbnail/cover layout, real viral-note references, visible like-count examples, eye-catching but authentic hooks, or packaging content around their personal creator tone.
---

# Xiaohongshu Cover Title

## Overview

Turn the user's spoken script, storyline, topic idea, or rough outline into Xiaohongshu-ready cover and title options. Default to the user's personal tone: a post-95 male creator, working-person daily life, Hangzhou city life, weekend self-rescue, authentic vlogs, and light emotional resonance.

## Default Output

Produce 3-5 selected options unless the user asks for another count. Mark the strongest 3 as `Top 1`, `Top 2`, and `Top 3`.

Each option must include:

- `封面主文案`: short, stop-scrolling text.
- `封面副文案`: one supporting line that adds scene, emotion, or specificity.
- `小红书标题`: a publishable title.
- `整体构图样式`: a directly actionable cover composition.
- `适用理由`: state whether it is better for clicks, comments, saves, profile retention, or follows.

Keep the default style authentic but hooked: no fake conflict, no exaggerated clickbait, no forced trend-chasing. Prefer `场景 + 情绪 + 结果感`.

## Real Reference Cases

By default, look for 3 real Xiaohongshu reference cases before or while packaging the user's content.

Use this source priority:

1. Xiaohongshu in-site search or visible note pages.
2. Public search results that open to a verifiable Xiaohongshu page.
3. User-provided Xiaohongshu links.

For each real reference case, record:

- `参考标题`: the visible title.
- `可见点赞数`: the visible like count. If unavailable, write `点赞数未公开可见`.
- `链接或来源`: the page URL or a clear source description.
- `封面构图特征`: what can be observed about the cover layout.
- `可借鉴点`: the title, cover, or interaction pattern worth adapting.

Do not invent like counts, comments, saves, publication dates, or engagement claims. Do not label generated examples as real cases. If Xiaohongshu login walls, anti-bot limits, or search-result gaps prevent verification, state the limitation and base recommendations only on verified visible information.

## Cover Style

Default to a `生活感杂志` visual style:

- Use real photo/video frames as the base.
- Keep the image clean, personal, and memorable.
- Prioritize frames where `person + scene + emotion` are all visible.
- Use large readable Chinese cover text, but keep it tasteful.
- Avoid overdesigned sales-poster styling unless the user explicitly asks.

For every cover composition, specify:

- What kind of frame to choose.
- Whether the person should be left, center, right, foreground, side profile, back view, or small in the environment.
- Where to place the main and secondary text.
- Main/subtitle size relationship.
- Background treatment: negative space, soft mask, color block, outline, shadow, or blur.
- The best key frame to screenshot.

## Input Handling

If the user provides a full spoken script:

1. Extract the core emotion, turning point, concrete scene, and strongest visual frame.
2. Avoid summarizing the script mechanically.
3. Package the content around the most clickable and authentic viewer promise.
4. Search for reference cases using keywords derived from the script's topic, scene, and audience.

If the user provides a storyline:

1. Decide whether the strongest hook is character, place, conflict, emotion, or outcome.
2. Search for reference cases in the nearest comparable content category.
3. Generate cover/title options around the strongest hook.

If the user gives only one sentence or a loose idea:

1. Infer the likely audience and emotional angle.
2. Fill in a practical Xiaohongshu framing without inventing false facts.
3. Use 2-3 search keyword sets if needed to find comparable real notes.

If the topic fits a current platform trend:

1. Lightly incorporate relevant trend/search terms.
2. Do not change the user's persona or make the content feel unlike them.

## Writing Patterns

Prefer these title shapes:

- `连续上班后，我用半天把自己救回来了`
- `一个人在杭州，也能把周末过舒服`
- `95后打工人低成本周末：花很少的钱回血`
- `下班后去这里走一圈，感觉人又活了`
- `不是精致生活，是适合我的生活`

Prefer these cover text shapes:

- `周末自救`
- `一个人回血`
- `杭州半日逃离`
- `下班后的人生`
- `低成本快乐`
- `把自己哄好`

Use search-friendly words when natural: `杭州`, `打工人`, `周末`, `一个人`, `下班后`, `通勤`, `旅行`, `低成本`, `出租屋`, `618`, `值不值`.

## Quality Bar

Before answering, check that:

- The options sound like the user's account, not a generic marketing account.
- The cover text can fit on a mobile Xiaohongshu cover.
- Each composition can be executed from ordinary vlog footage.
- The real reference cases are visibly verifiable, or limitations are explicitly stated.
- Any missing like count is marked as `点赞数未公开可见`.
- No option overpromises something the content does not contain.

## Example Response Shape

When the user provides content, answer in Chinese using this compact structure:

```markdown
我会把这条内容包装成「核心情绪/主题」。以下方案参考了可见的真实案例；无法验证的数据会明确标注。

## 真实参考案例

### 案例 1
- 参考标题：
- 可见点赞数：
- 链接或来源：
- 封面构图特征：
- 可借鉴点：

## Top 方案

### Top 1
- 封面主文案：
- 封面副文案：
- 小红书标题：
- 整体构图样式：
- 适用理由：

### Top 2
- 封面主文案：
- 封面副文案：
- 小红书标题：
- 整体构图样式：
- 适用理由：

## 备选方案

### 4
- 封面主文案：
- 封面副文案：
- 小红书标题：
- 整体构图样式：
- 适用理由：
```

If the user asks for a rewrite, add a short `口播优化建议` section after the title options. Otherwise, do not rewrite the full spoken script by default.
