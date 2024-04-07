# Problema da Mochila com Busca Gulosa

O problema da mochila consiste em preencher uma mochila com objetos de diferentes pesos e valores. O objetivo é maximizar o valor total dos objetos colocados na mochila, sem ultrapassar o peso máximo da mochila e minimizando o desperdício de espaço.

## Componentes da Busca Gulosa

Em geral, o algoritmo guloso para resolver o problema da mochila possui cinco componentes:

1. Um conjunto candidato, a partir do qual é criada uma solução.
2. Uma função de seleção, que escolhe o melhor candidato para ser adicionado à solução.
3. Uma função de viabilidade, que determina se um candidato pode ser usado para contribuir para uma solução.
4. Uma função objetivo, que atribui um valor a uma solução, ou a uma solução parcial.
5. Uma função de solução, que indica quando uma solução completa foi encontrada.

## Implementação

A implementação deste problema envolve a criação de uma classe `Item` para representar os objetos a serem colocados na mochila, e uma classe `BagProblem` que implementa o algoritmo guloso para resolver o problema.

A classe `BagProblem` utiliza os seguintes métodos principais:

* **run():** Executa o algoritmo guloso para preencher a mochila com os itens.
* **select_item():** Seleciona o próximo item a ser adicionado à mochila com base na função de seleção.
* **viability(item):** Verifica se um item pode ser adicionado à mochila sem ultrapassar o peso máximo.
* **goal():** Retorna a porcentagem do peso máximo da mochila que já foi preenchida.
* **is_solution():** Verifica se a solução atual é completa ou o maior valor possível foi alcançado.

## Exemplo de Uso

No exemplo fornecido, uma lista de itens de sobrevivência é criada, e a classe `BagProblem` é instanciada com um peso máximo de mochila de 10kg. A solução é então calculada e exibida, juntamente com algumas métricas relevantes.