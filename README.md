# Conversor de Temperatura (Celsius para Fahrenheit)

Um projeto simples desenvolvido em Python para converter temperaturas de Celsius (°C) para Fahrenheit (°F).

## Sobre o projeto

Este programa solicita ao usuário uma temperatura em graus Celsius e realiza a conversão para Fahrenheit utilizando a fórmula:

```
°F = (°C × 9/5) + 32
```

Ao final, o resultado é exibido na tela.

## Tecnologias utilizadas

- Python 3

## Estrutura do projeto

```
conversor-temperatura/
│
├── conversor.py
├── README.md
```

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/conversor-temperatura.git
```

2. Acesse a pasta do projeto:

```bash
cd conversor-temperatura
```

3. Execute o programa:

```bash
python conversor.py
```

## Exemplo de uso

```text
Digite a temperatura em Celsius: 25

25.0°C equivalem a 77.0°F
```

## Fórmula utilizada

```python
fahrenheit = (celsius * 9 / 5) + 32
```

## Objetivo

Este projeto foi desenvolvido para praticar conceitos básicos de programação em Python, incluindo:

- Entrada de dados com `input()`
- Conversão de tipos com `float()`
- Operações matemáticas
- Exibição de resultados com `print()`
