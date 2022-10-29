
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Parallax analysis using stars with membership P>0.5
"""

in_fold = "../0_data/2_ASteCA_in_05/"
out_fold = "../2_pipeline/plots/"

plx, phot = {}, {}
for cl in ("NGC_2659", "UBC_482", "UBC_246"):
    df = pd.read_csv(in_fold + cl + ".csv")
    plx[cl] = df['Plx']
    phot[cl] = df['Gmag']

# Gcuts = (19, 18, 17, 16, 15, 14, 13, 12)

#
# fig = plt.figure(figsize=(10, 5))
# plt.suptitle("Stars with P>0.5")
# for cl in ("NGC_2659", "UBC_482", "UBC_246"):
#     xy = []
#     for Gmax in Gcuts:
#         msk = phot[cl] < Gmax
#         y, ymin, ymax = np.percentile(1 / plx[cl][msk], (50, 16, 84))
#         print(cl, Gmax, msk.sum()) #, y, ymin, ymax)
#         xy.append([Gmax, y, ymin, ymax])
#     x, y, ymin, ymax = np.array(xy).T
#     plt.plot(x, y, label=cl, lw=3)
#     plt.fill_between(x, ymin, ymax, alpha=0.2)
#     plt.legend(loc=2)
# plt.xlabel("G max")
# plt.ylabel("D [kpc]")
# fig.tight_layout()
# plt.savefig(out_fold + "plx_vs_Gmag.png", dpi=150)

Gmax = 17
fig = plt.figure(figsize=(5, 5))
plt.title(f"DM from plx of P>0.5, G>{Gmax} stars")
for cl in ("NGC_2659", "UBC_482", "UBC_246"):
    msk = phot[cl] < Gmax
    dm = -5 + 5 * np.log10(1000 / plx[cl][msk])
    dm_16, dm_50, dm_84 = np.percentile(dm, (16, 50, 84))
    std = np.std(dm)
    print("{}: {:.2f} {:.2f} {:.2f} {:.2f}".format(
        cl, dm_16, dm_50, dm_84, std))
    plt.hist(dm, label=r"{} ({}), {:.2f}$_{{{:.2f}}}^{{{:.2f}}}$".format(
        cl, msk.sum(), dm_50, dm_16, dm_84), alpha=.2, density=True)
    plt.axvline(dm_50, ls='--', c='k')
    plt.legend(fontsize=8)
plt.xlabel("dm")
fig.tight_layout()
plt.savefig(out_fold + "dm_hist.png", dpi=150)