import urllib, json

def getStockData(stockSym):
	stockURL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES'
	stockSymbol = stockSym
	#apiKey 3PAQV3G32XPI8SG4
	apiKey = '3PAQV3G32XPI8SG4'
	stockURL = stockURL+'&symbols='+stockSymbol+'&apikey='+apiKey


	connection = urllib.urlopen(stockURL)
	responseString = connection.read().decode()

	return responseString

symbol = ''
while symbol != 'quit' :
	symbol = raw_input("Enter a stock symbol: ")
	if symbol != 'quit':
		stockData = getStockData(symbol)
		stockDict = {}
		stockDict = json.loads(stockData)
		#f=open('japi.out','a')
		print stockData
		print 'The current price of '+symbol+' is '+stockDict.get('Stock Quotes')[0].get('2. price')
print "Stock Quotes retrieved successfully!"