# Busca em profundidade iterativa

Esse algoritmo é utilizado para encontrar um elemento em um grafo. Ele é baseado no algoritmo de busca em profundidade iterativa, que começa no nó raiz e explora o máximo possível cada um dos seus ramos antes de retroceder. Isso dentro do limite de uma profundidade máxima que é incrementado a cada execução. Se o nó objetivo não for encontrado, a busca é reiniciada com um limite de profundidade maior.

## Problema

Dado o mapa abaixo, utilizando a busca em profundidade iterativa, faça um algoritmo que encontre um caminho de `Arad` a `Bucharest` no menor limite possível. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![alt text](<../mapa simples.png>)

## Implementação da busca em profundidade iterativa

A implementação é um algoritmo de busca em profundidade iterativa (`IDS`) que combina busca em profundidade limitada com incremento **progressivo** de profundidade. A cada iteração, a profundidade de busca é aumentada, iniciando uma nova busca com limite maior até encontrar a solução. A busca em profundidade limitada (`DepthLimitedSearch`) usa uma estratégia LIFO para explorar o grafo até uma profundidade máxima, evitando ciclos com o método `is_cicle`. O algoritmo mantém um registro dos estados visitados a cada profundidade e retorna o nó final quando encontra a solução.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra um caminho de `Arad` a `Bucharest` e imprime o caminho percorrido e a solução.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`. Será impresso o caminho de `Arad` a `Bucharest`.

```bash
python search.py
```

