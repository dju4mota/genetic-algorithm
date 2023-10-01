import random
import math
from gene import Gene

def printList(lista):
    for d in lista:
        print(d)

def printGeneList(lista):
    for gene in lista:
        print(f" Gene {int(gene.x,base=0) - deltaX}, {int(gene.y,base=0) - deltaY} - Apitdao: {funcaoObjetivo(gene)}")


# Função Objetivo ->    f =  x^2 - sin(y pi/3) + y^3  , x = [-20,20] , y = [-40, 40], 

def funcaoObjetivo(gene):
    
    x = int(gene.x,base=0) - deltaX
    y = int(gene.y,base=0) - deltaY
    
    return (math.pow(x,2) - math.sin((y * math.pi)/3) + math.pow(y,3))


# Travando a aleatoriedade para desenvolvimento  
random.seed(42)


# codificação e parametros 
minX, maxX, deltaX = -20, 20, 20
minY, maxY, deltaY = -40, 40, 40
Npopulation = 10 


# Gerar população 
def generatePopulation():
    population = []
    for d in range (0,Npopulation):
        population.append(Gene(random.randint( minX+deltaX, maxX+deltaX ),random.randint( minY+deltaY, maxY+deltaY )))
    return population


pop = generatePopulation()

# Calcular Apitidão 
def calculateFitness(population):
    for p in population:
        funcaoObjetivo(p)
    

calculateFitness(pop)

# Selecionar Reprodutores 

def selectionByTournament(population): 
    
    # separando em duas listas
    aux1 = []
    aux2 = [] 
    pais = []
    for d in range (0, len(population)):
            rand1, rand2 = (random.randint(0,len(population)-1)), (random.randint(0,len(population)-1))
            print(f"r1 {rand1} r2 {rand2}")
            
            aux1.append(population[rand1])
            aux2.append(population[rand2])
            if(funcaoObjetivo(population[rand1]) > funcaoObjetivo(population[rand2])):
                pais.append(population[rand1])
            else: 
                pais.append(population[rand2])
            
            

    return pais,aux1, aux2

    # confronto




pais1, aux1, aux2 = selectionByTournament(pop)    



printGeneList(pop)
print("pais:")
printGeneList(pais1)
print("aux1:")
printGeneList(aux1)
print("aux2:")
printGeneList(aux2)


# Mutação 

# Apitdiao de cada individuo 

# Gera nova população 

# Teste da função 

