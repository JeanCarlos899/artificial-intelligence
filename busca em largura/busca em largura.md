# Busca em Largura

Esse algoritmo é utilizado para encontrar o caminho mais curto entre dois vértices em um grafo. Ele é baseado em uma busca em largura, que explora todos os vértices vizinhos de um vértice antes de avançar para os próximos vértices.

## Problema

Dado o mapa abaixo, utilizando a busca em largura, faça um algoritmo que encontre o menor caminho de `Arad` a `Bucharest`. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![alt text](<../mapa simples.png>)

## Implementação da busca em largura

A implementação da busca em largura é feita na classe `bread_first_search`, que percorre cada `vértice` do gráfo a partir da `raiz`, removendo-o da fila e verificando se ele é o `vértice` `objetivo`. Caso não seja, ele acidiona os filhos do `vértice` à fila de `vértices` a serem visitados. O algoritmo é interrompido quando o `vértice` `objetivo` é encontrado.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra o menor caminho de `Arad` a `Bucharest` e imprime o caminho percorrido.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`. Será impresso o caminho de `Arad` a `Bucharest`.

```bash
python search.py
```

