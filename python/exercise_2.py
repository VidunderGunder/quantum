# %% [markdown]

"""
# Exercise 2

**Norsk**: Den tidsavhengige Schrödingerlikningen er gitt ved:

\begin{equation}

- \frac{\hbar^2}{2m} \frac{d^2 \phi(x,t)}{dx^2} = i\hbar \frac{d \phi(x,t)}{dt}

\end{equation}

Vi har sett hvordan vi løser Schrödingerlikningen analytisk for et utvalg av potensialer. Vi kan også løse Schrödingerlikningen numerisk. Numerisk kan man uttrykke derivasjon ved

\begin{equation}

\frac{d \phi(x,t)}{dt} = \frac{\phi(x,t + \Delta t) - \phi(x,t)}{(\Delta x)^2}

\end{equation}

\begin{equation}

\frac{d^2 \phi(x,t)}{dx^2} = \frac{\phi(x + \Delta x,t) - 2 \phi(x,t) + \phi(x - \Delta x,t)}{(\Delta x)^2}

\end{equation}

Ønsker dere å lese mer om denne metoden, søk opp *Finite Difference Methods*.

I denne oppgaven skal dere sende en bølgepakken inn mot trinnpotensialet fra oppgave 1. Bølgepakken er spesifisert av parameterne nedenfor, og er gitt ved funksjonen

\begin{equation}

\phi(x) = \frac{1}{\pi^\frac{1}{4}\sqrt{\sigma}}\exp[- \frac{1}{2}\frac{(x - x_0)^2}{\sigma^2}]\exp[ik(x - x_0)]

\end{equation}
\
Trinnpotensialet og bølgepakken befinner seg i en boks med bredden $L$. Trinnet starter ved $x = 100nm$ og har verdien $V_0$, se figur 2. Ved hjelp av likningene ovenfor, finn et utrykk for $Φ$ ved tiden $t+\Delta t$ og propager bølgepakken inn mot trinnpotensialet ved å beregne bølgepakken for hvert tidssteg $\Delta t$.\
\
Beregn så transmisjons- og refleksjonskoeffisientene for dette potensialet, og sammenlikn med svaret dere fikk i oppgave 1. For å beregne transmisjons- og refleksjonskoeffisientene i dette tilfellet kan dere integrere over den transmitterte og reflekterete delen hver for seg. Propager bølgepakken til dere får to separerte bølgepakker før dere utfører integrasjonen. Plot en figur av bølgepakken ved $t = 0$ og plot en figur når bølgepakken er fullstenig reflektert og transmittert. Vis figuren i oppgavebesvarelsen. Lag også en video der dere følger bølgepakken fra $t = 0$ og til den er fullstenig
reflektert og transmittert (se tips nedenfor).\
\
I denne oppgaven bruker dere følgende parametre:

- $\sigma = 1 * 10^{-8}m$
- $E = 0.2\text{eV}$
- $V_0 = 0.16\text{eV}$
- $m = 9.11 * 10^{-31}\text{kg}$
- $x_0 = 50\text{nm}$
- $L = 200\text{nm}$\

\begin{equation}
\end{equation}

> Figur 2 (not included)

\begin{equation}
\end{equation}

Trinnpotensial i en boks med bredden $L = 200 m$. I området $x < 100nm$ er potensialet $0$, når $x > 100nm$ er er potensialet lik $V_0$. I dette potensialet skal en bølgepakke propagerere mot høyre fra $x = 50nm$ mot potensialtrinnet.\
\
Tips til verdier for $\Delta t$ og $\Delta x$ (Dere må gjerne prøve dere fram med andre verdier også for å se
hvordan dette påvirker simuleringene):

$$\Delta x = 1.5 * 10^{-10}\text{m}$$

$$\Delta t = 2.25 * 10^{-19}\text{s}$$

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
