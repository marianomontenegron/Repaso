import matplotlib.pyplot as plt
import math
import numpy as np


def ejercicio_6():

    x = np.arange(-10,10,0.1)
    y_1 = np.sin(x) / x
    y_2 = np.sin(x) * np.e ** (-x)

    plt.title("Gráficas")
    plt.grid()
    plt.axhline(0)
    plt.axvline(0)
    plt.plot(x,y_1)
    plt.plot(x,y_2)
    plt.show()