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
        self.reached: list = []

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
                self.reached.append(node.state)
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
            self.reached.append(node.state)

        return None

    def depth(self, node: Node):
        depth = 0
        while node.father:
            node = node.father
            depth += 1
        return depth

    def visited(self):
        return self.reached


if __name__ == '__main__':
    problem = Problem(initial_state='Arad', final_state='Bucharest')
    depth_first_search = DepthLimitedSearch(problem, 3)

    node = depth_first_search.search()

    print('================================== Nós visitados ==================================')
    for visited in depth_first_search.visited():
        print(visited, end=' -> ' if visited != problem.final_state else '\n')

    if not node:
        print('\n===================================== Solução =====================================')
        print('Não foi possível encontrar uma solução para o limite especificado.')
    else:
        print('===================================== Solução =====================================')
        for state in node.solution():
            print(state, end=' -> ' if state != problem.final_state else '\n')

        solution: list[Node] = node.solution()
