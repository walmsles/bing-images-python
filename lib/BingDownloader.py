import json

class BingDownloader:

	all_markets = { "en-US", "zh-CN", "ja-JP", "en-AU", "en-UK", "de-DE", "en-NZ", "en-CA" }
	
	def __init__(self, markets=None):
		self.bing_base_url = "https://bing.com/"
		self.markets = set() 

		if markets != None:
			# add init markets to initial empty set
			for market in markets:
			 	self.add_market(market)
		else:
			self.markets = self.all_markets

	def add_market(self, market):
	 	if market != None:
	 		self.markets.add(market)
	 	else:
	 		raise Exception('must provide a market to add!')

