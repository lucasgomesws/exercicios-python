# Exercícios de Python — 1º Semestre (ADS)

Repositório com exercícios práticos de Python desenvolvidos durante o primeiro semestre do curso de Análise e Desenvolvimento de Sistemas.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `01-fundamentos-io/` | Entrada/saída, conversão de tipos, operações aritméticas básicas |
| `02-condicionais/` | `if` / `elif` / `else`, condicionais aninhadas |
| `03-lacos-for-while/` | `for`, `while`, `break`, `continue`, tratamento de exceções em loops |
| `04-funcoes-estruturas-dados/` | Funções, dicionários, tuplas |
| `05-pygame/` | Loop de jogo, eventos, input de teclado, colisão com bordas |

## Correções feitas em relação ao código original

Alguns exercícios continham erros de sintaxe ou lógica que impediam a execução ou geravam resultado incorreto. Foram corrigidos:

- **`conversor_celsius_fahrenheit.py`**: parêntese não fechado em `float(input(...))` impedia a execução; a variável de Celsius era lida mas nunca usada no cálculo.
- **`letras_de_uma_palavra.py`** e **`letras_de_uma_palavra_v2.py`**: o `for` reatribuía a variável de entrada (`for palavra in palavra`), sobrescrevendo a string original a cada iteração. Corrigido usando uma variável de laço distinta (`letra`).
- **`tupla_hobbies.py`**: `("olhar, dormir, praticar")` é uma string, não uma tupla — faltava a vírgula separando os elementos. Corrigido para `("olhar", "dormir", "praticar")`.
- **`calculadora_imc.py`**: removido `import pandas as pd` não utilizado.

## Observação sobre duplicatas

Alguns exercícios têm mais de uma versão (ex.: cálculo de idade, aprovação por média, contagem de 1 a 10). Foram mantidos como arquivos separados por refletirem entregas distintas, mas podem ser consolidados se preferir reduzir redundância no repositório.

## Como executar

```bash
python3 caminho/do/arquivo.py
```

A maioria dos scripts lê dados via `input()` no terminal. Os scripts em `05-pygame/` abrem uma janela gráfica e exigem a biblioteca `pygame` instalada:

```bash
pip install pygame
```

`quadrado_controlavel.py` é a base conceitual que evoluiu para o projeto **Recife Verde**.
