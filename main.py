from labyrinthGraph import readLabyrinth
import time

caminho = 1

while caminho != '0' :
    caminho = input("Informe o aquivo (0 para sair): ")
    
    if caminho != '0':
        start_time = time.time()
        readLabyrinth(caminho)
        print("\nTempo: ", time.time() - start_time)
    
print("acabou")


