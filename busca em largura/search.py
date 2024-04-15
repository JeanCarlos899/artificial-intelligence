
from collections import deque

from node import Node
from problem import Problem


class BreadFirstSearch:
    def __init__(self, problem: Problem):
        self.problem = problem
        self.sorce = Node(problem.initial_state)
        self.frontier = deque([self.sorce])
        self.reached = [self.sorce]

    def search(self):
        # se o estado inicial é o objetivo, retorna o nó raiz
        if self.problem.objective(self.problem.initial_state):
            return Node(self.problem.initial_state)

        # enquanto a fronteria não estiver vazia
        while self.frontier:
            # recebe o primeiro nó da fila (FIFO) e o remove
            node = self.frontier.popleft()

            # percorrido cada filho do nó
            for child in node.explore(problem):
                # recebendo o estado do filho
                state = child.state
                # verifico se o estado é o objetivo
                if problem.objective(state):
                    # adiciono o nó na lista de nós visitados
                    self.reached.append(child)
                    # caso seja, retorno o nó
                    return child

                # verifico se o estado já foi visitado
                if state not in [node.state for node in self.reached]:
                    self.frontier.append(child)
                    self.reached.append(child)

                # modifiquei a implementação que o professor fez em sala para ficar
                # mais parecida com a implementação da busca em largura que tinha no
                # search.md. Notei que faltava salvar os nós visitados, o que
                # causava uma performance ruim.

        # em último caso, retorna None indicando que não foi encontrado o objetivo
        return None


if __name__ == '__main__':
    problem = Problem(initial_state='Arad', final_state='Bucharest')
    breadth_first_search = BreadFirstSearch(problem)

    node = breadth_first_search.search()
    solution = node.solution()

    print('-------------- Nós percorridos --------------')
    for node in breadth_first_search.reached:
        print(node.state, end=' -> ' if node.state !=
              problem.final_state else '\n')

    print('------------------ Solução ------------------')
    for node in solution:
        print(node, end=' -> ' if node != problem.final_state else '')
