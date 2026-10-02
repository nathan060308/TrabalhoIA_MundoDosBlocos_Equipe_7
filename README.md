# Planejamento no Mundo dos Blocos de Tamanho Variável via SAT Solver

Trabalho prático desenvolvido para a disciplina de **Fundamentos de Inteligência Artificial** do Instituto de Computação (IComp) da Universidade Federal do Amazonas (UFAM), ministrada pelo **Prof. Edjard Mota**.

---

## Integrantes da Equipe
* Ana Barroso
* John Kennedy
* Nathan Maciel
* Victor Silva

---

## Descrição do Projeto
Este projeto implementa uma solução formal e automatizada para o problema de planejamento no **Mundo dos Blocos com dimensões variáveis** e restrições de estabilidade física. 

A abordagem converte uma especificação em Lógica de Primeira Ordem (LPO) para a Forma Normal Conjuntiva (CNF) em Lógica Proposicional, sendo resolvida através de um **SAT Solver** com interpretação automática dos planos gerados.

---

## Arquitetura e Ficheiros do Repositório

* **`bw2cnf_var.py`**: Gerador em Python que converte as regras formais, estado inicial e meta para cláusulas CNF no formato DIMACS, gerando também o mapa de variáveis.
* **`rodar_sat.py`**: Script responsável por invocar o SAT Solver (`python-sat` / `miniSAT`) e registrar a valoração dos literais lógicos no arquivo de saída informado.
* **`interpretar.py`**: Interpretador que mapeia os identificadores booleanos do arquivo de resultado de volta para ações em linguagem natural e estado temporal do sistema.
* **`trab01_blocos2SAT.cnf`**: Arquivo gerado em formato DIMACS CNF contendo as cláusulas proposicionais.
* **`trab01_blocos2SAT.map`**: Mapeamento numérico de variáveis booleanas para predicados e instantes temporais.
* **`resultado1.txt`**: Saída do Solver para o Cenário 1 (SAT com $T=4$).
* **`resultado2.txt`**: Saída do Solver para o Cenário 2 (UNSAT demonstrando horizonte insuficiente com $T=2$).
* **`resultado3.txt`**: Saída do Solver para o Cenário 3 (SAT para meta alternativa com $T=5$).

---

## Requisitos de Instalação

Para executar o projeto, é necessário ter o **Python 3.8+** instalado e a biblioteca `python-sat`:

```bash
pip install python-sat
