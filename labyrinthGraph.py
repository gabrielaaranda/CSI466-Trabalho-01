def ConectEdges(grafo,map,i,j):                         #Faz as ligações dos nós à esquerda, cima, direita e baixo no grafo
    
    if i > 0 and map[i-1][j] != "#":
        grafo[(i, j)].append((i-1, j))                  #Esquerda
    if j > 0 and map[i][j-1] != "#":
        grafo[(i, j)].append((i, j-1))                  #Cima
    if i < len(map)-1 and map[i+1][j] != "#":
        grafo[(i, j)].append((i+1, j))                  #Direita
    if j < len(map[0])-1 and map[i][j+1] != "#":
        grafo[(i, j)].append((i, j+1))                  #Baixo
        
    return grafo
                    
def interpretMapToGraph(map):                           #Cria um grafo com todos os espaços diferentes de #
    grafo = {}

    for i in range(len(map)):
        for j in range(len(map[0])):

            if map[i][j] != "#":
                grafo[(i, j)] = []                      #Cria o nó referente ao i e j do mapa no grafo
                ConectEdges(grafo,map,i,j)              #Chama a função que conecta os nós
                
    return grafo

def startLabyrinth(map):                                #Identifica a entrada do labirinto procurando o "S"
    inicio = None

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                inicio = (i, j)

    return inicio

def endLabyrinth(map):                                  #Identifica a saída do labirinto procurando o "E"
    fim = None

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "E":
                fim = (i, j)

    return fim
            
def readLabyrinth(nomeDoLabirinto):                     #Abre o arquivo do labirinto e lê os caracteres  
    map = []
    with open(nomeDoLabirinto) as file:
        for linha in file:
            linha = linha.strip()                       #Desmembra a linha em seus caracteres
            map.append(list(linha))                     #Coloca os caracteres separadamente no mapa

    grafo = interpretMapToGraph(map)
    inicio = tuple(startLabyrinth(map))
    fim = tuple(endLabyrinth(map))
    caminho = ivyFarejaCaminho(grafo, inicio, fim)      #Chamada da função que retorna o caminho da entrada a saída

    if caminho is not None:
        print("Caminho: ", caminho)   
    else:
        print("Não há um caminho até a saída")

def ivyFarejaCaminho(grafo, s, e):                      #Busca o caminho por DFS
    desc = set()
    caminho = []
    pilha = [s]

    while len(pilha) != 0:                              #Enquanto a pilha não estiver vazia
        u = pilha.pop()                                 #u recebe as informações uma a uma da pilha

        if u == e:                                      #se a u for igual ao final termina o caminho e retorna ele
            caminho.append(u)                           
            return caminho

        if u not in desc:                               #Se u não estiver descoberto, adiciona u nos descobertos e liga u no caminho
            desc.add(u)
            caminho.append(u)

            for v in grafo[u]:                          #Acrescenta o elemento na pilha 
                pilha.append(v)

    return None