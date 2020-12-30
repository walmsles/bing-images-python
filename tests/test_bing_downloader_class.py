import inspect
from lib.BingDownloader import BingDownloader


def test_class_creation():
	assert inspect.isclass(BingDownloader)

	downloader = BingDownloader()

	assert isinstance(downloader, BingDownloader)

	# if not set passed in then expect default set defined by BingDownloader Class (all_markets)
	assert downloader.markets == { "en-US", "zh-CN", "ja-JP", "en-AU", "en-UK", "de-DE", "en-NZ", "en-CA" }
	assert downloader.markets == downloader.all_markets

def test_class_constructor():
	# test specific markets only
	downloader = BingDownloader({'en-US','en-AU'})
	assert downloader.markets == {'en-US','en-AU'}
