import json

class BingDownloader:

	def __init__(self, markets={}):
		self.bing_base_url = "https://bing.com/"
		self.markets = set()
		print(markets)
		for market in markets:
		 	print(market)
		 	self.add_market(market)

	def add_market(self, market):
	 	if market != None:
	 		self.markets.add(market)
	 	else:
	 		raise Exception('must provide a market to add!')

