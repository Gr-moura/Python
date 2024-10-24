import yfinance as yf
import openpyxl

Lista = ["AAPL", "MSFT", "GOOGL", "AMZN", "FB", "TSLA", "NVDA", "PYPL", "ADBE", "NFLX"]

# 1. Função para obter dados históricos de ações com yfinance
def obter_dados_acao(ticker):
    # Baixar dados históricos da ação (ex: Apple 'AAPL')
    acao = yf.Ticker(ticker)
    dados = acao.history(period="1mo")  # Exemplo: pegar dados do último mês
    return dados

# 2. Função para salvar os dados em uma planilha Excel usando openpyxl
def salvar_dados_em_excel(dados, nome_arquivo):
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

    # Encontrar a próxima coluna vazia
    col_offset = sheet.max_column + 1

    # Escrever cabeçalhos na nova coluna
    headers = ["Data", "Abertura", "Alta", "Baixa", "Fechamento", "Volume"]
    for i, header in enumerate(headers):
        sheet.cell(row=1, column=col_offset + i, value=header)

    # Escrever os dados históricos na planilha
    for row_idx, (index, row) in enumerate(dados.iterrows(), start=2):
        data = index.strftime('%Y-%m-%d')
        valores = [data, row['Open'], row['High'], row['Low'], row['Close'], row['Volume']]
        for col_idx, valor in enumerate(valores):
            sheet.cell(row=row_idx, column=col_offset + col_idx, value=valor)

    # Salvar o arquivo Excel
    workbook.save(nome_arquivo)
    print(f"Dados salvos com sucesso em {nome_arquivo}")

# 3. Executar o código
for ticker in Lista:   # Exemplo: ação da Apple
    dados = obter_dados_acao(ticker)
    salvar_dados_em_excel(dados, "Planilha.xlsx")
