
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""
Use the Carrasco transformations:
https://gea.esac.esa.int/archive/documentation/GDR3/Data_processing/chap_cu5pho/cu5pho_sec_photSystem/cu5pho_ssec_photRelations.html#Ch5.T10

For the Johnson-Cousins system we usa coefficients from Table 5.9
"""


Av = {"NGC2659": 1.718, "UBC_482": 1.359, "UBC_246": 1.519}
dm = {"NGC2659": 11.33, "UBC_482": 11.05, "UBC_246": 11.34}

N_brightest = 15

plx, phot = {}, {}
for cl in ("NGC2659", "UBC_482", "UBC_246"):
    print(cl)

    df = pd.read_csv("./ASteCA_out/" + cl + "/" + cl + ".csv", sep=r"\s+")
    G_obs = df['Gmag']
    BPRP = df['BP-RP']
    probs = df['probs_final']

    G_V = -0.02704 + 0.01424 * BPRP - 0.2156 * BPRP**2 + 0.01426 * BPRP**3
    V_obs = -1 * (G_V - G_obs)

    # Convert V observed to V intrinsic
    # V_int = V_obs - dm - Av
    V_int = V_obs - dm[cl] - Av[cl]

    # Select the N_brightest brightest
    msk = np.argsort(V_int.values)[:N_brightest]

    # Select brightest stars
    df_out = df.loc[msk]
    # Add column
    df_out['V0'] = V_int[msk]
    # Remove columns
    df_out.drop(['sel', 'memb_probs'], axis=1, inplace=True)

    df_out.to_csv(cl + '.csv')

    # plt.scatter(BPRP, V_int, c=probs)
    # plt.gca().invert_yaxis()
    # plt.colorbar()
    # plt.show()
