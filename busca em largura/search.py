
from collections import deque

from node import Node
from problem import Problem


def bread_first_search(problem: Problem):
    # frontier é uma fila de nós - FIFO
    frontier = deque([Node(problem.initial_state)])

    # a fronteira é uma fila de nós, portanto, o algoritmo continua
    # até que a fronteira esteja vazia
    while frontier:     # enquanto houver nós na fronteira...
        # remove o primeiro nó da fronteira e o armazena em node para explorar
        # o estado do nó. 
        node = frontier.popleft() 

        # se o estado do nó for o estado final, então o nó é a solução
        if problem.objective(node.state):
            return node
        
        # se o estado do nó não for o estado final, então a fronteira é
        # estendida com os nós filhos do nó atual.

        # por ser uma fila, os nós filhos são adicionados ao final da fila
        frontier.extend(node.explore(problem))
    return None


if __name__ == '__main__':
    problem = Problem(initial_state='Arad', final_state='Bucharest')

    nodes = bread_first_search(problem).solution()

    for node in nodes:
        print(node, end=' -> ' if node != nodes[-1] else '')
