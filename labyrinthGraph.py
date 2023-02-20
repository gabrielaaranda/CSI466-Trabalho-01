
def ConectEdges(grafo,map,i,j):
    #faz as ligações das arestas a esquerda, cima, direira e baixo no mapa 
    
    if i > 0 and map[i-1][j] != "#":
        grafo[(i, j)].append((i-1, j))
    if j > 0 and map[i][j-1] != "#":
        grafo[(i, j)].append((i, j-1))
    if i < len(map)-1 and map[i+1][j] != "#":
        grafo[(i, j)].append((i+1, j))
    if j < len(map[0])-1 and map[i][j+1] != "#":
        grafo[(i, j)].append((i, j+1))
        
    return grafo
                    
def interpretMapToGraph(map):
    grafo = {}

    for i in range(len(map)):
        for j in range(len(map[0])):

            if map[i][j] != "#":
                grafo[(i, j)] = []
                ConectEdges(grafo,map,i,j)
                
    return grafo

def startLabyrinth(map):
    inicio = None

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                inicio = (i, j)

    return inicio

def endLabyrinth(map):
    fim = None

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "E":
                fim = (i, j)

    return fim
            
def readLabyrinth(nomeDoLabirinto):
    map = []
    with open(nomeDoLabirinto) as f:
        for linha in f:
            linha = linha.strip()
            map.append(list(linha))

    grafo = interpretMapToGraph(map)
    inicio = tuple(startLabyrinth(map))
    fim = tuple(endLabyrinth(map))
    caminho = ivyFarejaCaminho(grafo, inicio, fim)

    if caminho is not None:
        print("Caminho até a saída do labirinto: ", caminho)
    else:
        print("Não há um caminho até a saída")

def ivyFarejaCaminho(grafo, s, e):
    desc = set()
    caminho = []
    pilha = [s]

    while len(pilha) != 0:
        u = pilha.pop()

        if u == e:
            caminho.append(u)
            return caminho

        if u not in desc:
            desc.add(u)
            caminho.append(u)

            for v in grafo[u]:
                pilha.append(v)

    return None