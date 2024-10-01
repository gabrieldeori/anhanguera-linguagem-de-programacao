# Plano de Ensino: Curso de Python

Este repositório contém os códigos desenvolvidos ao longo do curso de Python, organizado em unidades e seções, facilitando o aprendizado progressivo. Cada seção explora um conceito ou funcionalidade específica da linguagem e suas aplicações.

## UNIDADE 1 – Introdução a Linguagem Python

A Unidade 1 introduz os conceitos fundamentais da linguagem Python, abordando desde os princípios básicos até estruturas essenciais como condicionais, loops e funções.

### [Seção 1.1 – A linguagem Python](secao_1_1)
Uma visão geral sobre a linguagem Python, suas características e o ambiente de desenvolvimento.

### [Seção 1.2 – Estruturas Condicionais em Python](secao_1_2)
Introdução às estruturas condicionais (if, elif, else) e como elas são usadas para controle de fluxo.

### [Seção 1.3 – Estruturas de Repetição em Python](secao_1_3)
Aborda as principais estruturas de repetição (while, for) e como utilizá-las para iteração em Python.

### [Seção 1.4 – Funções em Python](secao_1_4)
Explora a definição e utilização de funções em Python para criar blocos de código reutilizáveis.

## UNIDADE 2 – Explorando Recursos do Python

A Unidade 2 aprofunda o uso de estruturas de dados mais avançadas, além de introduzir conceitos como classes, métodos, bibliotecas e módulos.

### [Seção 2.1 – Estruturas de Dados em Python – Parte I](secao_2_1)
Trata de listas e tuplas, suas operações e utilidades no dia a dia do desenvolvimento.

### [Seção 2.2 – Estruturas de Dados em Python – Parte II](secao_2_2)
Explora dicionários e sets, importantes para lidar com dados não ordenados e associados.

### [Seção 2.3 – Classes e Métodos em Python](secao_2_3)
Introdução à Programação Orientada a Objetos (POO) com Python, cobrindo a criação de classes e métodos.

### [Seção 2.4 – Bibliotecas e Módulos em Python](secao_2_4)
Aborda o uso de bibliotecas e módulos para estender as funcionalidades padrão do Python.

## UNIDADE 3 – Introdução à Análise de Dados com Python

A Unidade 3 foca na manipulação de dados, apresentando ferramentas populares para análise e visualização.

### [Seção 3.1 – Aplicação de Banco de Dados com Python](secao_3_1)
Demonstra como conectar e interagir com bancos de dados utilizando Python.

### [Seção 3.2 – Introdução a Biblioteca Pandas](secao_3_2)
Uma introdução à biblioteca Pandas, essencial para manipulação e análise de dados.

### [Seção 3.3 – Introdução a Manipulação de Dados em Panda](secao_3_3)
Explora como manipular grandes conjuntos de dados de forma eficiente utilizando Pandas.

### [Seção 3.4 – Visualização de Dados em Python](secao_3_4)
Apresenta bibliotecas para visualização de dados, como Matplotlib e Seaborn, para criar gráficos e representações visuais.

## UNIDADE 4 – Aplicações com Python

A Unidade 4 introduz aplicações práticas da linguagem Python em diferentes domínios como web, mobile e testes automatizados.

### [Seção 4.1 – Introdução à Programação Web com Python](secao_4_1)
Explora os fundamentos da programação web usando frameworks como Flask ou Django.

### [Seção 4.2 – Introdução à Programação Mobile com Python](secao_4_2)
Discute o desenvolvimento de aplicativos móveis com Python, utilizando frameworks como Kivy ou BeeWare.

### [Seção 4.3 – Testes com Python](secao_4_3)
Cobertura de testes automatizados com Python, incluindo bibliotecas como unittest e pytest.

---

## Executando os Exercícios

###### Sugestão: utilize o pyenv: (https://github.com/pyenv/pyenv) ou (https://pyenv-win.github.io/pyenv-win/)


### VENV
Caso esteja utilizando no windows pode ser que receba um erro do tipo:
```diff
- ... não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.
```

Para isso indico um comando que libera a execução de scripts apenas no processo da janela aberta. Portanto tenha cuidado com o que vai executar aqui.

```powershell
Set-ExecutionPolicy Bypass -Scope Process
```

Confira os links acima para ver como instalar as versões do python corretamente

Versão python escolhida para os exercícios:
> python 3.12.5

Ambiente de desenvolvimento:

Crie o ambiente:
```sh
python -m venv .venv
```
Ative o ambiente:
```sh
source .venv/bin/activate
```
Instale os requisitos se existir:
```sh
pip -r install requirements.txt
```
Execute o exercício:
```sh
python ./secao_x_y/exercicio_escolhido.py
```

Ambiente de desenvolvimento (Windows):

Crie o ambiente:

```powershell
python -m venv .venv
```
Ative o ambiente:

```powershell
.venv\Scripts\activate
```
Instale os requisitos:

```powershell
pip install -r .\requirements.txt
```
Instale os requisitos se existir:

```powershell
pip -r install requirements.txt
```
Execute o exercício:

```powershell
python .\secao_x_y\exercicio_escolhido.py
```

Parar projeto:

Fechar o server: CTRL+C

Desativar o ambiente:
```powershell
deactivate
```