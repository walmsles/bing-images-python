import inspect
from lib.BingDownloader import BingDownloader


def test_class_creation():
	assert inspect.isclass(BingDownloader)
	downloader = BingDownloader()
	assert isinstance(downloader, BingDownloader)
	assert downloader.markets == set()

def test_class_constructor():
	downloader = BingDownloader({'en-US','en-AU'})
	assert downloader.markets == {'en-US','en-AU'}

def test_add_market():
	
