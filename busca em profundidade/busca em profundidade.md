# Busca em profundidade

Esse algoritmo é utilizado para encontrar um elemento em um grafo. Ele é baseado no algoritmo de busca em profundidade, que começa no nó raiz e explora o máximo possível cada um dos seus ramos antes de retroceder.

## Problema

Dado o mapa abaixo, utilizando a busca em profundidade, faça um algoritmo que encontre um caminho de `Arad` a `Bucharest`. O estado inicial é representado pelo círculo verde e o estado final é representado pelo círculo vermelho. 

![alt text](<../mapa heurística.png>)

## Implementação da busca em profundidade

A implementação é um algoritmo de busca em profundidade `(DFS)` que explora um problema a partir de um **estado inicial** até encontrar um **estado final**. O algoritmo mantém uma `fronteira` de nós não explorados e uma `lista de nós visitados`. Ao encontrar o objetivo, ele `retorna` o nó `final` e imprime os estados visitados e a `solução`. A estratégia **LIFO** permite explorar um ramo até o final antes de retroceder e explorar outro.

## Exemplo de uso

No exemplo fornecido, o algoritmo encontra um caminho de `Arad` a `Bucharest` e imprime o caminho percorrido e a solução.

## Como executar

Para testar o algoritmo, execute a partir do arquivo `search.py`. Será impresso o caminho de `Arad` a `Bucharest`.

```bash
python search.py
```

