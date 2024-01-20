from sommatoria import Sommatoria
from media import media
from coeffienti import numeratore,denominatore_coefficiente
def funzione_interpolante_lineare(x_array,y_array):
    coefficiente_a=(numeratore(x_array,y_array)/denominatore_coefficiente(x_array))
    print(coefficiente_a)
    return coefficiente_a
def funzione_regressiva(x_array,y_array):
    denominatore_coefficiente_b=(numeratore(x_array,y_array)/denominatore_coefficiente(y_array))
    print(denominatore_coefficiente_b)
    return denominatore_coefficiente_b

x=[23, 45, 12, 67, 89]
y=[34, 56, 78, 21, 43]
funzione_interpolante_lineare(x,y)
funzione_regressiva(x,y)

