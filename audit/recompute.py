"""Recompute statistics reported in 'Auditing JBEP Supplemental Materials Jan 2025.docx'.

Cell counts are inferred from reported percentages (the unique integer
numerator/denominator pairs consistent with them near the reported N);
see audit report for the inference. Run: python3 audit/recompute.py
"""
import itertools, json
import numpy as np
from scipy import stats
from scipy.stats import norm

# --- Experiment 1: inferred counts (cheaters / N) -------------------------
E1 = {"10% P": (13, 124), "1% P": (19, 123), "0": (29, 122), "1% R": (32, 118),
      "10% R": (43, 126), "1% R10": (16, 102), "1% R10P": (7, 103)}
for k, (x, n) in E1.items():
    print(f"{k:8s} {x:3d}/{n:3d} = {100*x/n:6.2f}%")

def chi2(a, b, correction=False):
    t = np.array([[a[0], a[1] - a[0]], [b[0], b[1] - b[0]]])
    c, p, _, _ = stats.chi2_contingency(t, correction=correction)
    return c, p

def power_two_prop(p1, p2, n1, n2, alpha=0.05):
    # Normal approximation with pooled variance under H0 (as in Stata power twoproportions).
    pbar = (p1 * n1 + p2 * n2) / (n1 + n2)
    se0 = np.sqrt(pbar * (1 - pbar) * (1 / n1 + 1 / n2))
    se1 = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    z = norm.ppf(1 - alpha / 2)
    d = abs(p1 - p2)
    return norm.cdf((d - z * se0) / se1) + norm.cdf((-d - z * se0) / se1)

def n_required(p1, p2, power=0.8, alpha=0.05):
    for n in range(2, 100000):
        if power_two_prop(p1, p2, n, n, alpha) >= power: return n

out = {"pairwise": {}}
names = list(E1)
print("\nPairwise chi-square (no continuity correction) | with Yates")
for a, b in itertools.combinations(names, 2):
    c, p = chi2(E1[a], E1[b]); cy, py = chi2(E1[a], E1[b], True)
    pa, pb = E1[a][0] / E1[a][1], E1[b][0] / E1[b][1]
    pw = power_two_prop(pa, pb, E1[a][1], E1[b][1])
    out["pairwise"][f"{a} vs {b}"] = dict(chi2=c, p=p, chi2_yates=cy, p_yates=py, power=pw, n_req=n_required(pa, pb))
    print(f"{a:8s} vs {b:8s} chi2={c:6.2f} p={p:.3f} | yates chi2={cy:5.2f} p={py:.3f} | power={pw:.2f} n80={n_required(pa, pb)}")

# --- MDEs at control rate 23.77%, N = 125 per group -------------------------
p0 = 0.2377
def mde(direction, power, n=125):
    grid = np.arange(0.0005, 0.7, 0.0005)
    for d in grid:
        p1 = p0 + direction * d
        if 0 < p1 < 1 and power_two_prop(p0, p1, n, n) >= power: return d
print("\nMDEs (pp), N=125/group, alpha 0.05:")
for direction, lab in ((1, "increase"), (-1, "decrease")):
    for pw in (0.8, 0.5):
        print(f"  {lab} power {pw}: {100*mde(direction, pw):.2f}")
out["mde"] = {f"{lab}_{pw}": 100 * mde(dr, pw) for dr, lab in ((1, "increase"), (-1, "decrease")) for pw in (0.8, 0.5)}

# --- Expected values ----------------------------------------------------------
X, Y = 0.50, 1.00
ev = {"1% P": (X, 0.99 * Y + 0.01 * (Y - 1)), "10% P": (X, 0.9 * Y + 0.1 * (Y - 1)),
      "1% R": (X + 0.01 * 1, Y), "10% R": (X + 0.1 * 1, Y), "1% R10": (X + 0.01 * 10, Y),
      "1% R10P": (X + 0.01 * 10, 0.99 * Y + 0.01 * (Y - 1))}
print("\nExpected values (honest, cheat, gap) with X=0.50, Y=1.00, M=1 or 10:")
for k, (h, c) in ev.items(): print(f"  {k:8s} {h:.2f} {c:.2f} gap {c-h:.2f}")
out["ev"] = ev

# --- Experiment 2: Table S2 counts (++, +, 0, -, --) --------------------------
S2 = {"0": {"H": [59, 12, 8, 31, 9], "T": [10, 7, 16, 32, 54]},
      "0.01P": {"H": [62, 15, 13, 19, 10], "T": [15, 10, 13, 42, 39]},
      "0.1P": {"H": [50, 13, 17, 20, 20], "T": [25, 11, 19, 22, 43]},
      "0.01R": {"H": [57, 14, 20, 19, 10], "T": [7, 18, 19, 32, 44]},
      "0.1R": {"H": [59, 9, 16, 25, 9], "T": [16, 11, 19, 40, 32]},
      "R10": {"H": [62, 23, 8, 15, 13], "T": [18, 17, 13, 36, 37]},
      "R10P": {"H": [69, 20, 10, 11, 9], "T": [18, 16, 16, 19, 50]}}
reportedN = {"0": 119, "0.01P": 119, "0.1P": 120, "0.01R": 120, "0.1R": 118, "R10": 121, "R10P": 119}
reportedMean = {("0", "H"): .37, ("0", "T"): -.44, ("0.01P", "H"): .43, ("0.01P", "T"): -.29, ("0.1P", "H"): .23, ("0.1P", "T"): -.18,
                ("0.01R", "H"): .38, ("0.01R", "T"): -.35, ("0.1R", "H"): .38, ("0.1R", "T"): -.22, ("R10", "H"): .43, ("R10", "T"): -.21,
                ("R10P", "H"): .53, ("R10P", "T"): -.28}
w = np.array([1, 1 / 3, 0, -1 / 3, -1])
print("\nTable S2 check: sum vs N; recomputed mean vs reported")
out["S2"] = {}
for t, d in S2.items():
    for a, c in d.items():
        c = np.array(c); m = float(c @ w / c.sum())
        flag = "" if (c.sum() == reportedN[t] and abs(m - reportedMean[(t, a)]) < 0.006) else "  <-- CHECK"
        out["S2"][f"{t} {a}"] = dict(sum=int(c.sum()), N=reportedN[t], mean=m, reported=reportedMean[(t, a)])
        print(f"  {t:6s} {a}: sum {c.sum()} (N {reportedN[t]}), mean {m:+.3f} (reported {reportedMean[(t, a)]:+.2f}){flag}")

def ranksum(c1, c2):
    v = np.repeat(w, c1), np.repeat(w, c2)
    # Stata-style ranksum z with tie correction: sign follows group 1 rank sum minus expected
    x = np.concatenate(v); r = stats.rankdata(x)
    n1, n2 = len(v[0]), len(v[1]); N = n1 + n2
    R1 = r[:n1].sum(); E = n1 * (N + 1) / 2
    _, tc = np.unique(x, return_counts=True)
    var = n1 * n2 / 12 * ((N + 1) - (tc ** 3 - tc).sum() / (N * (N - 1)))
    z = (R1 - E) / np.sqrt(var)
    return z, 2 * norm.sf(abs(z))

order = ["0.1P", "0.01P", "0", "0.01R", "0.1R", "R10", "R10P"]
out["ranksum"] = {}
for a_ in ("T", "H"):
    print(f"\nRank-sum (row vs column), action {a_}: |z| and p")
    for i, r1 in enumerate(order):
        row = []
        for r2 in order[i + 1:]:
            z, p = ranksum(S2[r1][a_], S2[r2][a_])
            out["ranksum"][f"{a_} {r1} vs {r2}"] = dict(z=z, p=p)
            row.append(f"{r2}:{z:+.2f}({p:.3f})")
        print(f"  {r1:6s} " + "  ".join(row))

json.dump(out, open(__file__.replace("recompute.py", "recompute-results.json"), "w"), indent=1, default=float)
