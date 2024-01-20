import math
import matplotlib.pyplot as plt 
import numpy as np 
def Sommatoria(array):
    sommatoria=0
    for i in array:
        i=int(i)
        sommatoria=sommatoria+i
    return sommatoria

def media(array):
    lenght=len(array)
    sommatoria=Sommatoria(array)
    media=sommatoria/lenght
    
    return media

def numeratore(x_array,y_array):
    gamma=[]
    for alpha,beta in zip(x_array,y_array):
        alpha=int(alpha)
        beta=int(beta)
        delta=(alpha-media(x_array))*(beta-media(y_array))
        gamma.append(delta)
    #print(gamma)
    somma=Sommatoria(gamma)
    return somma

def denominatore_coefficiente(x_vel_y_array):
        gamma=[]
        for alpha in x_vel_y_array:
             delta=(alpha-int(media(x_vel_y_array)))
             gamma.append(delta)
        print(gamma)
        Denominatore_coefficiente=(Sommatoria(gamma))**2
        #print(Denominatore_coefficiente)
        return(Denominatore_coefficiente)

def funzione_interpolante_lineare(x_array,y_array):
    coefficiente_a=(numeratore(x_array,y_array)/denominatore_coefficiente(x_array))
    
    return coefficiente_a
def funzione_regressiva(x_array,y_array):
    denominatore_coefficiente_b=(numeratore(x_array,y_array)/denominatore_coefficiente(y_array))
    
    return denominatore_coefficiente_b


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