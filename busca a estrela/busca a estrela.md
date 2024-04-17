# Busca A*

Esse algoritmo é utilizado para encontrar o caminho mais curto entre dois vértices em um grafo. Ele é baseado em uma busca A*, que explora o grafo de forma inteligente, utilizando uma heurística para priorizar os vértices que estão mais próximos do vértice final.

## Problema

Dado o mapa abaixo, utilizando a busca em largura, faça um algoritmo que encontre o menor caminho de `Arad` a `Bucharest`. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![alt text](<../mapa heurística.png>)

## Implementação da busca A*

A implementação da busca em largura é feita na classe `AStarSearch` e utiliza a função `search` para encontrar o menor caminho entre dois vértices. A função `search` funciona da seguinte forma:
1. Insere o estado inicial na lista de prioridade;
2. Enquanto a lista de prioridade não estiver vazia, faça:
    1. Remove o nó com menor custo da lista de prioridade;
    2. Adiciona o nó removido na lista de visitados;
    3. Se o nó for o estado final, retorna o nó;
    4. Para cada ação possível a partir do nó, faça:
        1. Calcula o custo do nó filho;
        2. Insere o nó filho na lista de prioridade;
3. retorna `None` se não encontrar o estado final.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra o menor caminho de `Arad` a `Bucharest` e imprime os nós visitados e a solução do problema.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`.

```bash
python search.py
```

