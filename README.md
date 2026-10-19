# Calculadora em Python

## 1. Sobre o projeto

Este projeto consiste em uma calculadora desenvolvida em Python, executada em ambiente Linux por meio do terminal. O programa permite realizar operações matemáticas básicas.

## 2. Funcionalidades

- Adição
- Subtração
- Multiplicação
- Divisão
- Verificação de operações inválidas
- Tratamento de divisão por zero

## 3. Arquivos do projeto

- `calculadora.py`: contém o código-fonte da calculadora.
- `executar.sh`: script Bash utilizado para iniciar o programa Python.
- `README.md`: documentação do projeto.

## 4. Requisitos

- Sistema Linux ou ambiente compatível, como o WSL com Ubuntu.
- Python 3 instalado.

## 5. Como executar o programa

Abra o terminal e acesse a pasta do projeto.

Dê permissão de execução ao script:

```bash
chmod +x executar.sh
```

Execute a calculadora com:

```bash
./executar.sh
```

Alternativamente, execute o script utilizando:

```bash
bash executar.sh
```


## 6. Explicação do código Python

O programa utiliza a função `calculadora()` para organizar a execução da calculadora.

A função `print()` apresenta o menu de operações disponíveis, enquanto `input()` recebe a opção escolhida e os números informados pelo usuário.

A estrutura condicional `if`, `elif` e `else` permite identificar a operação matemática selecionada e calcular o resultado correspondente.

A função `float()` converte os valores digitados em números que permitem operações com casas decimais.

O bloco `try` e `except` trata entradas numéricas inválidas. A verificação do divisor impede que uma divisão por zero seja realizada.

Por fim, `print()` exibe o resultado calculado no terminal.

## 7. Explicação do arquivo executar.sh

O arquivo `executar.sh` é um script Bash que automatiza a inicialização da calculadora.

## 8. Tecnologias utilizadas

- Python 3
- Bash
- Linux
- GitHub

## 9. Autor

Projeto desenvolvido como atividade prática de programação em Python.
