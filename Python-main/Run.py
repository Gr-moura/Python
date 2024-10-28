import Excel
import Backtest

Lista = ["AAPL", "MSFT", "GOOGL", "AMZN"]

Excel.ReiniciarPlanilha()
for ticker in Lista:
    dados = Excel.obter_dados_acao(ticker)
    Excel.salvar_dados_em_excel(dados, "Planilha.xlsx", acao = ticker)

profits = Backtest.runBacktest('2017-11-13', '2023-11-13', len(Lista))
print(profits)
print(sum(profits))