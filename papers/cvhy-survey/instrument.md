---
title: "Valuing Life and Health on One Scale: Study 1 Survey Instrument"
subtitle: "National stated-preference survey for the Common Value of a Healthy Year (CVHY) programme · Draft v0.1 for cognitive testing"
author:
  - Austin Henderson, University of Otago, Dunedin, New Zealand
date: "November 2026"
---

**Purpose of this document.** This is the complete draft questionnaire and design specification for Study 1 of the CVHY programme. It is written for the survey programmer, the ethics committee and the cognitive-testing team. Text in boxes marked **Screen** is shown to respondents. Text in *italics* is programming or interviewer instruction.

**Licensing note.** The EQ-5D-5L descriptive system, the EQ VAS and the EQ-VT composite time trade-off protocol are proprietary. Their exact wording must be licensed from the EuroQol Research Foundation before fielding. Where they appear below, the wording is a placeholder marked **[EQ licensed text]**.

**Link to theory.** Each module identifies one or more factors in the decomposition theorem of the companion theory paper:

$$G = \tfrac{\text{DQALE}}{\text{LE}} \times N \times \sigma \times \pi \times M \times \lambda_h .$$

The identification map is in Section 12.

---

# 1 Design summary

| Element | Specification |
|---|---|
| Population | NZ residents aged 18–79, online panel with quotas on age × sex, region and education; probability-based top-up sample for weighting checks |
| Target sample | 3,000 completes: general sample 1,800; Māori boost 600; Pasifika boost 600 |
| Median length | 30 minutes (target ≤ 35 minutes at the 90th percentile) |
| Languages | English; te reo Māori version offered (translation and back-translation, Module 0 onward) |
| Incentive | Panel points equivalent to NZ\$10 |
| Between-subject factors | Context (5) × payment vehicle (2) × risk scope range (2) = 20 cells, about 150 respondents each |
| Within-subject tasks | Module A: 8 mortality-risk choice tasks + 2 checks. Module B: 6 morbidity choice tasks + 1 check. Module C: 6 composite TTO states + 1 practice |
| Order | 0 Consent → 1 Screening → 2 Risk training → 3 Module A → 4 Perception → 5 Module B → 6 Module C → 7 Own health and expectations → 8 Economic background → 9 Debrief |
| Order randomisation | Modules A and B swapped for a random half (order effects test). Module C always follows both choice modules |

**Cell allocation (per 3,000).**

| Context ↓ / arm → | Private payment, low scope | Private, high scope | Tax, low scope | Tax, high scope |
|---|---:|---:|---:|---:|
| Road crashes | 150 | 150 | 150 | 150 |
| Air pollution | 150 | 150 | 150 | 150 |
| Workplace accidents | 150 | 150 | 150 | 150 |
| Bowel cancer | 150 | 150 | 150 | 150 |
| Hospital care | 150 | 150 | 150 | 150 |

Allocation uses block randomisation within quota strata. Boost samples are allocated in the same proportions.

---

# 2 Module 0 · Participant information and consent

> **Screen 0.1 — About this study**
> This survey is run by researchers at the University of Otago. It asks how you would trade money against risks to your life and health. Your answers will help government agencies in Aotearoa New Zealand value health more consistently when they decide what to fund.
>
> The survey takes about 30 minutes. Some questions ask you to imagine being in poor health or facing a risk of death. If any question is upsetting, you can skip it or stop at any time. Support contacts are listed at the end.
>
> Your answers are anonymous. We do not collect your name or contact details. Data are stored securely in New Zealand. The project follows the principles of Māori data sovereignty, and data about Māori participants will be governed with Māori partners.
>
> This project has been reviewed and approved by the University of Otago Human Ethics Committee (reference **[to be inserted]**).

> **Screen 0.2 — Consent**
> ☐ I have read the information above and agree to take part.
> ☐ I do not want to take part. *(→ end)*

---

# 3 Module 1 · Screening and quotas

1. **Age.** What is your age in years? *(numeric 18–79; outside range → end)*
2. **Sex.** *(Stats NZ standard: Male / Female / Another gender)*
3. **Ethnicity.** Which ethnic group or groups do you belong to? Select all that apply. *(Stats NZ standard ethnicity question, Census 2023 wording)*
4. **Region.** *(16 regions)*
5. **Highest qualification.** *(Stats NZ standard categories)*
6. **Household.** How many people live in your household? How many are under 18?

*Quota check after Q1–Q5. Full quotas → polite exit.*

---

# 4 Module 2 · Understanding small risks

Risk communication follows established visual-aid practice for stated-preference studies of mortality risk. Each respondent learns to read a 100,000-square grid and is tested on it before any valuation task.

> **Screen 2.1**
> In this survey we describe risks as "out of 100,000 people like you". The grid below has 100,000 small squares. Each square is one person. The coloured squares are people who die from a particular cause over the next 10 years.

*Show a 100,000-cell grid (500 × 200) with 70 cells coloured, labelled "70 out of 100,000".*

**Practice questions** (feedback shown after each answer):

- **2.2.** Person A has a risk of 20 in 100,000. Person B has a risk of 40 in 100,000. Who is more likely to die? *(A / B / Same)*
- **2.3.** A safety programme lowers your risk from 70 to 60 in 100,000. How many fewer people out of 100,000 like you would die? *(numeric; correct = 10)*
- **2.4.** Which is the larger risk reduction: from 70 to 60, or from 70 to 50, in 100,000? *(First / Second / Same)*

**Numeracy** (Lipkus three-item short form, adapted to "out of 1,000"):

- **2.5–2.7.** *(standard items)*

*Respondents who answer two or more of Q2.2–2.4 incorrectly see a second explanation screen and one repeat item. Final comprehension score is recorded; the pre-registered exclusion rule appears in Section 11.*

---

# 5 Module 3 · Mortality risk choices (Module A)

## 5.1 Context scripts (one per respondent)

*Show the script for the assigned context, with a context-specific illustration and the grid at the baseline risk.*

> **Road crashes.** Each year about 300–350 people die on New Zealand roads. Your own risk depends on how much and where you travel. Out of 100,000 people like you, about **70** will die in a road crash over the next 10 years.
>
> **Air pollution.** Air pollution from vehicles and home heating contributes to deaths from heart and lung disease. Out of 100,000 people like you, about **70** will die early because of air pollution over the next 10 years.
>
> **Workplace accidents.** Out of 100,000 people like you, about **70** will die in an accident at work or while travelling for work over the next 10 years.
>
> **Bowel cancer.** Out of 100,000 people like you, about **70** will die from bowel cancer over the next 10 years.
>
> **Hospital care.** When people are treated in hospital, some die from complications that better care could prevent. Out of 100,000 people like you, about **70** will die from such complications over the next 10 years.

*Design note.* The baseline risk is held at 70 in 100,000 across contexts so that the context, not the baseline, varies. The script tells respondents that risks are illustrative of "people like you" and need not match national statistics exactly. Real national figures appear on the debrief screen.

## 5.2 Payment vehicle (one per respondent)

> **Private payment.** Imagine you could pay for a programme that lowers this risk for you personally, for example a [context-specific: vehicle safety package / home air filter and cleaner heating / workplace safety service / screening and follow-up programme / hospital safety programme]. You would pay every year for 10 years.
>
> **Taxation.** Imagine the government could run a programme that lowers this risk for everyone, including you. It would be paid for by increasing your household's taxes every year for 10 years.

## 5.3 Consequentiality and cheap talk

> Results from this survey will be shared with the Treasury, the Ministry of Health and the Ministry of Transport. They may influence how much is spent on programmes like these. Please answer as if the payments were real.
>
> In surveys, people often say they would pay more than they really would. When you choose, please think about your household budget and the other things you need to spend money on.

## 5.4 Attributes and levels

| Attribute | Levels | Notes |
|---|---|---|
| Risk reduction over 10 years (per 100,000) | **Low-scope arm:** 5, 10, 20 · **High-scope arm:** 20, 40, 80 | 20 appears in both arms for the external scope test (Prop. 5) |
| When the reduction starts | Now; in 10 years | Shown only for air pollution and bowel cancer, where latency is realistic; fixed at "now" for other contexts |
| Annual cost for 10 years | NZ\$25, 50, 100, 200, 400, 800 | Same levels in both vehicles |
| Who else benefits | Only you (private); everyone in NZ (tax) | Fixed by vehicle; restated on every task |

## 5.5 Choice task format

> **Screen 3.x** — Which would you choose?
>
> | | Programme A | Programme B | No programme |
> |---|---|---|---|
> | Deaths out of 100,000 like you, next 10 years | 70 → **60** | 70 → **50** | **70** |
> | Reduction starts | now | now | — |
> | Cost to your household each year for 10 years | **\$100** | **\$400** | **\$0** |
>
> ○ Programme A ○ Programme B ○ No programme

*Each task shows grids for each option, with the reduction highlighted. Two alternatives plus an opt-out. Eight design tasks are in random order, with a dominance check inserted at position 4 (one programme cheaper and larger) and a repeat of task 2 at position 9.*

## 5.6 Experimental design

- **Design.** Bayesian D-efficient design with priors from the pilot (Section 10), generated separately for latency and non-latency contexts.
- **Blocks.** 48 choice situations in 6 blocks of 8.
- **Constraints.** No dominated pairs apart from the planned check. Cost and risk reduction are not perfectly correlated within a task.
- **Target efficiency.** D-error at or below the pilot-based benchmark; level balance within ±5%.

---

# 6 Module 4 · Risk perception and anxiety

These items identify the two components of the context premium (Proposition 4): misperception ($\omega_k$) and anxiety ($\alpha_k$).

1. **4.1 Perceived own risk.** Out of 100,000 people like you, how many do *you* think will die from [context] over the next 10 years? *(numeric, with grid slider)*
2. **4.2 Perceived effect.** If a programme reduced the number from 70 to 60, how much do you think it would really change *your own* chance of dying? *(Much less than the figure / A bit less / About right / A bit more / Much more)*
3. **4.3–4.7 Psychometric ratings** (1–7 scales): How much do you *dread* this kind of death? How much *control* do you have over this risk? Is the risk *voluntary*? How *familiar* is it? How *immediate* is death once it happens?
4. **4.8 Worry frequency.** In the past month, how often have you worried about dying from [context]? *(Never / Once or twice / Weekly / Most days)*
5. **4.9 Worry intensity.** When you do think about it, how anxious does it make you? *(0–10)*
6. **4.10 Exposure.** *(context-specific)*:
   - *Road:* hours a week in a car.
   - *Air:* main home heating type.
   - *Work:* industry and occupation.
   - *Cancer:* screening history.
   - *Hospital:* hospital stays in the past 5 years.

---

# 7 Module 5 · Health improvement choices (Module B)

## 7.1 Script

> In the next questions, imagine you have a health problem that lowers your quality of life but does not shorten your life. A treatment or programme could improve your health for some years. You would pay for it each year while it works.

## 7.2 Attributes and levels

| Attribute | Levels |
|---|---|
| Your health now | Four states described with the five EQ-5D-5L dimensions **[EQ licensed text]**. The design uses states 21232, 32323, 23242 and 44343, which span mild to severe |
| Your health with the programme | One to three levels better on one or more dimensions, generated by the design; never worse than "now" |
| How long the improvement lasts | 1, 5 or 10 years |
| Annual cost while it works | NZ\$25, 50, 100, 200, 400, 800 |
| Payment vehicle | As assigned in Module A (private or tax) |

## 7.3 Task format

There are six tasks with two programmes plus an opt-out, and one dominance check. Health states are shown as five-row profiles with the changed dimensions highlighted.

## 7.4 Design

- Bayesian D-efficient design.
- 36 situations in 6 blocks of 6.
- Priors on health-state coefficients come from the NZ EQ-5D-5L value set if one is available at the time; otherwise from a published value set from a comparable country.

---

# 8 Module 6 · Valuing health states (Module C)

Composite time trade-off following the EQ-VT protocol **[EQ licensed text and procedures]**. It is self-completed online with an animated aid, after the online feasibility work for EQ-VT-style tasks.

- **Practice.** One practice state ("being in a wheelchair") is valued with full feedback.
- **States.** Six states: the four Module B "now" states plus 11111 (to check that it is valued at 1) and 55555.
- **Procedure.** Conventional TTO over 10 years. Lead-time TTO (10 + 10 years) applies when a respondent prefers immediate death.
- **Iteration.** Iterative bisection with steps of 0.5 years. The respondent confirms the final indifference point.
- **Checks.**
  - 55555 valued below 11111 (logical consistency).
  - A response time under 3 seconds per state is flagged.

*Output for analysis.* Each respondent's own quality weights $Q_i(h)$ for the Module B states. These are used to compute personal DQALE and QALY gains (Section 12).

---

# 9 Module 7 · Own health, survival expectations and economic background

## 9.1 Own health

- **7.1** EQ-5D-5L, own health today **[EQ licensed text]**.
- **7.2** EQ VAS **[EQ licensed text]**.
- **7.3** Long-term conditions *(checklist)*.

## 9.2 Survival expectations

These items give the subjective survival function $S_i(t)$, using a Health and Retirement Study-style format.

- **7.4** What do you think is the chance, from 0 to 100, that you will live to age **75**? *(asked if age < 70)*
- **7.5** … to age **85**? *(asked if age < 80)*
- **7.6** … to age **95**?

*The three answers are combined with life tables in a Gompertz model to obtain individual survival curves. Focal answers (0, 50, 100) are flagged for robustness analysis.*

## 9.3 Economic background

- **7.7** Household income before tax *(Stats NZ bands)*.
- **7.8** Roughly how much does your household spend in a typical month, excluding rent or mortgage? *(bands)* (for $\bar c$)
- **7.9** Household net wealth *(bands; prefer not to say)*.
- **7.10** Employment status; hours worked.
- **7.11** Private health insurance *(yes/no)*.
- **7.12** Trust in government to spend money well *(0–10)*.
- **7.13** Political orientation *(left–right 0–10; optional)*.

---

# 10 Module 8 · Debriefing

1. **8.1 Certainty.** How sure are you that you would actually pay the amounts you chose? *(0–10)*
2. **8.2 Consequentiality.** How likely do you think it is that results of this survey will affect government decisions? *(0–10)*
3. **8.3 Protest screening.** *(Asked if "No programme" was chosen in every Module A task.)* Which statement best describes why you chose no programme every time?
   - I can't afford it.
   - The risk reduction is not worth that much to me.
   - The government should pay without extra tax.
   - I don't believe the programme would work.
   - It is wrong to put a price on life.
   - Other.
4. **8.4 Understanding.** How easy or difficult were the risk questions? *(1–5)*
5. **8.5 Attention.** One instructed-response item, embedded in Module 7.
6. **8.6 Open comments.**

> **Screen 8.7 — Thank you**
> Thank you for taking part. The risks in this survey were illustrative. National figures: [road deaths, air pollution-related deaths (HAPINZ 3.0), workplace fatalities, bowel cancer deaths; to be inserted with sources at fielding].
>
> If this survey raised concerns: Need to talk? Free call or text **1737**. Healthline **0800 611 116**. For questions about the study, contact the research team at **[email]**. To raise ethical concerns, contact the University of Otago Human Ethics Committee Administrator on **[phone/email]**.

---

# 11 Data quality and pre-registered exclusions

| Rule | Action |
|---|---|
| Failed the instructed-response attention item | Exclude |
| Completion time < one third of the median | Exclude |
| Failed both the Module A and Module B dominance checks | Exclude from choice models; keep for descriptive analysis |
| Two or more risk-comprehension errors after retraining | Keep; analyse separately as a robustness check |
| Protest zero (8.3 "government should pay" or "wrong to price life") | Exclude from WTP estimation; report prevalence by context and vehicle |
| Non-trading in all Module A tasks for non-protest reasons | Keep (valid zero WTP) |
| TTO: 55555 valued above 11111 | Exclude from Module C only |

All rules will be registered on OSF before fielding. Primary analyses use all non-excluded respondents, weighted to Census margins. Robustness analyses are unweighted and apply stricter rules.

---

# 12 Analysis map: from questions to theory

| Theoretical object | Questions | Estimator |
|---|---|---|
| Context VSL, $\text{VSL}_{k}$ | Module A (3.x), by cell | Mixed logit in WTP space; VSL = WTP ÷ risk reduction × 100,000 |
| Scope parameter $\theta$ and $M$ (Prop. 5) | Module A, external contrast at 20/100,000 between scope arms; internal range | WTP as $\beta \Delta p^\theta$ in the utility function; $M$ evaluated at policy-relevant $\Delta p_0$ |
| Personal DQALE | Module C weights, Module 7 survival, life tables | Individual Gompertz survival × own quality weights, discounted at 2% (sensitivity analyses at 0% and 3.5%) |
| $v^*$ and the test of Prop. 1(iii) | Modules A + B jointly with personal DQALE and QALY gains | Structural model: $\text{WTP}^A = \pi_k M v^* \Delta\text{DQALE}$, $\text{WTP}^B = v^* \Delta\text{QALY}$; test equality and age invariance (H1–H2) |
| $\sigma$ (state dependence) | Age and health interactions in the structural model | Bounded below by 1 (Prop. 2); estimated as the residual age gradient after controlling for $\pi$ and $M$ |
| $\omega_k$ (misperception) | Module 4.1–4.2 | Ratio of perceived to stated risk change; WTP regression on perception |
| $\alpha_k$ (anxiety) | Module 4.3–4.9; age gradient of $\pi_k$ | Prop. 4: $\pi_{k,a}-\omega_k \propto D_{a,T}/\text{VSL}^0_a$; worry items as instruments |
| Payment-vehicle effect (H5) | Vehicle arm | Main effect and interactions in Modules A and B |
| Subgroups (Māori, Pasifika, income) | Boost samples | Pre-specified heterogeneity; equity analysis |

---

# 13 Piloting plan

1. **Cognitive interviews (n ≈ 24).** Think-aloud interviews in Dunedin, Auckland and one rural area: eight with Māori participants (Māori interviewer), eight with Pasifika participants (Pasifika interviewer) and eight others. Focus areas:
   - understanding of the 100,000-person grid;
   - credibility of the payment vehicles;
   - acceptability of death and illness scenarios;
   - comprehension of the TTO.
2. **Soft launch (n ≈ 300).** Checks length, drop-out by screen, non-trading rates and data quality. Provides priors for the Bayesian efficient designs. Cost levels are revised if more than 60% or fewer than 15% choose the opt-out at the highest cost.
3. **Final design freeze and OSF registration**, before main fieldwork.

---

# 14 Ethical and cultural considerations

- **Distress.** Scenarios involving death and illness can be distressing. Mitigations:
  - neutral wording;
  - a skip option on every valuation screen;
  - support contacts on the opening and closing screens;
  - no questions about the deaths of family members.
- **Te Tiriti o Waitangi.** The project would be co-designed with Māori researchers. The Ngāi Tahu Research Consultation Committee would be consulted. Data about Māori participants would be governed under Māori data sovereignty principles (Te Mana Raraunga). Pasifika data would be handled in line with Pacific research guidelines. A te reo Māori version would be offered.
- **Equity in analysis.** Values estimated separately by income or ethnicity are for understanding, not for setting lower values for poorer or minority groups. The reporting standard uses a single population value of $v^*$.

---

*Version history: v0.1 (November 2026), drafted for the research team's review before cognitive testing.*
