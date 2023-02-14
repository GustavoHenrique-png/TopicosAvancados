import matplotlib.pyplot as plt

# f(x) = (X**2) - 2x-3 - Função usada como exemplo para o calculo das raizes
# delta = (b**2) -4 * a * c -  Delta em função de X 
# X1 = (-b + delta **(1/2))/2*a - Formula de achar as riazes da função

def trueRoots():

    Delta = (2**2) - 4 * 1 * (-3)

    X1 =  (-2 + Delta **(1/2)) /2*1
    X2 =  (-2 - Delta **(1/2)) /2*1

    #Criando listas vazias para alimentar o gráfico
    AxleX = []
    AxleY = []

    #populando as lista com os resultados de y em função de x e de 1 em 1 até 10
    for x in range(-10,10,1):
        AxleX.append(x)
        AxleY.append((x**2)+(2*x) - 3)

    #Construindo o gráfico com as informações
    fig,ax = plt.subplots()
    ax.plot(AxleX, AxleY)
    plt.xlim(-1,10)
    plt.ylim(-1,10)
    showgraph = plt.show()
    return showgraph

if __name__ == '__main__':
    trueRoots()
   
