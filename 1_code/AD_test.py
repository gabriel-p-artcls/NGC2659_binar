
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


def main():
    """
    """
    df1 = pd.read_csv("NGC2659_1.csv")
    df2 = pd.read_csv("NGC2659_2.csv")

    plx1, e_plx1 = df1['Plx'].values, df1['e_Plx'].values
    plx2, e_plx2 = df2['Plx'].values, df2['e_Plx'].values

    print("A-d statistic, significance_level")
    for _ in range(10):
        plx1_r = np.random.normal(plx1, e_plx1)
        plx2_r = np.random.normal(plx2, e_plx2)
        ad_test = stats.anderson_ksamp([plx1_r, plx2_r])
        print(ad_test[0], ad_test[-1])

    plt.hist(plx1, 30, alpha=.5, color='b', density=True)
    plt.hist(plx2, 30, alpha=.5, color='r', density=True)
    plt.show()


if __name__ == '__main__':
    # plt.style.use('science')
    main()
