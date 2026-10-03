# 💵 Conversor de Dólar com IOF

Um programa simples desenvolvido em **Python** que consulta a cotação atual do dólar através de uma API e calcula quanto uma determinada quantia em dólares custaria em reais, incluindo o **IOF de 3,5%**.

## 🚀 Funcionalidades

* Consulta a cotação atual do dólar em tempo real.
* Recebe do usuário a quantidade de dólares desejada.
* Converte o valor de USD para BRL.
* Calcula o valor do IOF.
* Exibe o valor base e o valor total da operação.
* Trata erros de entrada e problemas na comunicação com a API.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Requests**
* **AwesomeAPI**

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Entre na pasta do projeto

```bash
cd seu-repositorio
```

### 3. Instale a biblioteca Requests

```bash
pip install requests
```

Caso esteja utilizando o Windows e o comando `pip` não funcione:

```bash
py -m pip install requests
```

### 4. Execute o programa

```bash
python main.py
```

Ou, no Windows:

```bash
py main.py
```

## 🔄 Como funciona

O programa segue algumas etapas:

1. O usuário informa quantos dólares deseja converter.
2. O programa acessa a **AwesomeAPI** para obter a cotação atual do dólar.
3. A cotação é multiplicada pela quantidade de dólares informada.
4. O programa calcula o IOF de **3,5%** sobre o valor convertido.
5. O IOF é somado ao valor base.
6. O programa exibe os valores calculados.

### Fórmula utilizada

**Valor base:**

```text
Cotação do dólar × Quantidade de dólares
```

**IOF:**

```text
Valor base × 3,5%
```

**Valor total:**

```text
Valor base + IOF
```

## 💻 Exemplo de execução

```text
Quantos dólares você quer? 100

Cotação atual: R$ 5.35
Valor base: R$ 535.00
Valor do imposto: R$ 18.73
Valor total com IOF: R$ 553.73
```

> A cotação apresentada varia de acordo com o valor retornado pela API no momento da execução.

## 🌐 API utilizada

O projeto utiliza a **AwesomeAPI** para consultar a cotação USD/BRL:

```text
https://economia.awesomeapi.com.br/json/last/USD-BRL
```

A aplicação utiliza o valor `bid` retornado pela API como cotação do dólar.

## ⚠️ Tratamento de erros

O programa possui tratamento para:

* Entrada que não seja um número válido.
* Falha na comunicação com a API.
* Erros na requisição HTTP.
* Impossibilidade de obter a cotação.

## 📚 Objetivo do projeto

Este projeto foi desenvolvido como uma prática de **Python**, com foco em:

* Consumo de APIs.
* Requisições HTTP.
* Conversão de dados JSON.
* Tratamento de exceções.
* Entrada e saída de dados.
* Cálculos matemáticos em Python.

---

**Desenvolvido por Vinícius Rodrigues da Silva** 🚀
