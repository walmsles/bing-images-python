import inspect
import pytest
from bing_images.Downloader import Downloader

def test_class_creation():
	assert inspect.isclass(Downloader)

	downloader = Downloader()

	assert downloader.records == 100
	assert downloader.start == 0

	assert isinstance(downloader, Downloader)

	# if not set passed in then expect default set defined by BingDownloader Class (all_markets)
	assert downloader.markets == { "en-US", "zh-CN", "ja-JP", "en-AU", "en-UK", "de-DE", "en-NZ", "en-CA" }
	assert downloader.markets == downloader._all_markets

def test_class_constructor():
	# test specific markets only
	downloader = Downloader(markets={'en-US','en-AU'}, records=10, start=2)
	assert downloader.markets == {'en-US','en-AU'}
	assert downloader.records == 10
	assert downloader.start == 2

def test_add_market():
	downloader = Downloader({})
	downloader.add_market('en-AU')
	assert 'en-AU' in downloader.markets

	# check error condition
	with pytest.raises(Exception) as e:
		downloader.add_market(None)

	assert 'None is not a valid market' == str(e.value)

	market = 'EN-AU'
	with pytest.raises(Exception) as e:
		downloader.add_market(market)

	assert f'{market} is not a valid market' == str(e.value) 

