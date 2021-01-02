import inspect
import pytest
import os.path
from unittest.mock import call
from bing_images.Downloader import Downloader


def test_class_creation():
	assert inspect.isclass(Downloader)

	downloader = Downloader()

	assert downloader.records == 100
	assert downloader.start == 0

	assert isinstance(downloader, Downloader)

	# if not set passed in then expect default set defined by BingDownloader Class (_valid_markets)
	assert downloader.markets == { "en-US", "zh-CN", "ja-JP", "en-AU", "en-UK", "de-DE", "en-NZ", "en-CA" }
	assert downloader.markets == downloader._valid_markets

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
	assert len(downloader.markets) == 1

	# check error condition
	with pytest.raises(Exception) as e:
		downloader.add_market(None)

	assert 'None is not a valid market' == str(e.value)

	market = 'EN-AU'
	with pytest.raises(Exception) as e:
		downloader.add_market(market)

	assert f'{market} is not a valid market' == str(e.value) 

def test_get_filename():
	downloader = Downloader()

	filename = downloader.get_filename('/th?id=OHR.LoonyDook_EN-AU4013491478_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp')

	assert filename == 'LoonyDook.jpg'


def test_download_all(mocker):
	"""Test Downloader.download_all driver function using service mocks"""
	download_mock = mocker.patch('bing_images.services.download_image', return_value='filename.jpg')
	list_mock = mocker.patch('bing_images.services.list_images', return_value=["/download1?id=OHR.filenameAA_xxxxstuff.jpg&pid=hp&rf=filename.jpg","/download2?id=OHR.filenameBB_yyymorestuff.jpg&hp&rf=filename2.jpg"])
	isfile_mock = mocker.patch('os.path.isfile', return_value=False)

	downloader = Downloader(markets={'en-AU', 'en-US'}, records=2, start=3, image_path="images")

	downloader.download_all()

	download_mock.assert_has_calls([call("/download1?id=OHR.filenameAA_xxxxstuff.jpg&pid=hp&rf=filename.jpg","images/filenameAA.jpg"), call("/download2?id=OHR.filenameBB_yyymorestuff.jpg&hp&rf=filename2.jpg","images/filenameBB.jpg")])
	list_mock.assert_has_calls([call('en-AU', 2, 3), call('en-US', 2, 3)], any_order=True)

def test_no_repeat_download(mocker):
	download_mock = mocker.patch('bing_images.services.download_image', return_value='filename.jpg')
	list_mock = mocker.patch('bing_images.services.list_images', return_value=["/download1?id=OHR.filenameAA_xxxxstuff.jpg&pid=hp&rf=filename.jpg","/download2?id=OHR.filenameBB_yyymorestuff.jpg&hp&rf=filename2.jpg"])

	# patch isfile to always return true - should not try to download any files
	isfile_mock = mocker.patch('os.path.isfile', return_value=True)
	downloader = Downloader(markets={'en-AU', 'en-US'}, records=2, start=3, image_path="images")

	downloader.download_all()

	download_mock.assert_not_called()
	isfile_mock.assert_has_calls([call("images/filenameAA.jpg"), call("images/filenameBB.jpg")])
	list_mock.assert_has_calls([call('en-AU', 2, 3), call('en-US', 2, 3)], any_order=True)





