
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plx, phot = {}, {}
for cl in ("NGC2659", "UBC_482", "UBC_246"):
    df = pd.read_csv("./ASteCA_out/" + cl + "/" + cl + ".csv", sep=r"\s+")
    plx[cl] = df['Plx']
    phot[cl] = df['Gmag']

Gcuts = (19, 18, 17, 16, 15, 14, 13, 12)

#
fig = plt.figure(figsize=(10, 5))

for cl in ("NGC2659", "UBC_482", "UBC_246"):
    xy = []
    for Gmax in Gcuts:
        msk = phot[cl] < Gmax
        y, ymin, ymax = np.percentile(1/plx[cl][msk], (50, 16, 84))
        print(cl, Gmax, msk.sum()) #, y, ymin, ymax)
        xy.append([Gmax, y, ymin, ymax])
    x, y, ymin, ymax = np.array(xy).T
    plt.plot(x, y, label=cl, lw=3)
    plt.fill_between(x, ymin, ymax, alpha=0.2)
    plt.legend(loc=2)
plt.xlabel("G max")
plt.ylabel("D [kpc]")
# plt.show()

fig.tight_layout()
plt.savefig("plx_vs_Gmag.png", dpi=150)