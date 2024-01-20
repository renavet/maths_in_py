from funzione_interpolante_e_funzione_regressiva import funzione_interpolante_lineare,funzione_regressiva,media
import matplotlib.pyplot as plt
import numpy as np


#########esempio d'uso######################################################
x = [25, 30, 35, 40, 45, 50]
y = [80, 93, 102, 118, 132, 152]

a = funzione_interpolante_lineare(x, y)
b = funzione_regressiva(x, y)

x_m = media(x)
y_m = media(y)

print(f"equazione lineare => y - {y_m} = {a}(x - {x_m})")
print(f"equazione regressiva => y = {b}x + {y_m - b * x_m}")

# Creating vectors X and Y
X = np.linspace(min(x) - 5, max(x) + 5, 100)
equazione_lineare = a * (X - x_m) + y_m
equaziine_regressiva=b*X+(y_m-b*x_m)

fig = plt.figure(figsize=(10, 5))
# Create the plot
plt.plot(X, equazione_lineare, label='funzione Lineare')
plt.plot(X, equaziine_regressiva, label='funzione Regressiva')
plt.scatter(x, y, color='red', marker='o', label='Dati')

# Show the legend
plt.legend()

# Show the plot
plt.savefig('foo.pdf')
