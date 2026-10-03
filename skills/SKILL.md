---
name: gemini-gem-builder
description: >
  Guides university staff through building a reusable Gemini Gem from
  their own documents in three stages (extract, generate, test). Use when
  a grant writer, research development officer, academic or learning
  designer wants to turn proposals, reviewer feedback, funder calls,
  module handbooks, student feedback or assessment briefs into a
  specialist Gemini assistant. Covers data protection checks, extraction
  prompts, Gem instruction prompts, test prompts, refining, sharing, and
  when to use NotebookLM instead.
---

# University AI Assistant Skill
## Gemini Gem Builder for Academic and Professional Staff

---

### What This Skill Does

This skill helps you build a reusable Gemini Gem from your own
documents. It is designed for university staff who want to turn
their existing files — proposals, handbooks, feedback reports,
policy documents — into a specialist AI assistant they can return
to again and again.

The skill works in three stages that mirror the training session:

1. **Extract** — upload your documents and pull out what matters
2. **Generate** — turn that analysis into Gem instructions
3. **Test** — verify the Gem does what you need before saving it

---

### Who This Is For

This skill covers two main use cases. Use whichever matches your role.

**Grant Writers and Research Development Staff**
You have proposals, reviewer feedback, funder call documents, and
institutional boilerplate sitting in folders. This skill turns that
material into a Gem that knows your institutional language, spots
the weaknesses reviewers flag, and checks alignment with funder
priorities before you submit.

**Academic Staff and Learning Designers**
You have module handbooks, student feedback reports, assessment
briefs, and your own planning notes. This skill turns that material
into a Gem that knows your module, your students' recurring
difficulties, and your teaching approach — so you can draft
session plans, revise assessment briefs, and write student-facing
communications without starting from scratch each time.

---

### Before You Start

**What to gather:**

For grant writing, collect at least three of the following:
- One or two previous proposals (funded or unfunded, or both)
- Any reviewer feedback you have received
- Your institution's standard boilerplate document
- A current funder call document you are targeting
- A lessons learned or post-bid review note

For teaching and learning, collect at least three of the following:
- Your module handbook or course specification
- Student feedback or module evaluation report
- Your assessment brief
- Your own planning or reflection notes
- An annotated reading list or resource guide

**Data protection check before uploading:**

Run through the Stop / Pause & Check / Go framework before
uploading any document to Gemini.

- STOP: Do not upload documents containing identifiable student
  data, personal staff information, commercially sensitive data,
  or anything that would violate your institution's data
  protection policy.

- PAUSE AND CHECK: Documents containing aggregated or anonymised
  feedback data are generally safe but check your institution's
  AI use policy if unsure. Remove names from any document that
  contains individual performance information before uploading.

- GO: Module handbooks, assessment briefs, boilerplate
  institutional text, published funder call documents, and
  your own reflection notes are all low-risk and safe to upload.

If in doubt, speak to your Research Development Office or Digital
Education team before proceeding.

---

### Stage 1 — Extract: Upload Your Documents and Pull Out What Matters

Open Gemini (gemini.google.com) and sign in with your university
login. Click the attachment icon to upload your documents. You can
upload multiple files in one session.

Once uploaded, use the prompt that matches your use case.

---

**Prompt 1A — Grant Writing: Extract institutional language and patterns**

```
I have uploaded [number] documents relating to my grant writing
work at [your institution]. Please read all of them and give me
the following:

1. All standard institutional language I use consistently across
   proposals — for example, descriptions of our research
   environment, EDI statements, facilities, and data management
   policy. Present each as a labelled block of text I can copy.

2. The strongest writing in these documents — passages where the
   case for support, methodology, or impact statement is
   particularly clear and compelling. Pull out the best paragraph
   or section from each of these areas and explain briefly why
   it works.

3. The weakest sections — where a reviewer would likely push back,
   ask for more evidence, or mark down. Be specific about what is
   missing or unclear in each case.

4. The key phrases and framing language I use most often — grouped
   under: research significance, methodology, impact, team
   capability, and budget justification.

5. If I have uploaded any reviewer feedback: what are the
   recurring themes across the feedback, and are there patterns
   in what reviewers consistently flag?
```

---

**Prompt 1B — Teaching and Learning: Extract module patterns and insight**

```
I have uploaded [number] documents relating to my module
[module name] at [your institution]. Please read all of them
and give me the following:

1. The standard module description language I use consistently
   — learning outcomes, module overview, assessment criteria,
   and any standard policy text. Present each as a labelled
   block I can copy and reuse.

2. The three most significant gaps between what the module
   intends (as described in the handbook and assessment brief)
   and what students actually experienced (as shown in feedback
   and any reflection notes). Be specific and cite both
   documents.

3. The recurring student difficulties — which concepts, tasks,
   or assessments do students consistently struggle with, and
   what does the evidence suggest about why?

4. What has worked well and should be preserved — specific
   sessions, activities, or approaches that students respond
   to positively.

5. If I have uploaded my own reflection notes: what questions
   am I still trying to answer about this module, and what
   changes am I considering?
```

---

### Stage 2 — Generate: Turn the Analysis into Gem Instructions

Once Gemini has given you its analysis, use one of the following
prompts to turn it into Gem instructions. Do not start a new
conversation — continue in the same chat so Gemini has the
full context of what it has just read.

---

**Prompt 2A — Grant Writing: Generate Gem instructions**

```
Based on everything you have just read and analysed, write me
a set of instructions for a Gemini Gem that will act as my
grant writing assistant at [your institution].

The Gem should:
- Know our standard institutional language and be able to
  insert it appropriately in proposals
- Know the types of weaknesses that reviewers have flagged in
  our previous applications and challenge me on those points
  proactively before submission
- Be able to check a draft section against a funder call
  document and identify gaps in alignment
- Be direct and constructively critical — I need honest
  feedback, not reassurance

Write the instructions in second person, addressing the Gem
directly. Make them specific enough that the Gem produces
consistent, useful output without me having to repeat context
every time I use it.

End the instructions with a list of the five most useful
starter questions I could ask this Gem.
```

---

**Prompt 2B — Teaching and Learning: Generate Gem instructions**

```
Based on everything you have just read and analysed, write me
a set of instructions for a Gemini Gem that will act as my
module planning assistant for [module name] at [your
institution].

The Gem should:
- Know the module's structure, learning outcomes, and
  assessment design
- Know the recurring difficulties students face and factor
  these into any session or assessment design suggestions
- Be able to help me draft student-facing communications that
  are consistent with the module's tone and expectations
- Be able to suggest specific improvements to sessions,
  assessment briefs, or feedback approaches based on the
  patterns it knows about

Write the instructions in second person, addressing the Gem
directly. Make them specific to this module — not generic
teaching advice.

End the instructions with a list of the five most useful
starter questions I could ask this Gem.
```

---

### Stage 3 — Test: Check the Gem Before You Save It

After copying the instructions into Gem Manager and saving your
Gem, use the following prompts to test whether it is working
as intended. A Gem that produces generic or vague responses
needs its instructions refined — go back and add more specific
context or constraints.

---

**Test prompts for Grant Writing Gems:**

```
Here is my draft case for support section. Review it as a
panel reviewer would and tell me the two things most likely
to count against it.

[paste your text]
```

```
Here is the call document for the funding scheme I am
applying to. What key phrases or priorities from this
document are missing from my draft proposal?

[paste call document text]
```

```
Draft a 150-word research environment statement for our
next UKRI application using our standard institutional
language.
```

---

**Test prompts for Teaching and Learning Gems:**

```
I want to redesign the session where students first encounter
[topic that your feedback identified as difficult]. Suggest
a revised 2-hour session plan that addresses the specific
difficulty students have had with this topic.
```

```
Write a student-facing FAQ for [assessment name] that
answers the ten questions students are most likely to ask,
based on what you know about where students typically
get confused.
```

```
I am writing feedback for a student who has submitted a
[strong / weak] [assessment type]. Draft a paragraph of
formative feedback that is honest, specific, and points
toward what they should do differently next time.
```

---

### Refining Your Gem

If the test responses are too generic, go back to the Gem
instructions and add more specificity. Common improvements:

**Add a stronger persona.** Instead of "you are a grant writing
assistant," try "you are a research development professional with
ten years of experience in UKRI funding, who knows our
institutional strengths and the common mistakes our research
teams make."

**Add constraints.** Tell the Gem what it should not do — for
example, "do not produce generic advice that applies to any
university; always draw on the specific institutional context
and known patterns in my proposals."

**Add the institutional context directly.** Paste your
boilerplate institutional text or your standard module
description directly into the Gem instructions so the Gem
always has it available, without you needing to upload
documents each time.

**Set the tone explicitly.** Tell the Gem how direct to be —
for example, "be a critical friend. I do not need reassurance.
I need honest assessment of what is weak and what needs to
change."

---

### Using Your Gem Going Forward

Your Gem remembers its instructions across sessions, which
means you do not need to upload your documents or re-explain
your context every time you use it. Each conversation starts
with the Gem already knowing your institutional language,
your module, and your working patterns.

To get the most from it:

- Paste specific text when you want specific feedback
- Use it early in the drafting process, not just as a final
  check
- Treat its output as a first draft or a critical prompt,
  not a finished product — you remain the expert, author,
  and decision-maker
- Update the Gem instructions when your context changes
  significantly — a new module structure, a revised
  boilerplate, a new funder focus

---

### Sharing Your Gem With Colleagues

You can share your Gem instructions with colleagues by copying
the text from Gem Manager. They can paste the same instructions
into their own Gem and customise from there. This is
particularly useful for:

- Research teams who want a shared grant writing assistant
  anchored in the same institutional language
- Programme teams where multiple lecturers teach on the same
  module and want consistent student-facing communications
- Research development offices who want to give all
  investigators access to a pre-built funder alignment checker

Note: Gems do not share access to your documents. The
instructions travel; the uploaded files do not. If a
colleague needs the Gem to know specific documents, they
will need to upload those files themselves in their own
Gemini session.

---

### NotebookLM — When to Use It Instead

Your Gem is best for ongoing, repeated tasks where you want
a persistent assistant that knows your context.

NotebookLM (notebooklm.google.com) is best for deep,
one-time synthesis across a specific set of documents —
finding patterns across multiple proposals, cross-referencing
reviewer feedback against lessons learned, or generating a
structured briefing from a body of material you want to
interrogate in depth.

The two tools work well together:
- Use NotebookLM to find the patterns and generate the insight
- Use those insights to refine your Gem instructions
- Use your Gem for the ongoing day-to-day drafting and review

---

### Quick Reference — Which Prompt for Which Task

| Task | Tool | Prompt to Use |
|------|------|---------------|
| Extract boilerplate from uploaded documents | Gemini | Prompt 1A or 1B |
| Generate Gem instructions from analysis | Gemini | Prompt 2A or 2B |
| Test your new Gem | Gem | Test prompts above |
| Find patterns across multiple proposals | NotebookLM | Cross-reference prompt |
| Check what a funder is looking for | Gem | Funder alignment prompt |
| Draft a session plan for a difficult topic | Gem | Teaching test prompt |
| Generate a student FAQ from your brief | Gem or NotebookLM | FAQ prompt |
| Create an Audio Overview of your materials | NotebookLM | Use Studio panel |

---

### Data Protection Reminder

Always apply the Stop / Pause & Check / Go framework before
uploading any document. When in doubt, anonymise first or
check with your institution's data protection or digital
education team. Gemini for Education runs on enterprise-grade
data protection — your data is not used to train AI models —
but your institution's own policies about what can be shared
externally still apply.

---

*This skill was created as part of the Cardiff University /
University of East London Gemini for Education training
programme delivered by Happy2Host and Google for Education.
Adapt the prompts and instructions to your own institutional
context before use.*
