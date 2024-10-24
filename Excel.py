from openpyxl import load_workbook

# Abrir um arquivo Excel existente
wb = load_workbook('Planilha.xlsx')
sheet = wb.active

# Ler um valor de uma célula
valor = sheet['A1'].value
print(valor)

# Modificar uma célula
sheet['A1'] = 'Novo valor'

# Salvar as alterações
wb.save('Planilha.xlsx')
