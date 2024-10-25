from datetime import datetime, timedelta
import yfinance as yf
import openpyxl

Lista = ["AAPL", "MSFT", "GOOGL", "AMZN"]

def ReiniciarPlanilha():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # Calcular as datas dos últimos 20 anos
    fim = datetime.now()
    inicio = fim - timedelta(days=20*365)
    delta = timedelta(days=1)
    
    current_date = inicio
    row = 1
    while current_date <= fim:
        sheet.cell(row=row, column=1, value=current_date.strftime('%Y-%m-%d'))
        current_date += delta
        row += 1
    
    workbook.save("Planilha.xlsx")

# 1. Função para obter dados históricos de ações com yfinance
def obter_dados_acao(ticker):
    # Calcular a data de início e fim
    fim = datetime.now()
    inicio = fim - timedelta(days=20*365)
    
    # Baixar dados históricos da ação (ex: Apple 'AAPL')
    acao = yf.Ticker(ticker)
    dados = acao.history(start=inicio.strftime('%Y-%m-%d'), end=fim.strftime('%Y-%m-%d'))
    return dados

# 2. Função para salvar os dados em uma planilha Excel usando openpyxl
def salvar_dados_em_excel(dados, nome_arquivo, primeira_vez=False):
    if dados.empty:
        print(f"Nenhum dado encontrado para salvar em {nome_arquivo}")
        return

    try:
        # Tentar abrir o arquivo Excel existente
        workbook = openpyxl.load_workbook(nome_arquivo)
        sheet = workbook.active
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return

    # Encontrar a próxima coluna vazia
    col_offset = sheet.max_column
    
    if (sheet.max_column != 1):
        col_offset = sheet.max_column + 2 

    # Escrever cabeçalhos na nova coluna
    headers = ["Data", "Abertura", "Alta", "Baixa", "Fechamento", "Volume"]
    for i, header in enumerate(headers):
        sheet.cell(row=1, column=col_offset + i, value=header)

    # Criar um dicionário para acesso rápido aos dados históricos
    dados_dict = {index.strftime('%Y-%m-%d'): row for index, row in dados.iterrows()}

    # Escrever os dados históricos na planilha usando as datas existentes na coluna 1
    for row_idx in range(2, sheet.max_row + 1):
        data = sheet.cell(row=row_idx, column=1).value
        if data in dados_dict:
            row = dados_dict[data]
            valores = [data, row['Open'], row['High'], row['Low'], row['Close'], row['Volume']]
            for col_idx, valor in enumerate(valores):
                sheet.cell(row=row_idx, column=col_offset + col_idx, value=valor)
        else:
            print(f"Erro: Dados não encontrados para a data {data}")

    # Salvar o arquivo Excel
    workbook.save(nome_arquivo)
    print(f"Dados salvos com sucesso em {nome_arquivo}")

# Exemplo de uso
ReiniciarPlanilha()
primeira_vez = True
for ticker in Lista:
    dados = obter_dados_acao(ticker)
    salvar_dados_em_excel(dados, "Planilha.xlsx", primeira_vez)
    primeira_vez = False
