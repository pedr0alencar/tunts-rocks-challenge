![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/3ee79eb2-f0ff-4b8e-b4b4-37cf63dac95a)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

# Tunts.Rocks Challenge - Student Situation Analysis
Desafio técnico da Tutnts.Rocks - Dev Training Program  

## Sumário

- [Link da planilha copiada do candidato](#link-da-planilha-copiada-do-candidato)
- [Visão Geral](#visão-geral)
- [Pré-requisitos](#pré-requisitos)
- [Como Rodar Localmente](#como-rodar-localmente)
    - [Instalação de Dependências](#instalação-de-dependências)
    - [Executando a Aplicação](#executando-a-aplicação)
- [Sobre o Código](#sobre-o-código)
    - [Logging](#logging)
- [Como Rodar com Sua Própria Planilha](#como-rodar-com-sua-própria-planilha)
    - [Criar um Projeto na Plataforma Google Cloud (GCP)](#criar-um-projeto-na-plataforma-google-cloud-gcp)
    - [Habilitar a API do Google Sheets para Seu Projeto](#habilitar-a-api-do-google-sheets-para-seu-projeto)
    - [Criar uma Conta de Serviço](#criar-uma-conta-de-serviço)
    - [Baixar o Arquivo da Chave JSON](#baixar-o-arquivo-da-chave-json)
    - [Configurando as Variáveis de Ambiente](#configurando-as-variáveis-de-ambiente)
- [Considerações de Segurança](#considerações-de-segurança)
- [Demonstração](#demonstração)



## Link da planilha copiada do candidato
https://docs.google.com/spreadsheets/d/1qB_SdyfU3-MWK0i3rnFdYvhLK4nOVcoGu60S9Og_Vt8/edit#gid=0 

   

## Visão Geral
Este script Python automatiza a análise da situação dos estudantes em um documento do Google Sheets com base em suas notas e frequência. Ele calcula a média das três provas (P1, P2 e P3) de cada estudante e determina sua situação conforme as regras abaixo:

- **Reprovado por Nota**: Quando a média das notas (m) é inferior a 5.
- **Exame Final**: Quando a média das notas está entre 5 e 7 (5 ≤ m < 7).
- **Aprovado**: Quando a média das notas é igual ou superior a 7 (m ≥ 7).

Além disso, se o número de faltas do estudante ultrapassar 25% do total de aulas, ele será automaticamente **Reprovado por Falta**, independentemente da média. Para os estudantes na situação "Exame Final", o script também calcula a **Nota para Aprovação Final (NAF)** necessária. Esta nota é calculada de forma que a média final, considerando a NAF, seja pelo menos 5 para aprovação, seguindo a fórmula: 5 ≤ (m + naf)/2.

O script atualiza a planilha com essas informações, automatizando o processo de análise da situação dos estudantes.

## Pré-requisitos
- Python 3.8 ou superior.
- Conta Google com acesso à API do Google Sheets.
- Projeto no Google Cloud com a API do Sheets ativada.
- Conta de serviço no Google Cloud com permissões para a API do Sheets e um arquivo de chave JSON.

## Como rodar localmente
A fim de avaliação do desafio, a aplicação consumirá a API já com as informações da cópia da planilha do candidato. Assim, para executar:

1. Clone o repositório com:
```
git clone https://github.com/pedr0alencar/tunts-rocks-challenge.git
```
2. Navegue até o diretório do projeto e configure um ambiente virtual Python para gerenciar as dependências.
```
cd tunts-rocks-challenge
```

### Instalação de Dependências
Use `pip install -r requirements.txt` para instalar as dependências necessárias.


### Executando a Aplicação
Use o comando `python src/main.py` para iniciar o processo de leitura, análise e atualização das situações dos estudantes na sua planilha do Google Sheets.

## Sobre o código
A aplicação é dividida em três arquivos principais:

- `google_sheets.py`: Gerencia a autenticação e interação com a API do Google Sheets.
- `student_analysis.py`: Contém a lógica para calcular a situação de cada estudante com base nas regras fornecidas.
- `main.py`: Orquestra o processo chamando funções dos outros módulos.

Adicionalmente, temos:
- `credentials`: Armazena a chave json da planilha dentro do projeto do Google Cloud.
- `.env`: Parametriza o nome e o id da planilha.

### Logging
Foi utilizado o logging para acompanhamento das atividades, se tudo correr certo, aparecerá:  

![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/bc52555a-fd0d-446d-aa5a-465b9070c6c0)  
  
Também foi adicionado logging de warning e error para os casos:
- Nenhum dado foi lido na planilha.
- Falha ao atualizar células na tabela.
- Erro ao processar linha.
  
Se apresentar erro ao ler ou inserir os dados na planilha, a execução será encerrada.

## Como rodar com sua própria planilha:
Criar um Projeto na Plataforma Google Cloud (GCP):

- Visite o Console do Google Cloud.
- Clique no dropdown "Projeto" próximo ao canto superior esquerdo e, em seguida, clique em "Novo Projeto".
- Nomeie seu projeto (por exemplo, "Desafio Tunts Rocks") e clique em "Criar".

Habilitar a API do Google Sheets para Seu Projeto:

- Com seu novo projeto selecionado, navegue até "APIs & Serviços" > "Painel" na barra lateral esquerda.
- Clique em "ATIVAR APIS E SERVIÇOS" no topo. Procure por "API do Google Sheets", selecione-a e clique em "Ativar".

Criar uma Conta de Serviço:

- Vá para "APIs & Serviços" > "Credenciais" e clique em "Criar Credenciais" no topo. Selecione "Conta de serviço" no dropdown.
- Nomeie sua conta de serviço (por exemplo, "acesso-sheets"), conceda a ela um papel de "Editor" (isso lhe dá permissões para acessar e modificar suas planilhas do Google Sheets) e clique em "Concluído".
- Após criar a conta de serviço, clique nela na página "Credenciais". Vá para a aba "Chaves", clique em "Adicionar Chave" e escolha "Criar nova chave". Selecione "JSON" como o tipo de chave e clique em "Criar". Isso baixará o arquivo da chave JSON para o seu computador.

Baixar o Arquivo da Chave JSON:

- Armazene o arquivo da chave JSON baixado de forma segura. Este arquivo contém informações sensíveis que permitem acesso programático aos seus recursos do Google Cloud.
- Você usará este arquivo em seu projeto para autenticar o script com a API do Google Sheets.

Configurando as Variáveis de Ambiente:

- Mova o arquivo da chave JSON baixado para o diretório `credentials` dentro do seu projeto. Certifique-se de que o caminho no seu script corresponda à localização deste arquivo.
- Use o arquivo `.env` para definir variáveis de ambiente, como `SPREADSHEET_ID` e `SHEET_NAME`, com os respectivos valores do ID da sua Planilha do Google e o nome da aba que você pretende manipular.

## Demonstração
Imagens da planilha antes e depois da execução:  
  
![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/3ceb90fc-66bb-4f9b-ad35-45a4ff83742f)
  
![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/a5597c96-6ddb-4e17-8564-9616c080b4a7)


## Considerações de segurança
Este projeto inclui dados sensíveis, como chaves de API, para fins de demonstração. Em um cenário real, essas informações não seriam expostas publicamente. 

Make it fun, see you soon (-;
```
Speedy Dev off
```


