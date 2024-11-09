import yfinance as yf
import pandas as pd
import numpy as np



def price_change_indicator(ticker, start_date, end_date):

    # Pega os dados 
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval="1h")


    # Extract prices at 3pm and 4pm for each day
    stock_data['Datetime'] = pd.to_datetime(stock_data.index)

    # Pega os preços de 16h (fechamento)

    precos = stock_data[(stock_data['Datetime'].dt.hour == 16)]
  
    # Isso aqui é só pra n travar mas n entendi q q faz fudeu
  
    precos = precos['Close'].reset_index(drop=True)

    # Cria uma variável que guarda toda variação em % do fechamento de um dia pro anterior.
    # exemplo: variacoes relativo ao dia 10/03/2024 vai ser a variação do dia 9 pro dia 10

    variacoes = (precos[1:].values - precos[:-1].values) / precos[:-1].values * 100


   # A variação de cada dia é classificada em -2, -1, 0, 1, 2 : cai muito, cai pouco, praticamente estável, sobe pouco e sobe muito
   # obs: dá pra ajustar pra terem só 3 classes ou mais tb


    dp = np.std(variacoes)
    y = []

    for var in variacoes:
        if var <= -dp:
            y.append(-2)
        elif var <= -0.4 * dp:
            y.append(-1)
        elif var <= 0.4 * dp:
            y.append(0)
        elif var <= 1 * dp:
            y.append(1)
        else:
            y.append(2)

    # Só printa aí o que ele considerou como variação alta, baixa ...

    print('Variações > {}% são consideradas altas (2 ou -2)'.format(round(dp, 2)))
    print('Variações entre {}% e {}% são consideradas médias (1 ou -1) '.format(round(dp * 0.4, 2) , round(dp, 2)))
    print('Variações < {}% são consideradas nulas (0) '.format(round(dp * 0.4, 2)))
    print(y)

    # Esse Y que retorna é o que tem que ser colocado na função de classificador
    return y

