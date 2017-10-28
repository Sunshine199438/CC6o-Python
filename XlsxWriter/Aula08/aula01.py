import xlsxwriter


workbook = xlsxwriter.Workbook('Planilha01.xlsx')
worksheet = workbook.add_worksheet()

items = (
    ['Produto','Quatidade'],
    ['Caneta','150'],
    ['bloco azul','80'],
    ['Caderno','2'],
    ['Borracha','212'],
)


row = 0
col = 0

for item,qtd in (items):
    worksheet.write(row,col, item)
    worksheet.write(row,col+1, qtd)
    row+=1

worksheet.write(row,0,'Total')
worksheet.write(row,1,'=Sum(B2:B5)')

workbook.close()



print ('. |fim da ap' )