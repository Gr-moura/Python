import yfinance as yf
from datetime import datetime, timedelta

def criavetores(fim, ticker) :
    atual = datetime(2022, 11, 11, 0, 0, 0)
    
    # Baixar dados históricos da ação (ex: Apple 'AAPL')
    acao = yf.Ticker(ticker)
    vetores = []

    while 1 == 1 :
        atual += timedelta(days=1)
        if(atual.strftime('%Y-%m-%d') == fim) :
            break

        dados = acao.history(start=atual.strftime('%Y-%m-%d'), end=(atual + timedelta(days=1)).strftime('%Y-%m-%d'), interval='1h')
        if(len(dados) == 0) :
            print("NONE")
        
    print(vetores)

if __name__ == "__main__" :
    criavetores('2024-11-04', "AAPL")