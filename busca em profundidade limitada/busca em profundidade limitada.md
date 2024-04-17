# Busca em profundidade limitada

Esse algoritmo é utilizado para encontrar um elemento em um grafo. Ele é baseado no algoritmo de busca em profundidade limitada, que começa no nó raiz e explora o máximo possível cada um dos seus ramos antes de retroceder. Isso dentro do limite de uma profundidade máxima. 

## Problema

Dado o mapa abaixo, utilizando a busca em profundidade limitada, faça um algoritmo que encontre um caminho de `Arad` a `Bucharest` com limite 3. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![alt text](<../mapa simples.png>)

## Implementação da busca em profundidade limitada

A implementação é um algoritmo de busca em profundidade `limitada` (Depth-Limited Search, DLS) que explora um grafo até uma profundidade máxima definida pelo usuário. Mantém uma lista de nós a serem explorados (`fronteira`) seguindo LIFO, evitando ciclos e duplicações rastreando estados visitados. Durante a busca, retira nós da fronteira para verificar se o objetivo foi alcançado. Se a profundidade do nó não excede o limite e não há ciclo, seus filhos são adicionados à `fronteira`. O algoritmo retorna estados visitados e, se encontra a solução, o caminho percorrido até o estado final.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra um caminho de `Arad` a `Bucharest` e imprime o caminho percorrido e a solução.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`. Será impresso o caminho de `Arad` a `Bucharest`.

```bash
python search.py
```

