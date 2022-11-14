
import numpy as np
import pandas as pd
import astropy.units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt

in_fold = "../0_data/2_ASteCA_in_05/"
out_fold = "../2_pipeline/plots/"

# Radii in arcmins
radii = {"NGC_2659": 6.35, "UBC_482": 34.04, "UBC_246": 25.31}

xyz_c, rads = {}, {}
clusters = ("NGC_2659", "UBC_482", "UBC_246")
for cl in clusters:
    df = pd.read_csv(in_fold + cl + ".csv")

    # Estimate center
    gc = SkyCoord(
        l=np.median(df['GLON']) * u.degree, b=np.median(df['GLAT']) * u.degree,
        distance=(1 / np.median(df['Plx'])) * u.kpc, frame='galactic')
    xyz_c[cl] = (
        gc.cartesian.x.value, gc.cartesian.y.value, gc.cartesian.z.value)

    # Estimate radius
    rad = radii[cl] / 60.  # arcmin to degrees
    r_kpc = 1 / np.median(df['Plx']) * np.tan(np.deg2rad(rad / 2.))
    rads[cl] = r_kpc


def plt_sphere(ax, c, r, cl):
    """
    Source: https://stackoverflow.com/a/64658465/1391441

    Fix for labels: https://stackoverflow.com/a/65554217/1391441
    """
    # draw sphere
    u, v = np.mgrid[0:2 * np.pi:50j, 0:np.pi:50j]
    x = r * np.cos(u) * np.sin(v)
    y = r * np.sin(u) * np.sin(v)
    z = r * np.cos(v)
    c1 = ax.plot_surface(x - c[0], y - c[1], z - c[2], alpha=0.5, label=cl)
    c1._facecolors2d = c1._facecolor3d
    c1._edgecolors2d = c1._edgecolor3d


fig = plt.figure()
ax = fig.gca(projection='3d')
for cl in clusters:
    plt_sphere(ax, xyz_c[cl], rads[cl], cl)

ax.set_xlim(0.08, 0.32)
ax.set_zlim(-0.045, 0.195)
ax.set_xlabel("X [kpc]")
ax.set_ylabel("Y [kpc]")
ax.set_zlabel("Z [kpc]")

plt.legend()
plt.show()

# fig.tight_layout()
# plt.savefig(out_fold + "3_clusts.png", dpi=150)
