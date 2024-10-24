import yfinance as yf
import openpyxl

Lista = ["AAPL"]

# 1. Função para obter dados históricos de ações com yfinance
def obter_dados_acao(ticker):
    # Baixar dados históricos da ação (ex: Apple 'AAPL')
    acao = yf.Ticker(ticker)
    dados = acao.history(period="1mo")  # Exemplo: pegar dados do último mês
    return dados

# 2. Função para salvar os dados em uma planilha Excel usando openpyxl
def salvar_dados_em_excel(dados, nome_arquivo):
    # Criar um novo arquivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Escrever cabeçalhos
    sheet.append(["Data", "Abertura", "Alta", "Baixa", "Fechamento", "Volume"])

    # Escrever os dados históricos na planilha
    for index, row in dados.iterrows():
        data = index.strftime('%Y-%m-%d')
        abertura = row['Open']
        alta = row['High']
        baixa = row['Low']
        fechamento = row['Close']
        volume = row['Volume']
        
        # Adicionar a linha na planilha
        sheet.append([data, abertura, alta, baixa, fechamento, volume])

    # Salvar o arquivo Excel
    workbook.save(nome_arquivo)
    print(f"Dados salvos com sucesso em {nome_arquivo}")

# 3. Executar o código
for ticker in Lista:   # Exemplo: ação da Apple
    dados = obter_dados_acao(ticker)
    salvar_dados_em_excel(dados, "Planilha.xlsx")
