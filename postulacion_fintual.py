from random import randint
import datetime

# Suponemos que el portofalio se construye a partir de una seleccion de stocks donde cada stock tiene un porcentage de participacion en el portafolio.

class Portfolio:
        def __init__(self, stocks): # stocks es una lista de objetos del tipo Stock
            self.stocks = stocks

        ## Metodo Profit pedido
        
        def Profit(self, date1, date2): #Recibe 2 fechas en formato Dia-Mes-Año, ej '01-05-2021'
            print('Calculando profit .... ')
            profit = 0
            for stock in self.stocks:
                stockProfit = stock.percent * (stock.Price(date2) - stock.Price(date1))
                profit += stockProfit
                print('Profit atribuido a %s ( %.2f %%): $ %.2f' % (stock.name, stock.percent*100, stockProfit))    
            print('Total: $ %.2f'% profit)
            return profit
        
        ## Bonus (Para calcular el annualized return del fondo, concideramos años y fracciones de a años)
        def AnnualizedReturn(self, date1, date2):
            initialValue = 0
            finalValue = 0
            years = (datetime.datetime.strptime(date2, '%d-%m-%Y') - datetime.datetime.strptime(date1, '%d-%m-%Y')).days/365
            for stock in self.stocks:
                initialValue += stock.percent * stock.Price(date1)
                finalValue += stock.percent * stock.Price(date2)
            Ar = (finalValue/initialValue) ** ((1 / years) - 1)
            print('Annualize Return %.2f %%'% Ar)
            return Ar

################################################################################
#################                    TEST                    ###################
################################################################################
class Stock:
    def __init__(self, name, percent, dates):
        self.name = name
        self.percent = percent
        self.prices = dict() #Definimos la lista de precios como un diccionario
        
        for date in dates: #Poblamos los precios para las fechas dadas con un random int
            self.prices[date]= randint(1,100)

    def Price(self, date):
        return self.prices[date]

start_date = datetime.date(2018, 1, 1)
end_date   = datetime.date.today()
dates = [ (start_date + datetime.timedelta(n)).strftime("%d-%m-%Y") for n in range(int ((end_date - start_date).days + 1))]
#print(dates)

stockNamesAndPercent = [['Abble', 0.2], ['Tasle', 0.2], ['IVM', 0.1], ['Mitflix', 0.1], ['Amozan', 0.1], ['Guugle', 0.1], ['Fontual', 0.1], ['Dosney', 0.1]]
stocks = []
for stock in stockNamesAndPercent:
    stocks.append(Stock(stock[0], stock[1], dates))

fontualNorrisA = Portfolio(stocks) #Cualquier parecido con la realidad es mera coincidencia.

profit = fontualNorrisA.Profit('01-01-2018', datetime.date.today().strftime("%d-%m-%Y"))
annualizedReturn = fontualNorrisA.AnnualizedReturn('01-01-2018', datetime.date.today().strftime("%d-%m-%Y"))



