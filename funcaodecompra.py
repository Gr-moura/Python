from sklearn.linear_model import LogisticRegression
import numpy as np

# Fazer um programa que recebe um vetor e uma matriz de vetores e atributos e retorna o valor esperado.

# Esses valores são só pra testar

vt = np.array(range(4))
print(vt)
ma = np.array(range(16)).reshape(4, 4)

y = [2, 2, 1, 3]


def classificador(vetor, A, Y):


    """ 
    Essa função recebe a matriz A de vários vetores de ação e a matriz Y da performance
    de cada ação, ou seja se subiu ou desceu do dia pro dia seguinte
    """



  
    # Cria o modelo de regressão logística e coloca a matriz A de dados  e Y de resultados
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
    model.fit(A, Y)

    # Cria uma lista com as probabilidades do vetor pertencer a cada classe
    probs = model.predict_proba([vetor]).tolist()[0]
    classes = model.classes_.tolist()

    # Calcula o valor esperado que a variável pertença
    esperado = 0
    for i in range(len(classes)):
        esperado += classes[i]*probs[i]

    # Printa tudo
    for i in range(len(classes)):
        print('-' * 70)
        print('A probabilidade do vetor pertencer ao grupo {} é {}%  ' .format(classes[i], round(probs[i]*100, 2)))

    print('-' * 70)

    print('O resultado esperado para o vetor é {} '.format(round(esperado, 4)))

    return esperado




def funcaodevariasacoes(listadetickers, datainicio, datafim):


    """
    Pega uma lista de ações, aplica a função de compra (classificador) e compra 2 ações da que teve melhor performance e
    1 da 2a melhor performance. Caso o valor esperado das 2 ações seja negativo ele não compra nenhuma
    """


    # Pega os dados e acha o valor esperado de cada ação e salva em um dicionário

    compra = {}

    for ticker in listadetickers:
        vesperado = classificador(criavetor(ticker, datainicio, datafim), price_change_indicator(ticker, datainicio, datafim) )
        compra[ticker] = vesperado


    # Ordena esse dicionário do maior para o menor

    compraordenada = dict(sorted(compra.items(), key=lambda item: item[1], reverse=True))

    # Dá a ordem de compra de 2 para a melhor ação e 1 pra 2a melhor ação

    listacompras = []

    contador = 0
    for ticker in compraordenada:

        # Cria a exceção de se tudo for cair não compra nada

        if compraordenada[ticker] < 0:
            compraordenada[ticker] = 0

        else:
            if contador == 0:
                compraordenada[ticker] = 2

            elif contador == 1:
                compraordenada[ticker] = 1

            else:
                compraordenada[ticker] = 0

        contador += 1

    # Coloca o resultado em uma lista pra retornar

    for ticker in listadetickers:
        listacompras.append(compraordenada[ticker])

    return listacompras
