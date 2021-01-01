import json

class Downloader:

	def __init__(self, markets=None, records=100, start=0):
		self.markets = set() 
		self.records = records
		self.start = start

		# define set of valid markets 
		self._all_markets = { "en-US", "zh-CN", "ja-JP", "en-AU", "en-UK", "de-DE", "en-NZ", "en-CA" }

		if markets != None:
			# add init markets to initial empty set
			for market in markets:
			 	self.add_market(market)
		else:
			self.markets = self._all_markets

	def add_market(self, market):
	 	if market in self._all_markets:
	 		self.markets.add(market)
	 	else:
	 		raise Exception(f'{market} is not a valid market')