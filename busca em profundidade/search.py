from node import Node
from problem import Problem


class DepthFirstSearch:
    def __init__(self, problem: Problem):
        # inicializa o problema, o nó raiz, a fronteira e a lista de nós
        # visitados. A fronteira é uma lista de nós que ainda não foram
        # explorados. A lista de nós visitados é uma lista de nós que já
        # foram explorados. 
        self.problem = problem
        self.root = Node(problem.initial_state)
        self.frontier = [self.root]
        self.reached: list[Node] = []

    def search(self):
        # enquanto houver nós na fronteira...
        while self.frontier:
            # remove o último nó da fronteira - Last In First Out (LIFO). O 
            # último nó adicionado à fronteira é o primeiro a ser removido. Isso 
            # faz com que a busca em profundidade explore um ramo do grafo até
            # que não haja mais nós a serem explorados, e então volte para o nó
            # anterior e explore outro ramo. 
            node = self.frontier.pop()

            # se o estado do nó for o estado final do problema, então o objetivo 
            # foi alcançado
            if problem.objective(node.state):
                self.reached.append(node)
                return node

            # se o nó não foi visitado, então o explora e adiciona seus filhos
            # à fronteira. Isso evita que um nó seja explorado mais de uma vez, 
            # o que poderia causar um loop infinito
            elif node.state not in [node.state for node in self.reached]:
                # adiciona cada filho do nó à fronteira
                for child in node.explore(problem):
                    # caso um nó que já tenha sido explorado seja adicionado à
                    # fronteira, ele até será testado novamente, mas não será
                    # explorado mais uma vez.
                    self.frontier.append(child)

            # adiciona o nó à lista de nós visitados
            self.reached.append(node)

        return None
    
    def visited(self):
        return self.reached


if __name__ == '__main__':
    problem = Problem(initial_state='Arad', final_state='Bucharest')
    depth_first_search = DepthFirstSearch(problem)

    node = depth_first_search.search()
    solution: list[Node] = node.solution()

    print('================================== Nós visitados ==================================')
    for node in depth_first_search.reached:
        print(node.state, end=' -> ' if node.state != problem.final_state else '\n')
        
    print('===================================== Solução =====================================')
    for state in node.solution():
        print(state, end=' -> ' if state != problem.final_state else '\n')
