from problem import Problem

class Node:

    def __init__(self, state, cost, father=None, action=None):
        self.state = state
        self.cost = cost
        self.father = father
        self.action = action

    def child_node(self, problem: Problem, action):
        """ Retorna o nó filho """
        next_state = problem.transition(self.state, action)[0]

        next_node = Node(
            state=next_state, 
            father=self, 
            action=action, 
            cost=problem.cost(self.state, next_state)
        )

        return next_node

    def explore(self, problem: Problem):
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
    
    def total_cost(self):
        """Retorna o custo total do nó raiz até o nó"""
        return sum(node.cost for node in self.path())
