# Busca A*

Esse algoritmo é utilizado para encontrar o caminho mais curto entre dois vértices em um grafo. Ele é baseado em uma busca A*, que explora o grafo de forma inteligente, utilizando uma heurística para priorizar os vértices que estão mais próximos do vértice final.

## Problema

Dado o mapa abaixo, utilizando a busca em largura, faça um algoritmo que encontre o menor caminho de `Arad` a `Bucharest`. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![mapa com heurística](<../mapa heurística.png>)

## Implementação da busca A*

O código implementa o algoritmo de busca A* para resolver um problema de busca. Ele inicializa com um problema específico e utiliza uma fila de prioridade (heapq) para gerenciar os nós visitados. O método `search` realiza a busca enquanto a fila de prioridade não está vazia. Ele remove o nó com a menor prioridade, verifica se é o nó objetivo, e se não for, explora seus filhos e os adiciona à fila de prioridade com base no custo total (`f(n)`) que combina o custo do nó e a heurística. Se encontrar a solução, o método retorna o nó objetivo. O código também fornece uma função `visited` para retornar a lista de nós visitados. Na execução principal, o código inicializa o problema com um estado inicial e final, realiza a busca com `AStarSearch` e imprime os nós visitados e a solução encontrada com seu custo total.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra o menor caminho de `Arad` a `Bucharest` e imprime os nós visitados e a solução do problema.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`.

```bash
python search.py
```

