---
title: "One Price for a Healthy Year: A Life-Cycle Framework and Empirical Programme for Valuing Health Consistently Across Government"
subtitle: "Research proposal and pre-analysis plan"
author:
  - Austin Henderson, University of Otago, Dunedin, New Zealand
date: "Draft for author revision · November 2026"
bibliography: references.bib
link-citations: true
---

**Target outlets.** Theory and decomposition: *Journal of Health Economics* or *Journal of Benefit-Cost Analysis*. Empirical valuation study: *Journal of Risk and Uncertainty* or *Health Economics*. Policy synthesis: *Applied Health Economics and Health Policy* or *Policy Quarterly* (New Zealand).

**Status.** This is a draft proposal for the author's development. Illustrative numbers use published NZ values and simple life-table approximations; all hypotheses would be pre-registered before data collection.

---

# Abstract

**Problem.** New Zealand's transport agency values a statistical life at NZ\$12.5 million. The Treasury's cost–benefit tool values a quality-adjusted life-year (QALY) at about NZ\$36,000, and the medicines agency works within a fixed budget with no published threshold. Spread over a 40-year-old's discounted, quality-adjusted remaining life, the road value implies about NZ\$516,000 per QALY, roughly 14 times the Treasury value. Inconsistencies of this size mean that money moved between agencies could buy substantially more health. Yet there is no agreed way to tell which part of the gap reflects legitimate differences between decisions and which part is error.

**Proposal.** We propose the **Common Value of a Healthy Year (CVHY)**: a single consumption-equivalent value per QALY, $v^*$, derived from life-cycle theory and estimated directly. It comes with two published sets of adjustments that every agency would apply transparently:

- context multipliers $\pi_k$ for risk types (for example dread or identified victims), retained only where they survive empirical and deliberative tests;
- sector shadow prices of public funds $\lambda_s$, which convert budget-constrained spending into consumption-equivalent welfare.

The framework shows that the observed gap factors exactly into four parts: life-table arithmetic, context premia, elicitation artefacts, and the shadow price of the health budget. Each part is estimable.

**Empirical programme.** Four linked studies would estimate each factor for New Zealand:

1. A national stated-preference survey (n ≈ 3,000) in which the same respondents value mortality-risk reductions across five contexts, morbidity improvements and health states. It includes scope tests and payment-vehicle variation.
2. Estimates of the marginal productivity of health and transport spending, using the population-based funding formula and revealed funding decisions.
3. Deliberative citizens' panels to judge which context premia should count.
4. A re-ranking of real NZ interventions under the unified rule.

**Contribution.** A theoretically grounded, empirically calibrated and publicly legitimated value of health that transport, health, environment and education agencies could share, with an explicit account of when they should still differ.

---

# 1 Motivation

Governments value lives and health in at least three incompatible ways.

- **Transport and environmental regulators** use a value of a statistical life (VSL): the rate at which people trade money for small reductions in their own mortality risk, aggregated over a population [@viscusi2018pricing; @robinson2019global]. Waka Kotahi NZ Transport Agency raised its VSL from NZ\$4.88m to NZ\$12.5m in 2023 after replacing a 1991 survey [@denne2023rr698].
- **Health technology assessment** uses a cost per QALY threshold. In principle this is the marginal cost at which the health system produces health, so it is a supply-side value [@claxton2015methods]. NICE has used £20,000–30,000 per QALY since 1999 and moved to £25,000–35,000 in 2026. New Zealand's PHARMAC operates a fixed budget with no explicit threshold.
- **Central agencies** publish yet another value. NZ Treasury's CBAx tool values a QALY at about NZ\$36,000, and the UK Green Book at about £70,000.

The disagreement is old. Tengs and colleagues found that the cost per life-year of 500 US interventions varied across sectors by more than nine orders of magnitude [@tengs1995five]. When marginal costs per unit of health differ across agencies, reallocating money between them would increase total health at no extra cost. A consistent valuation is a precondition for spending efficiently.

Two literatures have studied the gap without closing it.

- **Bridging CBA and CEA.** One literature asks when cost-effectiveness analysis and cost–benefit analysis coincide. They do so under restrictive preference conditions [@pliskin1980utility; @bleichrodt1999life; @dolan2002bridge].
- **Estimating WTP per QALY.** The other estimates willingness to pay (WTP) per QALY directly, with results spanning more than an order of magnitude [@hirth2000wtp; @ryen2015wtp; @mason2009modelling; @baker2010svq].

Neither provides an operational rule that agencies can share, and neither separates legitimate from illegitimate sources of difference. This proposal does both.

# 2 Four layers of disagreement

Write the ratio between a road-safety VSL and a health-sector QALY value $k$, spread over remaining life expectancy $LE_a$ at the age $a$ of the people at risk, as

$$G \equiv \frac{\text{VSL}}{k \cdot LE_a}.$$

For New Zealand at $a = 40$ ($LE \approx 43.6$ years), VSL = NZ\$12.5m and $k$ = NZ\$36,000, so $G \approx 8.0$. The gap has four sources.

1. **Arithmetic.** A VSL covers remaining *discounted, quality-adjusted* life. At a 2% discount rate and population health norms, a 40-year-old's 43.6 remaining years are worth about 24.2 discounted QALYs. Correcting for this *raises* the implied value per QALY (to about NZ\$516,000), so the arithmetic widens the gap rather than closing it.
2. **Context.** People pay more to avoid deaths that are sudden, involuntary, dreaded or imposed by others than equally early deaths from illness [@chilton2002perceptions; @hammitt2010children].
3. **Opportunity cost.** A VSL is a demand-side value in private consumption units. A health threshold is a supply-side value: what a fixed public budget gives up at the margin [@claxton2015methods; @lomas2019marginal]. The two coincide only if the health budget is optimally sized.
4. **Measurement.** Stated-preference VSLs often fail scope tests: WTP rises less than in proportion to risk reductions, which inflates implied values [@johnston2017guidance]. Revealed-preference (wage–risk) estimates face their own biases.

Layer 1 is mechanical and should simply be standardised. Layer 4 is error to be removed. Layers 2 and 3 contain real economic content, and the framework below makes them explicit, estimable and open to public scrutiny.

# 3 Theory

## 3.1 The value of a life-year in a life-cycle model

Consider a person aged $a$ with survival function $S_a(t)$, health $h_t$, consumption $c_t$, income $y_t$ and period utility $u(c_t, h_t)$, discounting at rate $r$ with access to fair annuities [@rosen1988value; @shepard1984survival]. Expected lifetime utility is

$$V_a = \sum_{t \ge a} (1+r)^{-(t-a)}\, S_a(t)\, u(c_t, h_t).$$

The marginal rate of substitution between a small reduction in mortality risk at age $a$ and wealth is [@murphy2006value]

$$\text{VSL}_a = \sum_{t \ge a} (1+r)^{-(t-a)}\, S_a(t)\, \nu_t, \qquad \nu_t = \frac{u(c_t,h_t)}{\mu} + (y_t - c_t), \qquad (1)$$

Here $\mu = \partial V_a / \partial W$ is the marginal utility of lifetime wealth, and $\nu_t$ is the value of a life-year at age $t$. It is the consumption equivalent of being alive in that year, plus the person's net contribution to resources. Utility is normalised so that $u = 0$ corresponds to death.

## 3.2 When there is one value per QALY

Suppose period utility is multiplicatively separable, $u(c,h) = Q(h)\, w(c)$, so that health-related quality of life scales the utility of consumption. Suppose also that consumption is smooth at $\bar c$ and lifetime net saving is zero. These are the conditions under which QALY maximisation and cost–benefit analysis agree [@bleichrodt1999life].

**Proposition 1 (common value of a healthy year).** Under these conditions, $\nu_t = Q(h_t)\, v^*$ with $v^* \equiv w(\bar c)/\mu$, and

$$\text{VSL}_a = v^* \cdot \text{DQALE}_a, \qquad \text{DQALE}_a = \sum_{t \ge a}(1+r)^{-(t-a)} S_a(t)\, Q(h_t).$$

The WTP for any morbidity improvement that raises quality by $\Delta Q_t$ is $v^* \sum (1+r)^{-(t-a)} S_a(t) \Delta Q_t$.

*Proof sketch.* Substitute $u = Q(h_t)\,w(\bar c)$ and $y_t = c_t$ into (1), giving $\nu_t = Q(h_t)\,w(\bar c)/\mu$. For morbidity, $\partial V_a/\partial Q_t = (1+r)^{-(t-a)} S_a(t)\, w(\bar c)$; dividing by $\mu$ gives the stated WTP. ∎ Note that the normalisation by $\mu$, the marginal utility of lifetime wealth, is what makes $v^*$ a value per QALY. Dividing by the period marginal utility of consumption, $u_c = Q\,w'$, would cancel $Q$ and lose the quality adjustment.

So under QALY-consistent preferences, the VSL and the WTP per QALY are not rival values. They are the same parameter $v^*$, multiplied by different quantities of health. We call $v^*$ the **Common Value of a Healthy Year (CVHY)**.

Proposition 1 is testable. It implies that $\text{VSL}_a / \text{DQALE}_a$ is constant across ages and equals WTP per QALY elicited for morbidity. Systematic departures identify which assumption fails:

- departures that vary with age point to consumption profiles [@aldy2008adjusting];
- departures that vary with health state point to non-separability [@hammitt2002qalys].

## 3.3 Context premia

Let people derive additional disutility from exposure to risk of type $k$ (for example anxiety about a dreaded or involuntary hazard) that is not captured by the life-years at stake. Writing this as a context-specific term in the ex ante utility gives

$$\text{WTP}_k = \pi_k \, v^* \, \Delta \text{DQALE}, \qquad \pi_k \ge 1,$$

where $\pi_k$ is the **context multiplier** for risk type $k$. Whether policy should honour $\pi_k$ is a normative question. A premium for fear experienced while exposed is a real welfare effect. A premium for identified rather than statistical victims, or one that arises from misperceived risk, may not be. The framework treats $\pi_k$ as an estimated parameter that enters appraisal only after deliberative endorsement (Study 3).

## 3.4 Public budgets and sector shadow prices

Agencies do not spend private income. Each sector $s$ has a budget $B_s$, and the social planner solves

$$\max \; W = \sum_j x_j \Big( v^* \sum_k \pi_k \, \Delta Q_{jk} + \Delta Y_j \Big) \quad \text{s.t.} \quad \sum_{j \in s} x_j \, \Delta G_j \le B_s \;\; \forall s,$$

where $x_j \in \{0,1\}$ selects project $j$, $\Delta Q_{jk}$ is the project's discounted QALY gain in context $k$, $\Delta Y_j$ is its consumption-equivalent non-health benefit, and $\Delta G_j$ is its cost to the sector budget. The Lagrange multiplier $\lambda_s$ on each budget is the welfare value of a marginal dollar in sector $s$, expressed in consumption units.

**Proposition 2 (CVHY decision rule).** Project $j$ in sector $s$ should be funded if and only if

$$v^* \sum_k \pi_k \Delta Q_{jk} + \Delta Y_j \;\ge\; \lambda_s \, \Delta G_j .$$

For a pure health project, this is equivalent to a cost-per-QALY threshold of $k_s = v^*/\lambda_s$. Hence

$$\lambda_s = \frac{v^*}{k_s}.$$

A health agency whose marginal cost per QALY is NZ\$36,000 while $v^*$ is, say, NZ\$150,000 has $\lambda \approx 4.2$: each dollar in that budget is worth more than four dollars of private consumption. Allocative efficiency across government requires that $\lambda_s$ be equal across sectors, and equal to the marginal cost of public funds $\gamma$ (typically 1.1–1.3; @dahlby2008mcpf). Moving \$1 from sector $s$ to sector $s'$ changes welfare by about $\lambda_{s'} - \lambda_s$.

## 3.5 The exact decomposition

Combining Propositions 1 and 2 with a multiplicative measurement artefact $M_k$ in elicited values ($\text{VSL}^{\text{obs}}_k = M_k \pi_k v^* \text{DQALE}_a$) gives an identity for the observed gap:

$$\ln G = \underbrace{\ln \frac{\text{DQALE}_a}{LE_a}}_{\text{arithmetic}} + \underbrace{\ln \pi_k}_{\text{context}} + \underbrace{\ln M_k}_{\text{measurement}} + \underbrace{\ln \lambda_{\text{health}}}_{\text{opportunity cost}} . \qquad (2)$$

For New Zealand at age 40 and 2% discounting, $G = 7.96$ and the arithmetic term is $\ln(24.2/43.6) = -0.59$. The remaining three factors must therefore multiply to about 14.3. The empirical programme estimates each one. If, for example, $\pi_{\text{road}} = 1.3$, $M = 1.5$ and $\lambda_{\text{health}} = 7.3$, the transport and health values would be fully reconciled. The policy conclusion would then be that the health budget is too small, not that the road value is too high.

## 3.6 The reporting standard

We propose that every agency appraisal report health effects in discounted QALYs, by context, and value them using three published numbers:

1. **$v^*$**: the Common Value of a Healthy Year, estimated nationally and updated with income.
2. **$\pi_k$**: a short list of endorsed context multipliers (possibly all equal to 1).
3. **$\lambda_s$**: sector shadow prices of public funds, estimated from each sector's marginal productivity.

Mortality effects enter as $\Delta\text{DQALE}$ of the people affected. This replaces a single age-blind VSL with a life-table calculation; agencies that prefer an age-invariant value can still apply a population-average DQALE. The rule nests current practice:

- transport appraisal corresponds to $\lambda_{\text{transport}} = 1$, $\pi_{\text{road}}$ implicit in the VSL, and a fixed DQALE;
- health technology assessment corresponds to reporting $k = v^*/\lambda_{\text{health}}$ without stating either component.

## 3.7 Extensions

- **Distribution.** Equity weights can be added by replacing $v^*$ with person-specific values in a prioritarian social welfare function [@adler2014social]. Fleurbaey's equivalent-income approach offers a non-utilitarian alternative that respects individual trade-offs [@fleurbaey2013equivalent].
- **Wellbeing.** Life-satisfaction (WELLBY) valuations provide an independent cross-check on $v^*$ [@frijters2020happy].

# 4 Empirical programme

## 4.1 Study 1: National valuation survey

**Aim.** Estimate $v^*$, $\pi_k$ and $M_k$, and test Proposition 1, on one sample.

**Sample.** About 3,000 adults from a probability-based or high-quality quota online panel, with quotas for age, sex, region and education. Māori and Pasifika participants would be oversampled (n ≈ 600 each) so that subgroup estimates are precise. Data governance would follow Te Tiriti o Waitangi principles and Māori data sovereignty guidelines, with co-design through the Ngāi Tahu Research Consultation Committee.

**Design.** Each respondent completes four modules.

| Module | Task | Identifies |
|---|---|---|
| A. Mortality risk | Discrete choice experiment (DCE): pairs of policies reducing annual risk of death in one context, varying risk reduction (scope), latency, cost and payment vehicle | Context-specific VSL; scope elasticity $\Rightarrow M_k$ |
| B. Morbidity | DCE over health-improvement programmes varying EQ-5D-5L dimensions, duration and cost [@cameron2013demand] | WTP per QALY from morbidity |
| C. Health states | Composite time trade-off for 6 EQ-5D-5L states | Individual quality weights $Q(h)$ |
| D. Background | Subjective survival expectations, income, consumption, health, risk perceptions, numeracy | $S_a(t)$, $\bar c$, covariates |

**Arms.** Context is randomised between respondents across five contexts: road crashes, air pollution, workplace accidents, cancer (screening) and hospital care. Payment vehicle (private payment vs general taxation) is crossed with context. Within each arm, risk reductions vary over a 4:1 range for an internal scope test, and a split-sample external scope test is included [@johnston2017guidance].

**Estimation.** Each module is estimated by mixed logit in WTP space [@lancsar2008dce]. The structural step then estimates $v^*$ from Modules A and B jointly. It imposes $\text{WTP} = \pi_k v^* \Delta\text{DQALE}$, computing $\Delta\text{DQALE}$ for each respondent from their own survival expectations and TTO weights. The measurement factor $M_k$ is identified from departures from proportional scope.

**Power.** The main contrast is $\pi_k$ against road crashes. Log-WTP has a typical standard deviation of about 1.2 in comparable studies. Detecting $\pi = 1.25$ with 80% power at $\alpha = 0.05$ needs about 450 respondents per context arm; 600 per arm allows for exclusions and subgroup analysis. The payment-vehicle effect, with about 1,500 respondents per vehicle, can detect a 15% difference. Simulation-based power for the DCE designs would be completed with Bayesian efficient designs before fielding.

## 4.2 Study 2: Sector shadow prices

**Aim.** Estimate $\lambda_{\text{health}}$ and $\lambda_{\text{transport}}$.

**Health.**

- *Supply-side marginal productivity.* Following Claxton and colleagues and Lomas et al. [@claxton2015methods; @lomas2019marginal], we would estimate the elasticity of mortality and morbidity outcomes with respect to spending across health districts. New Zealand's population-based funding formula allocates money by formula rather than outcomes, so it supplies variation in spending that is plausibly unrelated to local health shocks. That variation serves as the instrument. The cost per QALY at the margin gives $k_{\text{health}}$, and $\lambda_{\text{health}} = v^*/k_{\text{health}}$.
- *Revealed preference from PHARMAC.* Binary-choice models of PHARMAC funding decisions on published cost-effectiveness ("QALYs per \$1 million") would estimate the implicit threshold [@devlin2004nice].

**Transport.** The marginal benefit–cost ratio of funded National Land Transport Programme projects estimates $\lambda_{\text{transport}}$ directly, because projects are valued with the VSL.

## 4.3 Study 3: Deliberative validation

Which context premia should count? Four citizens' panels (about 30 members each, demographically stratified, with Māori-led and Pasifika-led panels among them) would deliberate on whether premia for dread, involuntariness, identified victims and children should enter public appraisal. Panels would receive Study 1 results and structured evidence, then vote on each multiplier with reasons recorded. Only multipliers endorsed by a supermajority would be carried into the reporting standard. Any others would be reported as sensitivity analyses.

## 4.4 Study 4: Re-ranking New Zealand interventions

The final study would assemble about 40 recent NZ appraisals with published effects: PHARMAC listings, road-safety schemes, air-quality rules, school ventilation (linking to the CASCADE framework) and injury prevention. Each would be converted to discounted QALYs and consumption benefits, then re-ranked under the CVHY rule. The study would report:

- which decisions change under the unified rule;
- the health that could be gained by reallocating a fixed total budget across sectors;
- uncertainty from all four studies, propagated by probabilistic sensitivity analysis.

# 5 Pre-registered hypotheses

| | Hypothesis | Test |
|---|---|---|
| H1 | VSL-implied value per QALY ($\text{VSL}_a/\text{DQALE}_a$) is constant in age | Slope on age in structural model; Proposition 1 |
| H2 | VSL-implied value per QALY equals morbidity WTP per QALY | Equality of $v^*$ across Modules A and B |
| H3 | Context multipliers exceed 1 for road, workplace and air pollution relative to hospital care | $\pi_k > 1$, Holm-adjusted |
| H4 | Stated WTP is less than proportional to risk reduction | Scope elasticity < 1; $M_k > 1$ |
| H5 | WTP is lower under the taxation vehicle than under private payment | Vehicle coefficient |
| H6 | $\lambda_{\text{health}} > \lambda_{\text{transport}}$ | Studies 1–2 combined |
| H7 | Reallocation under the CVHY rule increases total discounted QALYs by at least 10% at constant total spending | Study 4 |

# 6 Threats to validity

- **Hypothetical bias and protest responses.** Mitigated with consequentiality scripts, cheap-talk scripts, debriefing questions and pre-specified exclusion rules.
- **Separability failure.** If H1 or H2 is rejected, $v^*$ becomes a function $v^*(Q, a)$ estimated from the same data. The decomposition (2) still holds, with age- or state-specific terms.
- **Instrument validity in Study 2.** Formula components could correlate with unobserved need. We would test over-identifying restrictions using multiple formula components, and report bounds.
- **Normative legitimacy.** Study 3 does not settle ethics. It provides transparent public input, and the reporting standard keeps every judgement visible as a separate number.

# 7 Outputs, timeline and resources

- **Months 1–6:** theory paper (§3); survey co-design and cognitive testing; ethics approval (University of Otago Human Ethics Committee); pre-registration.
- **Months 7–15:** Study 1 fieldwork and analysis; Study 2 data assembly.
- **Months 16–24:** Study 2 estimation; Study 3 panels.
- **Months 25–36:** Study 4; synthesis; draft guidance for Treasury CBAx and agency appraisal manuals.

**Indicative budget.** About NZ\$1.1m over three years. Main items are survey fieldwork (NZ\$250k), a research fellow and research assistant, panel costs (NZ\$120k) and Māori and Pasifika partnership roles. Suitable funders include the Marsden Fund (theory and Study 1), the Health Research Council (Studies 1–2) and the Ministry of Transport and Treasury (Study 4).

**Planned papers.**

1. "One price for a healthy year: a life-cycle decomposition of the VSL–QALY gap" (theory and NZ illustration).
2. "Valuing health and life on one scale: a national stated-preference study" (Study 1).
3. "The marginal productivity of New Zealand health spending" (Study 2).
4. "What should count? Citizens' panels on context premia" (Study 3).
5. "Rationalising life-saving expenditure across government" (Study 4).

# 8 Why this matters

The framework does not ask transport to adopt health's numbers, or health to adopt transport's. It asks every agency to use the same value of health and to state openly how its circumstances differ. If the health budget's shadow price is several times that of the transport budget, the right response is a budget decision made in daylight. Today the same question is answered implicitly, by agencies that do not know they disagree.

---

# References

::: {#refs}
:::
