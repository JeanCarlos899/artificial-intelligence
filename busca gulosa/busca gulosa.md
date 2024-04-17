# Busca Gulosa

Esse algoritmo é utilizado para encontrar o caminho mais curto entre dois vértices em um grafo. Ele é baseado no algoritmo de busca gulosa, que escolhe o caminho que parece ser o melhor de acordo com uma heurística.

## Problema

Dado o mapa abaixo, utilizando a busca gulosa, faça um algoritmo que encontre o melhor caminho de `Arad` a `Bucharest`. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![alt text](<../mapa heurística.png>)

## Implementação da busca gulosa

A implementação é um algoritmo de busca gulosa que utiliza uma `fila de prioridade` para explorar um problema com base em uma função heurística que estima a distância até o objetivo. O algoritmo começa inserindo o nó raiz na fila com custo zero. Em cada iteração, o nó com a `menor heurística` é removido e, se for o objetivo, é `retornado`. Os filhos do nó atual são gerados e inseridos na fila de prioridade com base na `heurística`. O algoritmo mantém uma lista de nós visitados para visualização. Se a busca não encontra uma solução, retorna None.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra o melhor caminho de `Arad` a `Bucharest` e imprime os nós visitados e a solução do problema.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`.

```bash
python search.py
```

