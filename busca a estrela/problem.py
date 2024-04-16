
class Problem:

    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state
        self.romania_map = {
            'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
            'Zerind': [('Arad', 75), ('Oradea', 71)],
            'Oradea': [('Zerind', 71), ('Sibiu', 151)],
            'Sibiu': [
                ('Arad', 140),
                ('Fagaras', 99),
                ('Oradea', 151),
                ('Rimnicu', 80)
            ],
            'Timisoara': [('Arad', 118), ('Lugoj', 111)],
            'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
            'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
            'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
            'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
            'Rimnicu': [('Craiova', 146), ('Pitesti', 97), ('Sibiu', 80)],
            'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
            'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
            'Bucharest': [
                ('Fagaras', 211),
                ('Pitesti', 101),
                ('Giurgiu', 90),
                ('Urziceni', 85)
            ],
            'Giurgiu': [('Bucharest', 90)],
            'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
            'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
            'Eforie': [('Hirsova', 86)],
            'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
            'Iasi': [('Vaslui', 92), ('Neamt', 87)],
            'Neamt': [('Iasi', 87)]
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
