
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

    def actions(self, state):
        return self.romania_map[state]

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

    def cost(self, state1, action, state2):
        return 1


if __name__ == '__main__':
    problem = Problem(initial_state='Arad', final_state='Bucharest')
    print(problem.actions('Arad'))
