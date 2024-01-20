import matplotlib.pyplot as plt
import numpy as np
import funzione_interpolante_e_funzione_regressiva as f

# Array for the column 'xG'
xG = ['0.15', '0.03', '0.15', '0.07', '0.08', '0.48', '0.88', '0.00', '0.11', '0.13', '0.30', '0.00', '0.01', '0.11', '0.21', '0.12', '0.61', '0.03']
npxg = np.array([float(element) for element in xG])
# Array for the column 'Sh'
Sh = ['3', '1', '2', '1', '2', '1', '4', '0', '2', '2', '1', '0', '1', '2', '2', '2', '4', '1']

# Array for the column 'G'
G = ['0', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '2', '0']

a_GSh = f.funzione_interpolante_lineare(G, Sh)
a_xGSh = f.funzione_interpolante_lineare(npxg, Sh)

G_m = f.media(G)
Sh_m = f.media(Sh)
xG_m=f.media(xG)



# Creating vectors X and Y
X = np.linspace(min(npxg) - 5, max(npxg) + 5, 100)
equazione_lineare_GSh = a_GSh * (X - G_m) + Sh_m
equazione_lineare_xGSh = a_xGSh * (X - xG_m) + Sh_m

fig = plt.figure(figsize=(10, 5))
# Create the plot
plt.plot(X, equazione_lineare_GSh, label='funzione Lineare Goal/Shots')
plt.plot(X, equazione_lineare_xGSh, label='funzione Lineare xGoal/Shots')
plt.scatter(G, Sh, color='red', marker='o', label='Goal/Shots')
plt.scatter(npxg, Sh, color='blue', marker='o', label='xGoal/Shots')
# Show the legend
plt.legend()

# Show the plot
plt.savefig('gudmunson.pdf')