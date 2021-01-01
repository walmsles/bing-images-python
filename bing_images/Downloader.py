import json
import bing_images.services as services
import re

class Downloader:
	"""Downloader class encapsulating the process of downloading images from each defined market region"""

	def __init__(self, markets=None, records=100, start=0):
		"""
		Parameters:
		-----------
		markets: set of str
			Set of markets for images to be downloaded from
		records: int, optional
			The number of results to return for the bing image api
		start: int, optional
			The starting index for paginating the API response from bing API, 0 based index.
		"""
		self.filename_re = re.compile("&rf=(.*.jpg)")
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
		"""Add a merket region for downloading images from

		The provided market must fall into one of the pre-defined markets which are valid (self._all_markets) array.
		"""
		if market in self._all_markets:
	 		self.markets.add(market)
		else:
	 		raise Exception(f'{market} is not a valid market')

	def get_filename(self, url):
		"""Extracts actual file name from relativer url link returned by the bing image API"""
		matches = self.filename_re.search(url)
		return matches.group(1)



