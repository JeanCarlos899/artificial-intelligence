import heapq
from node import Node
from problem import Problem


class UniformCostSearch:
    def __init__(self, problem: Problem) -> None:
        self.problem = problem
        # Cria uma fila de prioridade para a borda (a fila é ordenada pelo custo total)
        self.frontier = []
        self.root = Node(state=problem.initial_state, cost=0)
        self.explored = []

    def search(self) -> Node:
        # Insere o nó inicial na fila de prioridade com custo total zero
        heapq.heappush(self.frontier, (self.root.total_cost(), self.root))

        # Conjunto para verificar nós explorados e evitar ciclos

        # Loop principal
        while self.frontier:
            # Remove o nó com menor custo total da fila de prioridade
            _, node = heapq.heappop(self.frontier)

            # Verifica se o estado atual é o objetivo
            if self.problem.objective(node.state):
                self.explored.append(node.state)
                # Retorna o nó objetivo encontrado
                return node

            # Marca o estado atual como explorado
            if node.state not in self.explored:
                self.explored.append(node.state)

            # Expande o nó atual para gerar seus filhos
            children = node.explore(self.problem)

            # Itera pelos nós filhos
            for child in children:
                # Verifica se o estado do filho já foi explorado
                if child.state not in self.explored:
                    # Calcula o custo total acumulado até o filho
                    total_cost = child.total_cost()

                    # Adiciona o filho à fila de prioridade com seu custo total acumulado
                    heapq.heappush(self.frontier, (total_cost, child))

        # Se o loop terminar sem encontrar o objetivo, retorna None
        return None

    def __str__(self) -> str:
        explored_states = ''
        for state in self.explored:
            explored_states += f'{state} -> '
        return explored_states[:-4]


if __name__ == '__main__':
    problem = Problem(initial_state='Arad', final_state='Bucharest')
    uniform_cost_search = UniformCostSearch(problem)
    node = uniform_cost_search.search()

    print('================================== Nós visitados ==================================')
    print(uniform_cost_search)

    print('===================================== Solução =====================================')
    for state, _ in node.solution():
        print(state, end=' -> ' if state != problem.final_state else '\n')
    print(f'Custo total: {node.total_cost()}')
