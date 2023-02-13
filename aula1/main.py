import matplotlib.pyplot as plt

# f(x) = (X**2) - 2x-3 - Função usada como exemplo para o calculo das raizes
# delta = (b**2) -4 * a * c -  Delta em função de X 
# X1 = (-b + delta **(1/2))/2*a - Formula de achar as riazes da função

def trueRoots():

    Delta = (2**2) - 4 * 1 * (-3)

    X1 =  (-2 + Delta **(1/2)) /2*1
    X2 =  (-2 - Delta **(1/2)) /2*1

    ValoresDeX1 = []
    ValoresDex2 = []

    for i in range(-10,10,1):
        ValoresDeX1.append(X1)
        ValoresDex2.append(X2)

    return ValoresDeX1,ValoresDex2

def generateGraphs(EixoX,EixoY):
    fig,ax = plt.subplots()
    ax.plot([EixoX,EixoY])
    plt.xlim(-1,10)
    plt.ylim(-1,10)
    showgraph = plt.show()
    return showgraph


if __name__ == '__main__':
    print(trueRoots())
    generateGraphs(trueRoots.ValoresDeX1,trueRoots.ValoresDex2)
