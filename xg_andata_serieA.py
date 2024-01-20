from funzione_interpolante_e_funzione_regressiva import funzione_interpolante_lineare,funzione_regressiva,media
import matplotlib.pyplot as plt
import numpy as np

data = [
    {"№": 1, "Team": "Inter", "W": 16, "G": 49, "xG": 47.52},
    {"№": 2, "Team": "Juventus", "W": 15, "G": 32, "xG": 35.67},
    {"№": 3, "Team": "AC Milan", "W": 13, "G": 38, "xG": 33.35},
    {"№": 4, "Team": "Fiorentina", "W": 10, "G": 29, "xG": 24.93},
    {"№": 5, "Team": "Atalanta", "W": 10, "G": 35, "xG": 33.47},
    {"№": 6, "Team": "Lazio", "W": 10, "G": 24, "xG": 27.30},
    {"№": 7, "Team": "Bologna", "W": 8, "G": 23, "xG": 25.79},
    {"№": 8, "Team": "Napoli", "W": 9, "G": 30, "xG": 37.85},
    {"№": 9, "Team": "Roma", "W": 8, "G": 32, "xG": 30.19},
    {"№": 10, "Team": "Torino", "W": 7, "G": 18, "xG": 21.27},
    {"№": 11, "Team": "Monza", "W": 6, "G": 20, "xG": 25.94},
    {"№": 12, "Team": "Genoa", "W": 5, "G": 20, "xG": 18.17},
    {"№": 13, "Team": "Lecce", "W": 4, "G": 20, "xG": 22.64},
    {"№": 14, "Team": "Sassuolo", "W": 5, "G": 26, "xG": 26.89},
    {"№": 15, "Team": "Frosinone", "W": 5, "G": 25, "xG": 24.09},
    {"№": 16, "Team": "Udinese", "W": 2, "G": 21, "xG": 26.13},
    {"№": 17, "Team": "Cagliari", "W": 4, "G": 19, "xG": 24.64},
    {"№": 18, "Team": "Verona", "W": 4, "G": 18, "xG": 18.72},
    {"№": 19, "Team": "Empoli", "W": 3, "G": 11, "xG": 18.41},
    {"№": 20, "Team": "Salernitana", "W": 2, "G": 17, "xG": 15.74},
]

W=[team["W"]for team in data]
xG=[team["xG"]for team in data]
team_names = [team["Team"] for team in data]

a=funzione_interpolante_lineare(W,xG)
b=funzione_regressiva(W,xG)
X = np.linspace(min(W) - 5, max(W) + 5, 100)
equazione_lineare = a * (X - media(W)) + media(xG)
equaziine_regressiva=b*X+(media(xG)-b*media(W))

fig = plt.figure(figsize=(10, 5))
# Create the plot
plt.plot(X, equazione_lineare, label='funzione Lineare')
plt.plot(X, equaziine_regressiva, label='funzione Regressiva')
plt.scatter(W, xG, color='red', marker='o', label='Dati')
for i, team_name in enumerate(team_names):
    plt.annotate(team_name, (W[i], xG[i]), textcoords="offset points", xytext=(0, 5), ha='center')


# Show the legend
plt.legend()

# Show the plot
plt.savefig('serieA.pdf')
