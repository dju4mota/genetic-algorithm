import random
import math
from gene import Gene

def printList(lista):
    for d in lista:
        print(d)

def printGeneList(lista):
    for gene in lista:
        print(f" Gene {int(gene.x,base=0) - deltaX}, {int(gene.y,base=0) - deltaY} - Apitdao: {gene.aptidao}")

def printGeneListBinary(lista):
    for gene in lista:
        print(f" Gene {gene.x}, {gene.y} - Apitdao: {gene.aptidao}")

# Função Objetivo ->    f =  x^2 - sin(y pi/3) + y^3  , x = [-20,20] , y = [-40, 40],  -> [0,40] & [0,80]

def funcaoObjetivo(gene):
    
    x = int(gene.x,base=0) - deltaX
    y = int(gene.y,base=0) - deltaY
    
    # return (math.pow(x,2) - math.sin((y * math.pi)/3) + math.pow(y,3))
    return abs(x * y * math.sin((y * math.pi) / 4))
    # return math.pow(x,2) + math.pow(y,2)


# Travando a aleatoriedade para desenvolvimento  
random.seed(42)

# codificação e parametros 
# minX, maxX, deltaX, XtamanhoBinario = -20, 20, 20, 6
# minY, maxY, deltaY, YtamanhoBinario = -40, 40, 40, 7

minX, maxX, deltaX, XtamanhoBinario = 0, 63, 0, 6
minY, maxY, deltaY, YtamanhoBinario = 0, 127, 0, 7
Npopulation = 20 


# Gerar população 
def generatePopulation():
    population = []
    for d in range (0,Npopulation):
        population.append(Gene(random.randint( minX+deltaX, maxX+deltaX ),random.randint( minY+deltaY, maxY+deltaY )))
    return population


# Calcular Apitidão 
def calculateFitness(population):
    for p in population:
        p.aptidao = funcaoObjetivo(p)
    

# Selecionar Reprodutores 
def selectionByTournament(population): 
    
    pais = []
    for d in range (0, len(population)):
            rand1, rand2 = (random.randint(0,len(population)-1)), (random.randint(0,len(population)-1))
            
            if(population[rand1].aptidao > population[rand2].aptidao):
                pais.append(population[rand1])
            else: 
                pais.append(population[rand2])      
            
    return pais


# Crossover 
def generateChildren(pais):

    filhos = []
    for d in range(0,len(pais),2):
        
        pontoDeCorteX = random.randint(0,XtamanhoBinario)+2
        pontoDeCorteY = random.randint(0,YtamanhoBinario)+2
        
        x1 = pais[d].x[0:pontoDeCorteX] + pais[d+1].x[pontoDeCorteX:XtamanhoBinario+2]
        x2 = pais[d+1].x[0:pontoDeCorteX] + pais[d].x[pontoDeCorteX:XtamanhoBinario+2]

        y1 = pais[d].y[0:pontoDeCorteY] + pais[d+1].y[pontoDeCorteY:YtamanhoBinario+2]
        y2 = pais[d+1].y[0:pontoDeCorteY] + pais[d].y[pontoDeCorteY:YtamanhoBinario+2]
        
        filho1 = Gene(0,0)
        filho1.setValores(x=x1, y=y1)
        filho2 = Gene(0,0)
        filho2.setValores(x=x2, y=y2)

        filhos.append(filho1)
        filhos.append(filho2)

    return filhos


# Mutação 
def mutacao(gene):
    posicaoX = random.randint(2,XtamanhoBinario)
    posicaoY = random.randint(2,YtamanhoBinario)

    if(gene.x[posicaoX] == '1'):
        aux = list(gene.x)
        aux[posicaoX] = '0'
        gene.x = "".join(aux)
    else: 
        aux = list(gene.x)
        aux[posicaoX] = '1'
        gene.x = "".join(aux)

    if(gene.y[posicaoY] == '1'):
        aux = list(gene.x)
        aux[posicaoY] = '0'
        gene.x = "".join(aux)
    else: 
        aux = list(gene.y)
        aux[posicaoY] = '1'
        gene.y = "".join(aux)

    return gene


population = generatePopulation()
calculateFitness(population= population)
print("Populacao Inicial:")
printGeneList(population)

for j in range(0,100):    
    
    print(f"\n{j}")
    
    pais = selectionByTournament(population= population)    
    print("Pais")
    printGeneList(pais)
    
    filhos = generateChildren(pais= pais)
    calculateFitness(population= filhos)    
    print("Filhos")
    printGeneList(filhos)

    for d in range(0,len(filhos)):
        if (random.randint(0,1) < 0.005):
            filhos[d] = mutacao(filhos[d])
            funcaoObjetivo(filhos[d])
            print(f"Houve mutacao no {d}!")

    pais.sort(key=lambda gene: gene.aptidao,reverse=True)
    filhos.sort(key=lambda gene: gene.aptidao,reverse= True)
    
    porcentagemElitismo = int(Npopulation *0.1)
    population = pais[0:porcentagemElitismo] + filhos[porcentagemElitismo:Npopulation - porcentagemElitismo]
    
    print("Population")
    calculateFitness(population)
    printGeneList(population)

print("final: ")
calculateFitness(population=population)
population.sort(key=lambda gene: gene.aptidao)
printGeneList(population)