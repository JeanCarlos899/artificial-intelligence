################################################################################

# Desenvolvido por Jean Carlos Rodrigues Sousa, técnico em informática para
# internet e graduando em Análise e Desenvolvimento de Sistemas.

# Disciplina de Inteligência Artificial, ministrada pelo professor Dr. Rafael
# Torres Anchiêta.

############################ Problemática ######################################

# Preencher uma mochila com objetos de diferentes pesos e valores. Deve-se
# preencher a mochila com o maior valor possível, não ultrapassando o peso
# máximo, minimizando o desperdício de espaço.

# Deve ser utilizado a busca gulosa para implementação do problema.

######################## Componentes da busca gulosa ###########################

# Em geral o algoritmo guloso tem cinco componentes[1]:

# 1. Um conjunto candidato, a partir do qual é criada uma solução.
# 2. Uma função de seleção, que selecciona o melhor candidato para ser
#    adicionado à solução.
# 3. Uma função de viabilidade, que é usada para determinar se um candidato
#    pode ser utilizado para contribuir para uma solução.
# 4. Uma função objetivo, que atribui um valor a uma solução, ou uma solução
#    parcial.
# 5. Uma função de solução, que irá indicar quando tivermos descoberto uma
#    solução completa.

# Fonte: https://pt.wikipedia.org/wiki/Algoritmo_guloso

############################# Implementação ####################################

class Item:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight


class BagProblem:
    def __init__(self, items: list[Item], maximum_bag_weight: float) -> list:
        self.items: list[Item] = items
        self.maximum_bag_weight: float = maximum_bag_weight
        self.solution: list[Item] = []

    def run(self):
        while not self.is_solution():
            item = self.select_item()

            if self.viability(item=item):
                # adiciona o item a lista de itens da solução e remove da lista
                # de itens disponíveis.

                self.solution.append(item)
                self.items.remove(item)
                continue
        
            # remove o item da lista de itens, caso não seja viável.
            self.items.remove(item)


        return self.solution

    def select_item(self):
        selected = None

        for item in self.items:
            if selected == None:
                selected = item
            elif item.weight > selected.weight:
                selected = item

        return selected

    def viability(self, item: Item):
        # se a somatória do peso da bolsa somado ao peso do item for menor
        # que o peso máximo da bolsa, retorna verdadeiro.

        if (self.sum_of_solution_items() + item.weight) <= self.maximum_bag_weight:
            return True

        return False

    def goal(self):
        # retorna quantos porcento a solução atual representa do peso máximo da
        # bolsa.

        return (self.sum_of_solution_items() / self.maximum_bag_weight) * 100

    def is_solution(self):

        # se a somatória do peso dos itens da bolsa for igual ao peso máximo da
        # bolsa, retorna verdadeiro. Porém surgem os caso em que a bolsa não
        # pode mais ser preenchida, pois não há mais itens de tamanho compatível
        # ou simplesmente não existem mais itens.

        if (
            self.sum_of_solution_items() == self.maximum_bag_weight
            or not self.items
        ):
            return self.solution

        # verifica se não há mais itens viáveis para serem adicionados a bolsa.
        elif all(not self.viability(item) for item in self.items):
            return self.solution

        return False

    def sum_of_solution_items(self):
        value = 0
        for item in self.solution:
            value += item.weight

        return value


if __name__ == "__main__":

    # itens ilustrativos para o problema da mochila, pesando o total de 25kg.

    items = [
        Item("Garrafa térmica", 2.0),
        Item("Cantil de água", 1.0),
        Item("Panela de camping", 3.0),
        Item("Barraca para acampamento", 2.5),
        Item("Roupas de frio", 2.0),
        Item("Kit de primeiros socorros", 3.0),
        Item("Lanterna com baterias", 2.5),
        Item("Saco de dormir", 4.0),
        Item("Ferramenta multifuncional", 1.5),
        Item("Machado", 3.5),
    ]

    bag_problem = BagProblem(items=items, maximum_bag_weight=10)
    
    solution = bag_problem.run()

    print("---------- Itens na mochila ----------\n")
    for item in solution:
        print(f"{item.name} - {item.weight}kg")

    print()
    print("-------------- Métricas --------------\n")
    print(f"Peso máximo da bolsa: {bag_problem.maximum_bag_weight}kg")
    print()
    print(f"Total de itens na bolsa: {len(solution)}")
    print(f"Total: {bag_problem.sum_of_solution_items()}kg")
    print(f"{bag_problem.goal():.2f}% do objetivo alcançado.")
