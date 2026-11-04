---
title: "Audit of the supplemental materials for *Auditing with Rewards for Honesty and Punishments for Cheating*"
subtitle: "File audited: `Auditing JBEP Supplemental Materials Jan 2025.docx`"
date: "4 November 2026"
---

# Summary

I checked every reported number in the supplement that can be recomputed from the supplement itself:

- the expected-value table;
- the derivatives of the model;
- all χ² tests in Experiment 1, including the 21 pairwise *p*-values in Table 2;
- the minimum detectable effects and achieved-power figures;
- every count, percentage and mean in Table S2;
- all 42 rank-sum statistics in Tables S3 and S4.

The script `audit/recompute.py` reproduces each check, and its output is saved in `audit/recompute-output.txt`.

**Overall.** The empirical core is sound. The cheating rates, the Experiment 2 tallies and most test statistics are internally consistent, and I recovered integer cell counts that reproduce all Experiment 1 χ² statistics exactly. However, several errors would be visible to a careful referee. Five of them change a stated result or its interpretation:

| # | Severity | Location | Issue |
|---|---|---|---|
| A1 | **High** | Table S1 (expected values) | The cheating EVs for the punishment treatments are wrong: 1% P should be $0.99 (not $1.00) and 10% P $0.90 (not $0.99). The S3 text and the H1 classification already use the correct values. |
| A2 | **High** | Table S4; S5 results text | The honesty rank-sum for 10% P vs 1% R10 is reported as *Z* = 0.07, *p* = 0.94. Recomputed from Table S2, it is ***Z* = −2.07, *p* = 0.038**; the reported entry duplicates the 1% P vs 1% R10 cell. The claim that "the only significant difference" among small incentives is 10% P vs 1% P is therefore incorrect. |
| A3 | **High** | S4, H3 | Two comparisons are labelled as against the *10%* punishment arm but are, by their statistics, against the *1%* arm: (i) "1% chance of a $10 reward and a 10% chance of punishment … χ² < 0.01, *p* = 0.96" and (ii) "1% R10P … and a 10% chance of punishment was significant (χ² = 4.12, *p* = 0.04)". In (ii), the reported power (0.16) belongs to the 10% P comparison; for 1% P vs R10P it is about 0.53. |
| A4 | **Medium–high** | S4, H2; Table 2 | The control rate under H2 is given as 26.04%; everywhere else it is 23.77%. The 1% P vs control test gives χ² = 2.69, ***p* = 0.101**, which is not ≤ 0.10. The asterisk in Table 2 and the description "marginally significant" therefore do not meet the table's own threshold. With Yates' correction, *p* = 0.139. |
| A5 | **Medium** | S5 discussion | "Except for a 1% chance of a small punishment, all treatments weakened the norm against cheating" conflicts with Table S3 and the results text. 1% P is the treatment *with* a marginal weakening (*p* = 0.075), and 1% R shows no significant change (*p* = 0.13). |
| A6 | Medium | S4, H2 | 1% R vs control is reported as χ² = 0.65, *p* = 0.42. Recomputed, it is χ² = 0.35, *p* = 0.55, matching Table 2. |
| A7 | Medium | S4 throughout | The achieved power for 4 of 10 comparisons cannot be reproduced by standard formulas (details below). More fundamentally, post-hoc power computed from observed effects is a transformation of the *p*-value and is widely discouraged. |
| A8 | Low | Table S3 | 0 vs 1% R (cheating): *Z* is reported as 1.15 but is 1.51; the reported *p* = 0.13 matches 1.51 (digits transposed). |
| A9 | Low | Tables S3–S4 | The sign of *Z* is inconsistent across cells (e.g., 10% P vs 1% R is −1.44, but the same orientation elsewhere is positive). The captions also describe the tests as tests "of equal proportion of participants who cheated"; they are rank-sum tests of the appropriateness ratings. |
| A10 | Low | Table S2 | The second rating column is headed "−"; it should be "+" (socially appropriate). |
| A11 | Low | Model, S1 | Equation (6) differentiates with respect to *R*, which is undefined (should be *M*). Equations (7)–(8) use subscript *c,m*, which should be *c,k*. Experiment 2 refers to "(9)", which is unnumbered. |
| A12 | Low | Structure | There are two sections numbered "S3" and an unnumbered "S.2". The label "Table S1" is used twice. The treatments table is cited as "Table 2", which is also the label of the pairwise table. Figure 1 in S7 lacks an "S" prefix. There are stray "}" characters in two captions and LaTeX residue "$>$" in Experiment 2. |
| A13 | Low | Procedures | The procedures state that low and high payments were "$0.50 or $0.60" and "$1.00 or $1.10", but the EV table uses only $0.50 and $1.00. State which treatments used which pair. |
| A14 | Low | References | 10 works are cited but not listed, 3 are listed but not cited, and several names are misspelled (details below). |

The corrections below would make the supplement internally consistent without changing any of the main qualitative conclusions, except where noted under A2, A4 and A5.

---

# 1 Theory (S1, S2)

## 1.1 Expected values (Table S1, first instance) — A1

With honest payment *X* = $0.50, cheating payment *Y* = $1.00, a $1 penalty and $1 or $10 rewards:

| Treatment | EV(honest) reported | EV(cheat) reported | EV(honest) recomputed | EV(cheat) recomputed | Gain from cheating |
|---|---:|---:|---:|---:|---:|
| 1% punishment | $0.50 | $1.00 | $0.50 | **$0.99** | $0.49 |
| 10% punishment | $0.50 | $0.99 | $0.50 | **$0.90** | $0.40 |
| 1% small reward | $0.51 | $1.00 | $0.51 | $1.00 | $0.49 |
| 10% small reward | $0.60 | $1.00 | $0.60 | $1.00 | $0.40 |
| 1% large reward | $0.60 | $1.00 | $0.60 | $1.00 | $0.40 |
| 1% large reward or punishment | $0.60 | $0.99 | $0.60 | $0.99 | $0.39 |

The corrected values are already implied elsewhere in the supplement:

- S3 states that the expected gain falls from $0.50 to $0.40 under a 10% chance of punishment.
- H1 describes four treatments, including 10% P, as reducing the gain by $0.10–0.11.

Check that main-text Table 1 does not carry the same error.

## 1.2 Derivatives — A11

- Eq. (6): replace ∂EU~h,r~/∂*R* with ∂EU~h,r~/∂*M*.
- Eqs. (7)–(8): replace the subscript *c,m* with *c,k*, to match the punishment notation in (3)–(4).
- In Experiment 2, number the Krupka–Weber utility function as (9), or remove "Expanding (9)".
- Replace "(gamma) $>$ 0" with "γ > 0".

The signs of all derivatives are correct.

---

# 2 Experiment 1 statistics

## 2.1 Recovered cell counts

Each reported percentage is consistent with several integer fractions. The fractions below are the unique ones near the stated group sizes that reproduce the reported χ² statistics:

| Treatment | Cheated / *N* | Rate |
|---|---:|---:|
| Control | 29 / 122 | 23.77% |
| 1% punishment | 19 / 123 | 15.45% |
| 10% punishment | 13 / 124 | 10.48% |
| 1% reward | 32 / 118 | 27.12% |
| 10% reward | 43 / 126 | 34.13% |
| 1% $10 reward | 16 / 102 | 15.69% |
| 1% $10 reward + punishment | 7 / 103 | 6.80% |

Total *N* = 818. Report these counts in the supplement; they also allow readers to verify the tests. For example, 10% P = 11/105 would also give 10.48%, but only 13/124 reproduces χ² = 7.67 against control and χ² = 20.10 against 10% R.

## 2.2 Tests against reported values

All tests are Pearson χ² without continuity correction, which is what the reported statistics imply.

| Comparison (as described in text) | Reported | Recomputed | Note |
|---|---|---|---|
| 10% P vs control | χ² = 7.67, *p* < 0.01 | 7.67, *p* = 0.006 | ✓ |
| 10% R vs control | 3.23, *p* = 0.07 | 3.23, 0.072 | ✓ |
| 10% R vs 1% R | 1.41, 0.24 | 1.41, 0.236 | ✓ |
| 1% R10 vs control | 2.26, 0.13 | 2.26, 0.133 | ✓ |
| 1% R10P vs control | 11.97, *p* < 0.01 | 11.97, 0.001 | ✓ |
| 1% P vs control | 2.7, *p* = 0.10 | 2.69, **0.101** | A4: not ≤ 0.10 |
| 1% R vs control | 0.65, 0.42 | **0.35, 0.551** | A6 |
| 1% R vs 1% P | 4.92, 0.03 | 4.92, 0.027 | ✓ |
| 10% R vs 10% P | 20.10, *p* < 0.01 | 20.10, < 0.001 | ✓ |
| "1% R10 vs 10% P" | < 0.01, 0.96 | 10% P: 1.35, 0.245 · **1% P: 0.002, 0.961** | A3: arm mislabelled |
| "1% R10P vs 10% P" | 4.12, 0.04 | 10% P: 0.95, 0.329 · **1% P: 4.12, 0.042** | A3: arm mislabelled |

**Table 2 (pairwise *p*-values).** All 21 entries match the recomputed values to the reported precision, except 1% P vs control (reported 0.10*, recomputed 0.101). Several Table 2 cells are only significant without continuity correction: 1% P vs 1% R10P (*p* = 0.042; Yates 0.069), 1% R vs 1% R10 (0.041; 0.060) and 1% R10 vs 1% R10P (0.044; 0.073). State the test variant in the caption. Given 21 pairwise comparisons, also consider a multiplicity statement, such as Holm-adjusted *p*-values in an extra column.

## 2.3 Minimum detectable effects

The recomputed MDEs (two-sided α = 0.05, *N* = 125 per group, control 23.77%, pooled-variance normal approximation) are +16.50, +11.30, −13.30 and −9.75 pp. These agree with the reported +16.45, +11.30, −13.29 and −9.71 pp to within the resolution of the method. ✓

The observed 10% P reduction is 23.77 − 10.48 = 13.29 percentage points. In S3, "13.29%" should read "13.29 percentage points"; as written it reads as a relative change.

## 2.4 Achieved power — A7

| Comparison | Reported | Recomputed (pooled / unpooled / arcsine) |
|---|---:|---|
| 10% P vs control | 0.84 | 0.79 / 0.80 / 0.80 |
| 10% R vs control | 0.36 | 0.43 / 0.44 / 0.44 |
| 1% R10 vs control | 0.38 | 0.32 / 0.33 / 0.33 |
| 1% R10P vs control | 0.96 | 0.95 / 0.96 / 0.96 ✓ |
| 1% P vs control | 0.44 | 0.37 / 0.38 / 0.38 |
| 1% R vs control | 0.07 | 0.09 |
| 1% R vs 1% P | 0.60 | 0.60 ✓ |
| 10% R vs 10% P | 0.99 | 1.00 ✓ |
| 1% R10P vs 1% P | 0.16 | 0.53 (0.16 is the value for 10% P) |

The required sample sizes also differ for some comparisons. For 10% R vs control, 372 is reported against 300 recomputed; for 1% P vs control, 290 against 357. The figure of 192 for 1% R vs 1% P matches.

**Recommendation.** Remove "achieved power" entirely. Post-hoc power computed at the observed effect is a one-to-one function of the *p*-value and adds no information (Hoenig, J. M. and Heisey, D. M. (2001), "The abuse of power", *The American Statistician*, 55(1), 19–24). Keep the ex ante MDE analysis, which is informative. Report 95% confidence intervals for each difference in proportions, and, where a null is interpreted as "no effect", an equivalence bound. The H3 claim about *equal* rates in particular calls for an equivalence test (e.g., TOST) rather than a non-significant χ².

---

# 3 Experiment 2 statistics

## 3.1 Table S2

All 14 rows sum to the stated *N*, and the recomputed means match the reported means to two decimals. *N* sums to 836, as stated. ✓ The only defect is the column header (A10). A missing parenthesis in "10 (8.40" for R10P–H should be closed.

## 3.2 Rank-sum tests (Tables S3–S4)

I recomputed Wilcoxon–Mann–Whitney *Z* statistics, with tie correction, from the Table S2 counts.

**Table S3 (cheating, T).** All 21 cells match in absolute value except 0 vs 1% R: reported 1.15 (0.13), recomputed 1.51 (0.130) (A8).

**Table S4 (honesty, H).** All cells match except **10% P vs 1% R10: reported 0.07 (0.94), recomputed −2.07 (0.038)** (A2). The S5 text gives "Z = 1.71, p = 0.07" for R10P vs 10% R; Table S4 and the recomputation give 1.81 (0.070).

**Signs (A9).** Choose one orientation, such as positive *Z* when the column treatment is rated *more* appropriate than the row treatment, and apply it to every cell. Currently, several cells (e.g., 10% P vs 1% R in Table S3; 10% P vs 1% R and vs 10% R in Table S4) have the opposite orientation to their neighbours.

## 3.3 Corrected wording

- **S5 results**, final paragraph, replace the opening clause with: "the social appropriateness of reporting honestly was mostly unaffected by small incentives alone; the exceptions were that honesty was rated less appropriate under a 10% chance of punishment than under a 1% chance of punishment (*Z* = −1.99, *p* = 0.046) or a 1% chance of a $10 reward (*Z* = −2.07, *p* = 0.038)."
- **S5 discussion**, replace the first finding with: "Compared with control, a 10% chance of audit with either punishment or reward and a 1% chance of a $10 reward significantly weakened the norm against cheating, a 1% chance of punishment and a $10 reward with punishment weakened it marginally, and a 1% chance of a small reward did not significantly change it."

---

# 4 Presentation and references

**Numbering (A12).** Use S1–S8 consistently and update the contents list, adding S2. Label the treatments table "Table S2" and renumber the following tables. Change "Figure 1" in S7 to "Figure S9", or cite it as main-text Figure 1. Remove the stray "}" in the Figure S8 and Table 2 captions.

**Typos.** "So rensen" → "Sørensen"; "Soble" → "Sobel"; "Lowenstein" → "Loewenstein"; "Follmi-Heusi" → "Föllmi-Heusi"; "`a la" → "à la"; "could driven behavior" → "could drive behavior"; "lead to a higher level" → "led to a higher level"; "randomly assigned to one just one" → "randomly assigned to just one"; "is intuitively more probably associated with producing" → "is intuitively more likely to produce"; "Forest, Simmons, and Chesters, 2000" → "Forrest, Simmons and Chesters (2002)" (check the year).

**Cited in the text but missing from Works Cited (A14):**

- Rabin (2000)
- Laske, Saccardo and Gneezy (2018)
- Gneezy (2005)
- Fischbacher and Föllmi-Heusi (2013)
- Loewenstein et al. (2001)
- Krupka and Weber (2013); the text also cites "2011", so check which is meant
- Forrest, Simmons and Chesters (2002)
- Andreoni, Harbaugh and Vesterlund (2003) is listed ✓; Becker (1968) is listed, but cite the original, *Journal of Political Economy*, 76(2), 169–217, rather than the Palgrave reprint

**Listed but not cited:** Gneezy (2003), "The W effect of incentives"; Gneezy and Rustichini (2004); Lochner and Moretti (2004).

**Incomplete or incorrect entries:**

- *Dufwenberg (2016)*: the published version is Dufwenberg, M. Jr. and Dufwenberg, M. Sr. (2018), "Lies in disguise—A theoretical analysis of cheating", *Journal of Economic Theory*, 175, 248–264.
- *Bérgolo et al.*: a published version exists, in *American Economic Journal: Economic Policy*, 2023. Confirm the volume and pages.

**Style.** *JBEP* uses author–date (APA-style) references. Remove the numbering from the Works Cited list and format it consistently.

---

# 5 What did not need correcting

- All seven cheating rates.
- All Table S2 counts, percentages and means.
- 20 of 21 Table 2 *p*-values.
- 40 of 42 rank-sum *Z* statistics in absolute value.
- The MDE calculations.
- The prior-literature arithmetic in S3: 39–64% of participants responsive, and 1 pp per $0.01 under the uniform assumption.

*Method note.* The checks used only information in the supplement. Cell counts were inferred, as described in Section 2.1, and should be confirmed against the raw data. Rank-sum statistics were computed with the normal approximation and tie correction (as in Stata's `ranksum`).
