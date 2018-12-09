#Biblioteca para geracao de numeros aleatorios;
from random import *

#Constantes de altura e largura da matriz
#O ideal eh usar numeros impares, devido a necessidade de 3 casas pelo menos para formar um caminho '#0#'
#Caso sejam usados numeros pares, o programa ira ajustar para impar
MATRIX_W = 15
MATRIX_H = 15

if MATRIX_W % 2 == 0:
    MATRIX_W += 1

if MATRIX_H % 2 == 0:
    MATRIX_H += 1

#Campos importantes para DFS (Depth-First Search)
moves = []
done = False

#Campos uteis para o desenvolvimento lógico
currentX = 1
currentY = 1

x = 0
y = 1

#Matriz do mapa (Um jeito que eu achei de criar um array bidimensional em python - Funciona)
matrix = [['#' for x in range(MATRIX_W)] for y in range(MATRIX_H)]

#-------------------------------------------------------
#Funcao para desenhar o mapa na tela
def print_map():
    for i in range(MATRIX_W):
        for j in range(MATRIX_H):
            print(matrix[j][i], end = ' '),
        print('')

#---------------------------------------------------------
#Direcao aleatoria
def random_direction():
    return randint(0, 3)

#----------------------------------------------------------------------------------------------------------------
#Validacao da nova posicao
def evaluate_pos():
    global currentY #Necessario nao sei porque (Parece que o Python 3 nao deixa usar variavel global em funcao)
    global currentX #Mesma parada
    evaluated = False #Se torna True quando encontra uma direcao possivel
    sort = [False, False, False, False] #Armazena se cada direcao ja foi verificada
    while(not evaluated):
        direction = random_direction() #Armazena um valor de 0 - 3
        while(sort[direction]): #Verifica se essa direcao ja foi avaliada nesse loop, caso sim, gera um outra
            direction = random_direction()
        
        if direction == 0: #Cima
            if (currentY - 2) > 0:
                if matrix[currentX][currentY - 2] == '#': #Verifica se em duas casas na direcao gerada existe uma parede
                    matrix[currentX][currentY - 1] = '0' #Transforma as duas casas em paredes caso entre na condicao
                    matrix[currentX][currentY - 2] = '0' #--
                    currentX = currentX #Armazena a nova posicao em X
                    currentY = currentY - 2 #Armazena a nova posicao em Y
                    moves.append([currentX, currentY]) #Adiciona a nova posicao a lista de movimentos (Sendo usada como uma pilha, ja que Python nao tem pilha)
                    evaluated = True #Como entrou na condicao, o loop pode ser encerrado após o seu fim
        elif direction == 1: #Baixo
            if (currentY + 2) < (MATRIX_H - 1):
                if matrix[currentX][currentY + 2] == '#':
                    matrix[currentX][currentY + 1] = '0'
                    matrix[currentX][currentY + 2] = '0'  ##Mesma coisa Aqui
                    currentX = currentX
                    currentY = currentY + 2
                    moves.append([currentX, currentY])
                    evaluated = True            
        elif direction == 2: #Esquerda
            if (currentX - 2) > 0:
                if matrix[currentX - 2][currentY] == '#':
                    matrix[currentX - 1][currentY] = '0'
                    matrix[currentX - 2][currentY] = '0'  ##Aqui
                    currentX = currentX - 2
                    currentY = currentY
                    moves.append([currentX, currentY])
                    evaluated = True 
        elif direction == 3: #Direita
            if (currentX + 2) < (MATRIX_W - 1):
                if matrix[currentX + 2][currentY] == '#':
                    matrix[currentX + 1][currentY] = '0'
                    matrix[currentX + 2][currentY] = '0'  ##E aqui
                    currentX = currentX + 2
                    currentY = currentY
                    moves.append([currentX, currentY])
                    evaluated = True
        sort[direction] = True #Marca essa posicao como ja verificada no loop
        allVerified = True #Auxiliar para saber se todas as direcoes ja foram verificadas
        for i in range(0, 3): #Passando pelas 4 direcoes
            if sort[i] == False: #Se pelo menos uma delas nao foi verificada, entao ainda ha possibilidades a serem analisadas(Isso sera usado apenas caso ->
                allVerified = False                                                                 #-> a condicao de fim de loop nao seja satisfeita (evaluated = True)

        if allVerified: #Se tudo foi verificado o loop pode ser encerrado - Aqui aind anao foi verificado se esta validado ou nao
            break

    if not evaluated: #Ja fora do loop, caso nao tenha sido validada nenhuma posicao, significa que foi encontrado um end-point
        moves.pop() #Remove a ultima insercao na lista/pilha de movimentos.
        position = moves.pop() #Armazena a atual ultima posicao (Depois de remover o end-point da anterior)
        currentX = position[x] #Armazena a posicao atual em X
        currentY = position[y] #Armazena a posicao atual em Y
        if len(moves) == 0: #Se a lista/pilha de movimentos nao tem mais nenhum elemento, significa que nao existem mais casas que podem se tornar caminho ->
            return True;                                                                              #-> (Fim do programa)
        moves.append([currentX, currentY])

    return False #Retorna False, caso ainda existam casa possiveis a serem populadas.
#-------------------------------------------------------------------------------------

#Configura a posicao inicial como I
matrix[currentX][currentY] = 'I'

#Adiciona a posicao atual a lista de movimentos.
moves.append([currentX, currentY])

while(not done): #Enquanto evaluate_pos nao retornar True, ela sera chamada sequencialmente.
    done = evaluate_pos()

#Após o procedimento, configura a posicao final como F
matrix[MATRIX_W - 2][MATRIX_H - 2] = 'F'

print_map() #Ao fim do programa o mapa sera exibido
