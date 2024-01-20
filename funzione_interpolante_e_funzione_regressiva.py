import math
import matplotlib.pyplot as plt
import numpy as np

def Sommatoria(array):
    sommatoria = 0
    for i in array:
        i = float(i)
        sommatoria = sommatoria + i
    return sommatoria

def media(array):
    length = len(array)
    sommatoria = Sommatoria(array)
    media = sommatoria / length
    return media

def numeratore(x_array, y_array):
    gamma = []
    for alpha, beta in zip(x_array, y_array):
        alpha = float(alpha)
        beta = float(beta)
        delta = (alpha - media(x_array)) * (beta - media(y_array))
        gamma.append(delta)
    somma = Sommatoria(gamma)
    return somma

def denominatore_coefficiente(x_vel_y_array):
    gamma = []
    for alpha in x_vel_y_array:
        alpha=float(alpha)
        delta = (alpha - float(media(x_vel_y_array)))**2
        gamma.append(delta)
    Denominatore_coefficiente = Sommatoria(gamma)
    return Denominatore_coefficiente

def funzione_interpolante_lineare(x_array, y_array):
    coefficiente_a = numeratore(x_array, y_array) / denominatore_coefficiente(x_array)
    return coefficiente_a

def funzione_regressiva(x_array, y_array):
    coefficiente_b = numeratore(x_array, y_array) / denominatore_coefficiente(y_array)
    return coefficiente_b
