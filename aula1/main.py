import matplotlib.pyplot as plt

# f(x) = (X**2) - 2x-3 - Função usada como exemplo para o calculo das raizes
# delta = (b**2) -4 * a * c -  Delta em função de X 
# X1 = (-b + delta **(1/2))/2*a - Formula de achar as riazes da função

def trueRoots():

    Delta = (2**2) - 4 * 1 * (-3)

    X1 =  (-2 + Delta **(1/2)) /2*1
    X2 =  (-2 - Delta **(1/2)) /2*1

    return X1,X2

def generateGraphs(X1,X2):
    XBar = [1,2,3,4,5,6,7,8,9,10]
    YBar = [1,2,3,4,5,6,7,8,9,10]

    plt.plot(X1,X2)
    return plt.show()



if __name__ == '__main__':
    print(trueRoots())
    generateGraphs(trueRoots())
