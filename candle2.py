import xlrd 
import statistics as st
import matplotlib.pyplot as fig

wb=xlrd.open_workbook('AAPL.xls')
p=wb.sheet_by_name('Planilha2')

nl=p.nrows
nc=p.ncols
dados=[]
candles=[]
k=0
cores=[]

for i in range(1, nc):
    y=p.col_values(i)
    dados.append(y)

# fazendo candles para um intervalo

n0=int(input("  Você quer começando por que dia? "))
nf=int(input("  Você quer terminando por que dia? "))

for j in range(n0 , nf+1):
    candle=[]
    for i in range(0, 5):
        candle.append(dados[i][j])

    candles.append(candle)
    

while(k<=len(candles)-1):
    if(candles[k][0]>=candles[k][3]):
        cores.append("red")
    else:
        cores.append("green")
    k=k+1


fig.figure(figsize=(15,7))
bplots = fig.boxplot(candles, patch_artist= True )
for i, bplot in enumerate(bplots['boxes']):
    bplot.set(facecolor = cores[i])
fig.xlabel('dia')
fig.ylabel('preço')
fig.show()

