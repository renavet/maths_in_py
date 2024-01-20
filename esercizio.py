from sommatoria import Sommatoria
from media import media
from coeffienti import numeratore,denominatore_coefficiente
from funzioni import funzione_regressiva,funzione_interpolante_lineare
import matplotlib.pyplot as plt
import numpy as np
x=[25,30,35,40,45,50]
y=[80,93,102,118,132,152]

a=funzione_interpolante_lineare(x,y)
x_m=media(x)
y_m=media(y)
print(f"equazione=>y-{y_m}={a}(x-{x_m})")

# Creating vectors X and Y
X = np.linspace(-2, 2, 100)
Y = a*(X-x_m)+y_m

 
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(X, Y)
 
# Show the plot
plt.savefig('foo.pdf')
