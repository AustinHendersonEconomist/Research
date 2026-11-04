"""Figures and calibration numbers for the CVHY theory paper.
Usage: python3 figures/make_figures.py  (from papers/cvhy-theory)"""
import math, json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = pathlib.Path(__file__).resolve().parent
LE=[(0,82.5),(5,77.9),(20,63.2),(40,43.6),(60,25.0),(70,16.7),(80,9.6),(90,4.5),(100,2.2)]
QN=[(0,.94),(20,.93),(40,.89),(60,.83),(70,.80),(80,.74),(100,.68)]
def ip(t,x):
    for i in range(1,len(t)):
        if x<=t[i][0]:
            a,ya=t[i-1];b,yb=t[i];return ya+(yb-ya)*(x-a)/(b-a)
    return t[-1][1]
def dqale(age,r,quality=True):
    e=ip(LE,age);s=0.0
    for t in range(math.ceil(e)):
        w=min(1,e-t);q=ip(QN,age+t+.5) if quality else 1.0;s+=w*q*(1+r)**-(t+.5)
    return s
VSL=12.5e6
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":9,"axes.spines.top":False,"axes.spines.right":False,"savefig.dpi":600,"savefig.bbox":"tight"})
ages=list(range(5,86))
fig,ax=plt.subplots(figsize=(5.6,3.2))
for r,ls in ((0,":"),(.02,"-"),(.035,"--")):
    ax.plot(ages,[VSL/dqale(a,r)/1e3 for a in ages],ls,color="#1f5a52",lw=1.4,label=f"r = {r*100:.1f}%")
ax.axhline(36,color="#b3431f",lw=.8);ax.text(6,44,"NZ Treasury CBAx QALY (≈NZ$36k)",color="#b3431f",fontsize=7.5)
ax.set_yscale("log");ax.set_xlabel("Age of the population at risk");ax.set_ylabel("Implied v* (NZ$ thousand, log scale)")
ax.legend(frameon=False,fontsize=8);fig.savefig(HERE/"fig1-implied-vstar.png");fig.savefig(HERE/"fig1-implied-vstar.pdf")
out={"G":VSL/(36000*ip(LE,40)),"LE40":ip(LE,40),"DQALE40_2":dqale(40,.02),"arith":dqale(40,.02)/ip(LE,40)}
out["residual"]=out["G"]/out["arith"]
for name,(pi,M) in {"A":(1,1),"B":(1.2,3),"C":(2,1.5)}.items():
    lam=out["residual"]/(pi*M); v=VSL/(pi*M*out["DQALE40_2"]); out[name]={"pi":pi,"M":M,"lambda":lam,"vstar":v,"k":v/lam}
out["vstar_range"]={a:VSL/dqale(a,.02) for a in (10,40,70)}
(HERE/"calibration.json").write_text(json.dumps(out,indent=1))
print(json.dumps(out,indent=1))
