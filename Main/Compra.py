import random

#Como a função de compra ainda vai ser programada, fiz ela so comprar as ações aleatoriamente. 

#Considerei que a funçao de compra recebe um número row, referente à linha da planilha do excel
#que contem a data de hoje. O intuito é que a função compra acesse todas as linhas anteriores a
#essa para obter seus dados.
def compra(row):
    return [random.randint(0, 4), random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)]