import matplotlib.pyplot as plt

def relativa(x,prob):
    plt.bar(x, prob)
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia relativa')
    plt.title('Histograma de Frecuencias Relativa')
    plt.show()

def absoluta(x,y):
    plt.bar(x,y, color="green")
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia observada')
    plt.title('Histograma de Frecuencias Absolutas')
    plt.show()

def distribucion(x,fun,title):
    plt.bar(x, fun,color='red')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia absoluta')
    plt.title(title)
    plt.show()

def comparacion(x,prob,fun,label,title):
    plt.bar(x, prob, alpha=0.4, color='yellow', label="Densidad Relativa")
    plt.bar(x,fun, alpha=0.4, color='cyan', label=label)
    plt.xlabel('Valores')
    plt.ylabel('Densidad')
    plt.title(title)
    plt.legend()
    plt.show()