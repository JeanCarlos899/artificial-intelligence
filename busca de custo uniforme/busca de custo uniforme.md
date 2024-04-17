# Busca de custo uniforme

Esse algoritmo é utilizado para encontrar o caminho mais curto entre dois vértices em um grafo. Ele é baseado em uma busca de custo uniforme, ou seja, o algoritmo expande o nó com menor custo de caminho até o momento.

## Problema

Dado o mapa abaixo, utilizando a busca de custo uniforme, faça um algoritmo que encontre o menor caminho de `Arad` a `Bucharest`. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![alt text](<../mapa heurística.png>)

## Implementação da busca de custo uniforme

A implementação da busca de custo uniforme é feita na classe `UniformCostSearch` no arquivo `search.py`. O algoritmo é baseado em uma fila de prioridade, onde o nó com menor custo de caminho é expandido primeiro.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra o menor caminho de `Arad` a `Bucharest` e imprime os nós visitados e a solução do problema.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`.

```bash
python search.py
```

