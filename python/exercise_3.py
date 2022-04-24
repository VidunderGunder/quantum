# %% [markdown]

"""
# Exercise 2

Too much LaTeX to bother copying the text.
"""

# %%

from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")

h = 6.582 * 10 ** -16  # ... [eV * s]
m = 9.109 * 10 ** -31  # electron mass [kg]
V0 = 0.16  # potential [eV]

resolution = 200 + 1

E_array = np.linspace(0.2, 0.4, resolution)  # energy [eV]
a_array = np.linspace(0, 20, resolution)  # incoming angles [degrees]


def get_Kx(E, a):
    """Get x-component of waveplane [m]"""
    return (np.sqrt(2 * m * E) / h) * np.cos(a)


def get_Ky(E, a):
    """Get y-component of waveplane [m]"""
    return (np.sqrt(2 * m * E) / h) * np.sin(a)


def get_K0x(E, a):
    """Get ... [m]"""
    return np.sqrt(
        ((np.sqrt(2 * m * (E - V0)) / h)) ** 2 - (get_Ky(E, a)) ** 2
    )


def R(E, a):
    """Get the reflection coefficient"""
    Kx = get_Kx(E, a)
    K0x = get_K0x(E, a)
    return ((Kx - K0x) / (Kx + K0x)) ** 2


def get_R_array(E_array, a_array):
    R_array = np.zeros((len(E_array), len(a_array)))
    for i, E in enumerate(E_array):
        for j, a in enumerate(a_array):
            R_array[i, j] = R(E, a)
    return R_array


def T(E, a):
    """Get the transmission coefficient"""
    Kx = get_Kx(E, a)
    K0x = get_K0x(E, a)
    return (4 * Kx * K0x) / (Kx + K0x) ** 2


def get_T_array(E_array, a_array):
    T_array = np.zeros((len(E_array), len(a_array)))
    for i, E in enumerate(E_array):
        for j, a in enumerate(a_array):
            T_array[i, j] = T(E, a)
    return T_array


def is_correct(R, T, margin=0.05):
    return np.allclose(R + T, 1, atol=margin)


#  Check if the reflection and transmission coefficients are correct
#  for all values of E and a


def test_correctness():
    """
    assert that the sum of R and T is 1 for all values of E and a
    """
    successes = 0
    fails = 0

    for E in E_array:
        for a in a_array:
            _R = R(E, a)
            _T = T(E, a)

            # Skip iteration if either the reflection- or the transmission coefficient is not a number
            if np.isnan(_R) or np.isnan(_T):
                continue

            correct = is_correct(_R, _T)

            if correct:
                successes += 1
            else:
                fails += 1
                print("E: {}, a: {}".format(E, a))
                print("R = {}, T = {}".format(R(E, a), T(E, a)))
                print("Sum = {}".format(R(E, a) + T(E, a)))

    if fails > 0:
        print("{} errors".format(fails))

    assert fails == 0


def get_ticklabels(arr, major=5, decimals=2):
    """
    Get ticklabels for a given array
    """
    ticklabels = []

    # replace all values where `index % major` is not 0 with an empty string

    for index, value in enumerate(arr):
        if index % major != 0:
            ticklabels.append("")
        else:
            ticklabels.append(f"{value:.{decimals}f}")

    return ticklabels


def plot(E_array, a_array):
    """
    Heatmap showing transmission coefficient `T` as a function of energy `E` and incoming angle `a`

    ### Plot specs:
    
    - Label: `Transmission Coefficient`
    - size: 10x10
    - x-label: Energy [eV]
    - x-axis labels: show `E`, round to 2 decimals show all zeros
    - y-label: Angle [degrees]
    - y-axis labels: show `a`, round to 1 decimal show all zeros
    """
    _, ax = plt.subplots(figsize=(10, 10),)
    ax.set_title("Transmission Coefficient")

    T_array = get_T_array(E_array, a_array)

    sns.heatmap(
        T_array,
        cmap="YlGnBu",
        ax=ax,
        xticklabels=get_ticklabels(E_array, decimals=3),
        yticklabels=get_ticklabels(a_array, decimals=1),
    )


test_correctness()
plot(E_array, a_array)
