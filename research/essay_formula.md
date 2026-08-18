Yes. After looking across current guidance from **MIT, Yale, Harvard, Stanford, Princeton, and Johns Hopkins**, plus research on writing assessment, rater reliability, socioeconomic bias in admissions essays, automated essay scoring, and literary-personal-essay editing, I think this can be formalized surprisingly well.

The key is **not** to model “great essay” as one scalar aesthetic property. A college essay is simultaneously:

\[
\text{writing artifact} + \text{evidence about a person} + \text{information added to an application}
\]

That third term is especially important and is missing from most essay rubrics.

## 1. The strongest expert consensus

MIT explicitly tells applicants that its essays are **not a writing test** and emphasizes honesty, openness, authenticity, and connection. Yale's admissions officers emphasize showing rather than merely telling, reflection, natural personal voice, and simplicity rather than elaborate vocabulary or syntax. Stanford says the essays should reveal the applicant in their own words and help the office understand them as a future friend, roommate, and classmate. Princeton simultaneously emphasizes one's own voice and one's best writing. Harvard tells applicants not to chase an exotic topic; the purpose is to share something they care about and illuminate character and personal qualities. 

So the intersection looks approximately like:

> **Great college essay ≠ impressive story.**  
> **Great college essay ≈ distinctive person + meaningful reflection + credible evidence + authentic voice + effective writing.**

And the official Johns Hopkins examples provide a fascinating empirical sanity check. Essays their admissions committee selected as “Essays That Worked” revolve around things as ordinary or niche as **solitaire with a grandmother, potatoes, a robot, a dog, crochet, and fantasy worldbuilding**. The committee comments repeatedly praise what those subjects reveal about accountability, curiosity, humility, compassion, growth, worldview, interdisciplinary thinking, and likely campus contribution. 

That gives us an important result:

\[
\boxed{\text{Topic prestige} \approx 0}
\]

while

\[
\boxed{\text{Interpretation of topic} \gg \text{topic itself}}
\]

Harvard similarly says a topic does not need to be exotic to be compelling, and Yale explicitly warns against thinking there are particular “winning” topics. 

---

# 2. My proposed **EssayEval v1.0**

I would represent an admissions essay as an 8-dimensional vector:

\[
E=[R,S,V,C,D,N,M,T]
\]

where every variable is scored 0–5.

| Variable | Meaning | Weight | The central question |
|---|---|---:|---|
| **R** | Reflection / insight | **20%** | Does the writer discover or understand something meaningful? |
| **S** | Self-revelation | **18%** | Do I know this person substantially better afterward? |
| **V** | Voice / authenticity | **15%** | Does this sound unmistakably like an individual human being? |
| **C** | Concrete evidence / specificity | **12%** | Are claims about the self demonstrated rather than merely asserted? |
| **D** | Distinctive perspective | **10%** | Is the *way this person sees the world* non-interchangeable? |
| **N** | Narrative / structural coherence | **10%** | Does the piece have focus, progression, pacing, and an earned ending? |
| **M** | Marginal application value | **10%** | Does it add information not already obvious elsewhere? |
| **T** | Technical writing control | **5%** | Is the prose clear, precise, controlled, and sufficiently polished? |

These are **my proposed weights**, not any university's disclosed scoring rubric.

The analytic score becomes:

\[
A(E)=20R/5+18S/5+15V/5+12C/5+10D/5+10N/5+10M/5+5T/5
\]

so that:

\[
A(E)\in[0,100]
\]

The striking choice here is **only 5% for grammar/mechanics/technical polish**. That is deliberate. Princeton does care about strong writing, and general writing assessment rightly values organization, precision, syntax, and mechanics; ETS's highest analytical-writing category emphasizes insightful analysis, compelling support, focus, organization, precise language, sentence variety, and control of conventions. But MIT and Yale make clear that an admissions essay's main purpose is not to demonstrate linguistic virtuosity. 

Technical weakness can ruin communication, but technical brilliance cannot rescue an essay that tells me nothing meaningful about its author.

---

# 3. The deeper mathematical model: **information gain**

This is the part I think an information theorist would find most interesting.

Suppose:

- \(A\) = everything in the application **before** reading the essay.
- \(E\) = essay.
- \(T\) = latent understanding of the applicant: values, temperament, curiosity, motivation, maturity, agency, generosity, intellectual style, etc.

Before reading the essay, the reader has:

\[
P(T|A)
\]

After reading:

\[
P(T|A,E)
\]

Then one conceptual measure of essay value is:

\[
IG(E|A)
=
H(T|A)-H(T|A,E)
\]

where \(H\) represents uncertainty.

In plain English:

> **How much uncertainty about this person disappeared because I read these 650 words?**

This gives us one of the best diagnostics I know:

### The marginal-information question

> **“What do I know about this applicant now that I genuinely did not know before?”**

If the answer is:

> captain of orchestra, loves biology, volunteers, works hard

and all four things are already on the résumé, then:

\[
IG \rightarrow 0
\]

even if the prose is excellent.

Contrast that with Hopkins' *Building a Universe*. The writer deliberately chose a worldbuilding hobby that was missing from the résumé because it revealed curiosity and interdisciplinary thinking that the conventional application did not capture. The admissions committee then specifically highlighted what that hobby allowed them to infer about how he might learn at Hopkins. 

That is almost a textbook example of **high marginal information value**.

So I would actually model:

\[
\boxed{
EssayValue =
f(\text{Information Gain},
\text{Reflection},
\text{Credibility},
\text{Craft})
}
\]

rather than merely:

\[
EssayValue=f(\text{Writing Quality})
\]

---

# 4. Objective versus subjective components

There **are** things we can measure reasonably reproducibly.

| More objective / calibratable | More subjective, but still calibratable |
|---|---|
| Answers the prompt | Depth of insight |
| Follows length constraints | Authenticity of voice |
| Clear referents and chronology | Emotional resonance |
| Presence of concrete examples | Maturity |
| Logical progression | Charm / humor |
| Grammar that does not obscure meaning | Originality of perspective |
| Internal consistency | Memorability |
| Redundancy with résumé/application | Beauty/elegance |
| Evidence supporting stated qualities | Sense that “I know this person” |
| Excessive clichés/generalities | Likely contribution to a community |

The mistake is believing the right-hand column therefore cannot be assessed systematically.

It can.

It just requires **multiple judges, anchor examples, and calibration**.

---

# 5. I would use both analytic scoring **and gestalt**

Writing-assessment research distinguishes analytic scoring—breaking writing into traits—from holistic scoring—judging the work as a whole. Research has found that the approaches provide different useful information, and multi-trait scoring can reduce some of the reliability problems associated with purely holistic judgments. Human graders also have measurable severity/leniency effects. 

So I would not trust the 8-variable formula alone.

Have the reviewer first make a **cold holistic judgment** before touching the rubric:

\[
H \in [0,100]
\]

Then calculate:

\[
Final=0.80A+0.20H
\]

But with an important exception:

\[
|A-H| > 12
\quad\Rightarrow\quad
\text{mandatory reconsideration}
\]

Don't blindly average.

A disagreement such as

\[
A=76,\ H=95
\]

may mean the rubric failed to capture something genuinely extraordinary.

And

\[
A=94,\ H=68
\]

may indicate an essay that mechanically checks every box but somehow feels artificial, calculated, bloodless, or forgettable.

That difference is itself **information**.

---

# 6. The actual reviewer algorithm I would use

1. **Cold read.** Give a gestalt 1–5 score without dissecting the essay. Immediately write: “This person seems ___, ___, ___.” If you cannot fill those blanks confidently, that is already evidence of weak self-revelation.

2. **Evidence extraction.** Highlight separately: concrete events, reflection, values revealed through behavior, change/growth, distinctive language, and future/community implications. A claimed trait without behavioral evidence gets little credit.

3. **Score the eight dimensions independently.** Require the reviewer to cite one or two textual pieces of evidence for every score above 3. This reduces hand-waving such as “it just feels profound.”

4. **Run counterfactual tests.** Use the **Name-Swap Test**: could this essay plausibly have been written by 10,000 applicants? The **Résumé-Deletion Test**: what information disappears if we remove the essay? The **Topic-Swap Test**: is the essay impressive because the experience is prestigious, or because the student's thinking is interesting? The **Voice Test**: would people who know the writer recognize this person? And the **Memory Test**: ten minutes later, what image, idea, or person remains in the reader's head?

5. **Perform the application-context pass.** Compare the essay with activities, recommendations, short answers, and academic interests. Reward complementarity and coherent reinforcement; penalize pointless repetition. Do **not** require everything to form a manufactured “brand.”

6. **Independent second review.** Reviewers do not see one another's scores first. If overall scores or key dimensions diverge substantially, use a third adjudicator rather than simply averaging.

7. **Anchor calibration.** Before scoring a batch, have all reviewers score several common anchor essays representing weak, average, strong, and exceptional responses. Official Hopkins essays and committee commentary are unusually useful positive anchors because we know *why* the admissions committee thought they worked. 

8. **For hundreds or thousands of essays, model the reviewer too.** Measure weighted kappa/ICC and rater severity. At sufficient scale I would use a Many-Facet Rasch-type model rather than assuming Reviewer A's “4” equals Reviewer B's “4.” Such models explicitly estimate the latent quality of the writing separately from rater severity. 

---

# 7. The Rasch/data-science version gets especially interesting

A simplified model would be:

\[
\log
\frac{P(Y_{er}=k)}
{P(Y_{er}=k-1)}
=
\theta_e-\rho_r-\tau_k
\]

where:

- \(\theta_e\) = latent quality of essay \(e\)
- \(\rho_r\) = severity of reviewer \(r\)
- \(\tau_k\) = threshold between rating categories.

This mirrors the logic used in Many-Facet Rasch approaches to human writing assessment, where rater severity is treated as an unwanted source of variance rather than pretending every grader behaves identically. 

For the highly subjective dimensions—especially **voice, insight, distinctiveness, memorability**—I would additionally collect pairwise judgments:

> Which essay exhibits greater genuine self-understanding: A or B?

Then fit a Bradley–Terry model:

\[
P(A>B)
=
\frac{e^{\theta_A}}
{e^{\theta_A}+e^{\theta_B}}
\]

Pairwise judgments could give us a latent ordering without requiring humans to know exactly what separates an 86 from an 88.

---

# 8. One extremely important fairness constraint

I would **not** build an essay grader that heavily rewards vocabulary level, sophisticated stylistic ornamentation, international travel, rare extracurricular experiences, or cultural references associated with privilege.

A Science Advances study analyzed **240,000 admissions essays from 60,000 University of California applicants** and found that essay content and style were strongly related to household income; in that dataset the relationship with income was stronger than the relationship between SAT scores and income. 

That has profound consequences for rubric design.

A sentence like:

> “During my summer research fellowship at CERN…”

cannot automatically score higher than:

> “Every Thursday I translated the electric bill for my mother…”

The quality function should evaluate:

\[
\text{meaning extracted from experience}
\]

not:

\[
\text{market price / prestige of experience}.
\]

It is another reason I would keep lexical and mechanical sophistication relatively low-weighted.

---

# 9. What changes when we mean “great essay” in general?

Here the formula changes.

ETS's writing framework emphasizes depth of analysis, development/support, focus, organization, precise language and control. Literary personal-essay editors emphasize narrative, something changing, and reflection or broader meaning. Creative Nonfiction's editor described the sweet spot as the balance between story and reflection/context. And in one notable *Best American Essays* volume, Jonathan Franzen explicitly made **risk** the central selection criterion. 

So I would define the general literary/analytical essay approximately as:

\[
Q_{\text{general}}
=
.25I+
.20D+
.15N+
.15V+
.10C+
.10O+
.05T
\]

with:

- \(I\) = insight / quality of thinking
- \(D\) = development / evidence
- \(N\) = structure
- \(V\) = voice
- \(C\) = concreteness
- \(O\) = originality/surprise/risk
- \(T\) = technical control.

But a **college personal essay substitutes one major objective**:

\[
\text{argument/evidence}
\rightarrow
\text{revelation of person}
\]

So:

\[
\boxed{
Q_{\text{college}}
\approx
\text{Great Writing}
+
\text{Great Self-Knowledge}
+
\text{Great Information About Applicant}
}
\]

And the last two should dominate.

---

# 10. My definition of a truly exceptional admissions essay

I think the best operational definition is this:

> **An exceptional college essay causes a reader to construct a vivid, differentiated, credible mental model of the applicant—and to understand not simply what happened to them, but how they perceive, interpret, learn from, and act upon the world. It accomplishes this through concrete evidence, reflection, distinctive voice, narrative control, and language that serves the meaning rather than advertising the writer.**

Or, in data-science shorthand:

\[
\boxed{
\text{Exceptional}
=
\frac{
\text{Personal Information Gain}
\times
\text{Depth of Reflection}
\times
\text{Authenticity}
\times
\text{Memorability}
}{
\text{Words}
}
}
\]

I actually like that last formulation a lot: **personal information gain per word**.

It explains why a 500-word essay about potatoes can outperform a 650-word essay about founding an NGO.

The potato is irrelevant.

**The mind examining the potato is the signal.**

And I would go one step further: if we want to build a serious essay-evaluation methodology, **we should not train it on “admitted vs. rejected.”** Admission is a contaminated label—it contains GPA, recommendations, institutional priorities, athletics, demographics/context, class composition and dozens of other factors. Instead, I would construct a benchmark of essays independently scored by 3–5 expert readers on these latent dimensions, include official essays with admissions-officer commentary as anchors, estimate rater effects, and derive a calibrated latent **Essay Quality Score**. That would be much closer to something a mathematician or measurement scientist would trust.

If you want, the logical next step is to turn this into a **full “College Essay Evaluation System v1.0”**—with exact 0–5 descriptions for every dimension, 100-point scoring, examples of what a 1/3/5 looks like, red flags, counterfactual tests, and separate models for **Harvard/MIT/Stanford/Yale/Princeton-style essays** versus the Common App personal statement.
