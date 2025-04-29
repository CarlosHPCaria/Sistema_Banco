# 🏦 Desafio de Sistema Bancário em Python para o Bootcamp DIO Python Developer 🐍

Este projeto foi desenvolvido como parte do desafio proposto no Bootcamp DIO Python Developer. O objetivo principal era aplicar os conhecimentos básicos da linguagem Python na criação de um sistema bancário simplificado, capaz de realizar três operações fundamentais: **depósito 💰**, **saque 💸** e **visualização de extrato 🧾**.

## Visão Geral 

O sistema simula as funcionalidades essenciais de uma conta bancária, permitindo que um usuário (nesta primeira versão, um único usuário predefinido) interaja através de um menu simples para:

* **Depositar ➕:** Adicionar valores positivos ao saldo da conta.
* **Sacar ➖:** Retirar valores do saldo, respeitando um limite de **3️⃣ saques diários** com um valor máximo de **R$ 500,00 🏧** por saque.
* **Visualizar Extrato 📜:** Exibir todas as movimentações realizadas na conta (depósitos e saques), juntamente com o saldo atual. Caso não haja movimentações além do saldo inicial, uma mensagem informativa é mostrada.

## Complexidade e Detalhes Implementados 🧠

Apesar de se tratar de um sistema básico, foram considerados alguns detalhes para adicionar um grau de complexidade e demonstrar o uso de conceitos importantes em Python:

* **Orientação a Objetos 📦:** A lógica do sistema foi estruturada utilizando uma classe `ContaBancaria` para representar a conta e seus métodos para realizar as operações.
* **Controle de Saques 🛡️:** A operação de saque implementa um controle de limite diário (quantidade e valor), demonstrando o uso de lógica condicional e variáveis de estado.
* **Registro de Extrato 📝:** Todas as operações (depósitos e saques) são registradas em uma lista (`extrato`) para posterior visualização, incluindo a **data 📅** da transação.
* **Formatação de Valores 🇧🇷:** Os valores monetários são exibidos no formato brasileiro (**R$ xxx.xx**).
* **Tratamento de Entradas ✅:** O sistema valida entradas para garantir que valores de depósito e saque sejam positivos.
* **Mensagens Informativas 💬:** O usuário recebe feedback claro sobre o sucesso ou falha de cada operação, bem como informações sobre limites e saldo.
* **Simulação de Conta Predefinida 👤:** Para simplificar a interação nesta primeira versão, uma conta fictícia é criada automaticamente ao iniciar o programa, eliminando a necessidade de criação de conta pelo usuário.

## Ferramentas e Conceitos Utilizados 🛠️

Este projeto demonstra o uso de:

* **Classes e Objetos 🧱:** Para modelar a conta bancária.
* **Métodos ⚙️:** Para implementar as operações bancárias.
* **Listas 📒:** Para armazenar o extrato de movimentações.
* **Estruturas de Controle 🚦:** `if/elif/else` para lógica condicional e `while` para o loop principal do sistema.
* **Funções 🧩:** Para organizar o código em blocos reutilizáveis (menu, limpeza de tela).
* **Entrada e Saída ⌨️/🖥️:** `input()` para obter dados do usuário e `print()` para exibir informações.
* **Formatação de Strings (f-strings) ✨:** Para exibir valores monetários e mensagens de forma clara.
* **Módulo `datetime` 🕰️:** Para registrar a data das operações no extrato.
* **Módulo `os` 💻:** Para tentar limpar a tela do terminal, melhorando a experiência do usuário (comportamento dependente do sistema operacional).

## Conclusão 🎉

Este desafio foi uma excelente oportunidade para consolidar os conhecimentos básicos de Python e aplicá-los na resolução de um problema prático. A implementação das operações de depósito, saque e extrato, com a adição de regras de negócio como limites de saque, demonstra a capacidade de utilizar a linguagem para criar sistemas com um grau razoável de complexidade, mesmo em suas etapas iniciais de aprendizado.
