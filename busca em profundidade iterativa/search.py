from node import Node
from problem import Problem


class DepthLimitedSearch:
    def __init__(self, problem: Problem, limit: int):
        # inicializa o problema, o nó raiz, a fronteira e a lista de nós
        # visitados. A fronteira é uma lista de nós que ainda não foram
        # explorados. A lista de nós visitados é uma lista de nós que já
        # foram explorados.
        self.problem = problem
        self.limit = limit
        self.root = Node(problem.initial_state)
        self.frontier = [self.root]
        self.explored: list = []

    def is_cicle(self, node: Node):
        # inicializa um conjunto para armazenar os estados encontrados no
        # caminho do nó atual até o nó raiz
        visited_states = set()

        # percorre o caminho do nó atual até o nó raiz
        while node:
            # se o estado do nó já foi encontrado no caminho, há um ciclo
            if node.state in visited_states:
                return True
            # adiciona o estado do nó ao conjunto de estados visitados
            visited_states.add(node.state)
            # move para o próximo nó (pai)
            node = node.father
        # se não houver ciclo, retorna False
        return False

    def search(self) -> Node:
        # enquanto houver nós na fronteira...
        while self.frontier:
            # remove o último nó da fronteira - Last In First Out (LIFO). O
            # último nó adicionado à fronteira é o primeiro a ser removido. Isso
            # faz com que a busca em profundidade explore um ramo do grafo até
            # que não haja mais nós a serem explorados, e então volte para o nó
            # anterior e explore outro ramo.
            node = self.frontier.pop()

            depth = self.depth(node)
            if depth > self.limit:
                continue

            # se o estado do nó for o estado final do problema, então o objetivo
            # foi alcançado
            if problem.objective(node.state):
                self.explored.append(node.state)
                return node

            # se a profundida do nó não for igual ao limite e não for um ciclo,
            # então o nó pode ser explorado. O método explore() retorna uma
            # lista de nós filhos do nó atual
            if depth != self.limit and not self.is_cicle(node):
                for child in node.explore(problem):
                    # os filhos do nó também podem causar ciclos, então é
                    # necessário verificar se o filho é um ciclo
                    if not self.is_cicle(child):
                        # adiciona o filho à fronteira
                        self.frontier.append(child)

            # adiciona o nó à lista de nós visitados
            self.explored.append(node.state)

        return None

    def depth(self, node: Node):
        depth = 0
        while node.father:
            node = node.father
            depth += 1
        return depth

    def __str__(self) -> str:
        explored_states = ''
        for state in self.explored:
            explored_states += f'{state} -> '
        return explored_states[:-4]


class IterativeDeepeningSearch:
    def __init__(self, problem: Problem):
        self.problem = problem
        self.depth = 0
        self.explored = {}

    def search(self) -> Node:
        # enquanto não retornar um nó...
        while True:
            # cria uma busca em profundidade limitada com a profundidade atual
            self.depth_limited_search = DepthLimitedSearch(
                self.problem, self.depth)
            # realiza a busca em profundidade limitada
            node = self.depth_limited_search.search()
            # se o nó for diferente de None, então o objetivo foi alcançado
            if node:
                # adiciona a lista de nós visitados à lista de nós visitados
                # por profundidade
                self.explored[self.depth] = self.depth_limited_search.__str__()
                # retorna o nó
                return node
            # adiciona a lista de nós visitados à lista de nós visitados por
            # profundidade
            self.explored[self.depth] = self.depth_limited_search.__str__()
            # incrementa a profundidade
            self.depth += 1

    def __str__(self) -> str:
        explored_states = ''
        for depth, states in self.explored.items():
            explored_states += f'Profundidade [{depth}]: {states}\n'
        return explored_states


if __name__ == '__main__':
    problem = Problem(initial_state='Arad', final_state='Bucharest')
    iterative_deepening_search = IterativeDeepeningSearch(problem)

    node = iterative_deepening_search.search()
    solution: list[Node] = node.solution()

    print('================================ Estados visitados ================================')
    print(iterative_deepening_search)

    print('===================================== Solução =====================================')
    for state in solution:
        print(state, end=' -> ' if state != problem.final_state else '\n')
