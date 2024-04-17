# Busca de custo uniforme

Esse algoritmo é utilizado para encontrar o caminho mais curto entre dois vértices em um grafo. Ele é baseado em uma busca de custo uniforme, ou seja, o algoritmo expande o nó com menor custo de caminho até o momento.

## Problema

Dado o mapa abaixo, utilizando a busca de custo uniforme, faça um algoritmo que encontre o menor caminho de `Arad` a `Bucharest`. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![mapa simples](<../mapa simples.png>)

## Implementação da busca de custo uniforme

Este código implementa o algoritmo de Busca de Custo Uniforme, uma abordagem de busca que explora nós com base no custo total acumulado até eles. A busca utiliza uma fila de prioridade (`frontier`) para manter os nós a serem explorados, ordenados pelo custo total.

A busca começa com o nó inicial (`root`) com custo zero. Em cada iteração, o nó com menor custo total é retirado da fila. Se o estado desse nó é o objetivo, a busca termina e o nó é retornado.

Caso contrário, os estados dos filhos do nó atual são verificados. Se um estado filho não foi explorado, ele é adicionado à fila com seu custo total acumulado.

Se a busca terminar sem encontrar o objetivo, `None` é retornado. O código também imprime os estados explorados e a solução encontrada com seu custo total.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra o menor caminho de `Arad` a `Bucharest` e imprime os nós visitados, solução do problema e seu custo.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`.

```bash
python search.py
```

