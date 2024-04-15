from problem import Problem

class Node:

    def __init__(self, state, father=None, action=None, cost=0):
        self.state = state
        self.father = father
        self.action = action
        self.cost = cost

    def child_node(self, problem: Problem, action):
        """ Retorna o nó filho """
        next_state = problem.transition(self.state, action)
        # custo=problema.custo(self.custo, self.state, acao, proximo_state))
        next_node = Node(state=next_state, father=self, action=action)
        return next_node

    def explore(self, problem: Problem) -> list['Node']:
        """Retorna todos os filhos"""
        nodes = []
        for action in problem.actions(self.state):
            nodes.append(self.child_node(problem, action))
        return nodes

    def path(self) -> list['Node']:
        """Retorna uma lista nós formando o caminho percorrido"""
        node, reverse_path = self, []
        while node:
            reverse_path.append(node)
            node = node.father
        return list(reversed(reverse_path))

    def solution(self):
        """Retorna uma lista de ações da raiz até o nó"""
        actions = []
        for node in self.path()[1:]:
            actions.append(node.action)
        return actions
