# Desafio Tunts Rocks

## Descrição
Este é um projeto desenvolvido como parte do desafio Tunts Rocks. Ele consiste em uma aplicação Python para análise de dados de alunos em uma planilha do Google Sheets.

## Pré-requisitos
- Python 3.x instalado (recomenda-se o uso de um ambiente virtual)
- Conta de serviço do Google Cloud com acesso à API do Google Sheets
- Credenciais de serviço JSON para autenticação

## Instalação
1. Clone este repositório em sua máquina local:
    ```bash
    git clone https://github.com/pedr0alencar/tunts-rocks-challenge.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd tunts-rocks-challenge
    ```
3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure suas credenciais de serviço do Google Cloud em um arquivo JSON e salve-o no diretório `credentials`.

## Uso
1. Preencha as variáveis de ambiente no arquivo `.env` com as informações necessárias.
2. Execute o script principal `main.py` para iniciar a aplicação:
    ```bash
    python src/main.py
    ```

## Estrutura do Projeto
O projeto está estruturado da seguinte forma:
- `src/`: Contém os arquivos-fonte do projeto.
  - `google_sheets.py`: Módulo para interação com a API do Google Sheets.
  - `main.py`: Script principal da aplicação.
  - `student_analysis.py`: Módulo para análise dos dados dos alunos.
- `credentials/`: Diretório para armazenar as credenciais de serviço JSON.
- `.env`: Arquivo de configuração para variáveis de ambiente.
