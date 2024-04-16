from node import Node
from problem import Problem
import heapq
import os

class GreedySearch:
    def __init__(self, problem: Problem) -> Node:
        # a busca gulosa escolhe o nó com a menor heurística, ou seja, a menor
        # distância até o nó objetivo. Para isso, utilizo uma fila de prioridade
        # para ordenar os nós a serem visitados
        self.problem = problem
        self.priority_queue = []
        self.visited_nodes = []

    def search(self) -> Node:

        # inicialmente insiro o nó raiz com a prioridade 0 (que é a maior) e o
        # custo 0, pois é o nó raiz
        heapq.heappush(
            self.priority_queue, (0, Node(state=problem.initial_state, cost=0))
        )

        # enquanto a fila de prioridade não estiver vazia...
        while self.priority_queue:
            # recebo o nó com a maior prioridade e o removo da fila de
            # prioridade
            node: Node = heapq.heappop(self.priority_queue)[1]
            # adiciono o nó visitado na lista de nós visitados para imprimir ao
            # final os nós visitados na busca, para fins de visualização
            self.visited_nodes.append(node)

            # se o nó atual for o nó objetivo, retorno o nó
            if problem.objective(node.state):
                return node

            # lista de filhos do nó atual
            children: list[Node] = node.explore(problem)
            # percorro a lista e insiro os filhos na fila de prioridade
            for child in children:
                # custo da heuristica que foi definida no problema
                heuristic = problem.heuristic(child.state)
                # insiro o nó na fila de prioridade o valor da heurística e o nó
                # filho
                heapq.heappush(self.priority_queue, (heuristic, child))

        # retorna None se não encontrar solução
        return None

    def visited(self) -> list[Node]:
        return self.visited_nodes


if __name__ == '__main__':
    os.system('cls')

    problem = Problem(initial_state='Arad', final_state='Bucharest')

    a_star_search = GreedySearch(problem)
    node = a_star_search.search()

    print('====================== Nós visitados ======================')
    for node in a_star_search.visited():
        print(
            node.state, end=' -> ' if node.state !=
            problem.final_state else '\n')

    print('========================= Solução =========================')
    for state in node.solution():
        print(state, end=' -> ' if state != problem.final_state else '\n')
