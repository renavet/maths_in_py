from sommatoria import Sommatoria
from media import media
#dato che numeratore di a e b è uguale andiamo a calcolare prima quello
#numeratore=sommatoria(x-x')(y-y')
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


x=[23, 45, 12, 67, 89]
y=[34, 56, 78, 21, 43]

numeratore(x,y)
denominatore_coefficiente(x)
denominatore_coefficiente(y)
print(denominatore_coefficiente(x))