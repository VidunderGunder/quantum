# %% [markdown]

"""
# Exercise 1

**Norsk**: Beregn transmisjons- og refleksjonskoeffisienten for en partikkel beskrevet ved en planbølge med energien E = 0.20eV som sendes inn mot et potensialtrinn med potensiell energi V0 = 0.16eV. Lag et plot som viser hvordan transmisjonskoeffisienten endrer seg n ̊ar energien øker, og kommenter resultatet.\
\
**English**: Calculate the transmission and reflection coefficients for a particle described by a beam with energy E = 0.20eV and sent into a potential well with potential energy V0 = 0.16eV. Create a plot showing how the transmission coefficient changes with the energy, and comment the result.
"""

# %%

import numpy as np
import seaborn as sns

sns.set_theme(style="darkgrid")


def reflection_coefficient(E, V0):
    # Supress sqrt warning
    with np.errstate(divide="ignore", invalid="ignore"):
        return (
            (np.sqrt(E) - np.sqrt(E - V0)) / (np.sqrt(E) + np.sqrt(E - V0))
        ) ** 2


def transmission_coefficient(E, V0):
    # Supress sqrt warning
    with np.errstate(divide="ignore", invalid="ignore"):
        return (4 * np.sqrt(E) * np.sqrt(E - V0)) / (
            np.sqrt(E) + np.sqrt(E - V0)
        ) ** 2


def is_correct(R, T):
    return R + T == 1


def plot_coefficients(Es=np.linspace(0, 1, 100), V0=0.20):
    """
    Create a plot showing how the transmission coefficient changes with the E using Seaborn
    """
    Rs = reflection_coefficient(Es, V0)
    Ts = transmission_coefficient(Es, V0)
    sns.lineplot(x=Es, y=Rs, label="Reflection")
    sns.lineplot(x=Es, y=Ts, label="Transmission")
    sns.lineplot(x=Es, y=Rs + Ts, label="Total")
    sns.lineplot(x=Es, y=np.ones(len(Es)), label="1")
    sns.axes_style("darkgrid")


plot_coefficients()
