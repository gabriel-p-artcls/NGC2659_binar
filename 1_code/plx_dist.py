
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xy, plx, pms, phot = {}, {}, {}, {}
for cl in ("NGC2659", "UBC_482", "UBC_246"):
    df = pd.read_csv("./ASteCA_out/" + cl + "/" + cl + ".csv", sep=r"\s+")
    plx[cl] = df['Plx']
    pms[cl] = [df['pmRA'], df['pmDE']]
    xy[cl] = [df['GLON'], df['GLAT']]
    phot[cl] = [df['BP-RP'], df['Gmag']]

#
fig = plt.figure(figsize=(10, 10))
plt.subplot(221)
for cl, xy_v in xy.items():
    plt.scatter(*xy_v, label=cl, alpha=.3)
plt.xlabel("GLON")
plt.ylabel("GLAT")
plt.legend()
plt.subplot(222)
for cl, pms_v in pms.items():
    plt.scatter(*pms_v, label=cl, alpha=.3)
plt.legend()
plt.xlabel("pmRA")
plt.ylabel("pmDE")
plt.subplot(223)
for cl, plx_v in plx.items():
    plt.hist(plx_v, label=cl, density=True, alpha=.3)
plt.legend()
plt.xlabel("Plx")
plt.subplot(224)
for cl, phot_v in phot.items():
    plt.scatter(*phot_v, label=cl, alpha=.3)
plt.gca().invert_yaxis()
plt.legend()
plt.xlabel("BP-RP")
plt.ylabel("Gmag")

fig.tight_layout()
plt.savefig("3_clusts.png")
