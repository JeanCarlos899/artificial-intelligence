
class Problem:

    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state
        self.romania_map = {
            'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
            'Zerind': ['Arad', 'Oradea'],
            'Oradea': ['Zerind', 'Sibiu'],
            'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
            'Timisoara': ['Arad', 'Lugoj'],
            'Lugoj': ['Timisoara', 'Mehadia'],
            'Mehadia': ['Lugoj', 'Drobeta'],
            'Drobeta': ['Mehadia', 'Craiova'],
            'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
            'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
            'Fagaras': ['Sibiu', 'Bucharest'],
            'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
            'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
            'Giurgiu': ['Bucharest'],
            'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
            'Hirsova': ['Urziceni', 'Eforie'],
            'Eforie': ['Hirsova'],
            'Vaslui': ['Iasi', 'Urziceni'],
            'Iasi': ['Vaslui', 'Neamt'],
            'Neamt': ['Iasi']
        }
        self.heuristics = {
            'Arad': 366,
            'Bucharest': 0,
            'Craiova': 160,
            'Drobeta': 242,
            'Eforie': 161,
            'Fagaras': 176,
            'Giurgiu': 77,
            'Hirsova': 151,
            'Iasi': 226,
            'Lugoj': 244,
            'Mehadia': 241,
            'Neamt': 234,
            'Oradea': 380,
            'Pitesti': 100,
            'Rimnicu': 193,
            'Sibiu': 253,
            'Timisoara': 329,
            'Urziceni': 80,
            'Vaslui': 199,
            'Zerind': 374
        }

    def actions(self, state):
        return self.romania_map[state]

    def heuristic(self, state):
        return self.heuristics[state]

    def transition(self, state, action):
        # a transição de Arad para Sibiu é Sibiu, optei por deixar dessa maneira
        # para não deixar a variável do estado atual sem uso. Mas poderia ser
        # feito da seguinte maneira: return action

        actions = self.actions(state)
        if action in actions:
            return action

    def objective(self, state):
        # a função de objetivo testa se o estado atual é o estado final.
        # portanto, se o estado atual for igual ao estado final, a função
        # retorna True

        return state == self.final_state

    def cost(self, state, next_state):
        # a função do custo percorre o dicionário de estados e custos para
        # encontrar o custo da aresta entre os estados

        for action, cost in self.actions(state):
            if next_state == action:
                return cost


if __name__ == '__main__':
    problem = Problem(initial_state='Arad', final_state='Bucharest')

    from node import Node
    # print(problem.actions('Arad'))
    # print(problem.heuristic('Arad'))
    # print(problem.cost('Arad', 'Sibiu'))
