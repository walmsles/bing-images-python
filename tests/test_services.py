import pytest
import os.path
import os
import responses
import bing_images.services as services

# Tests for web service interactions that are isolated out to seperate utility file

def test_get_list_images_url():
	url = services.get_list_images_url(market='en-AU', records=10, start=0)
	assert url == 'https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=en-AU'

@responses.activate
def test_list_images():
	# setup mock response
	responses.add(
		responses.GET,
		"https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=2&mkt=en-AU",
		json={"images":[{"startdate":"20201231","fullstartdate":"202012311300","enddate":"20210101","url":"/th?id=OHR.LoonyDook_EN-AU4013491478_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp","urlbase":"/th?id=OHR.LoonyDook_EN-AU4013491478","copyright":"Polar bear in waters off Svalbard, Norway (© Westend61/Getty Images)","copyrightlink":"https://www.bing.com/search?q=new+year%27s+day&form=hpcapt&filters=HpDate%3a%2220201231_1300%22","title":"Take the plunge into 2021","quiz":"/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20201231_LoonyDook%22&FORM=HPQUIZ","wp":True,"hsh":"f3462ea46d71f2c3c7ebdfda3db041af","drk":1,"top":1,"bot":1,"hs":[]},{"startdate":"20201230","fullstartdate":"202012301300","enddate":"20201231","url":"/th?id=OHR.ZaragozaSpain_EN-AU9226372489_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp","urlbase":"/th?id=OHR.ZaragozaSpain_EN-AU9226372489","copyright":"Fireworks during a New Year's Eve celebration in Zaragoza, Spain (© Martina Badini/Shutterstock)","copyrightlink":"https://www.bing.com/search?q=new+years+eve&form=hpcapt&filters=HpDate%3a%2220201230_1300%22","title":"Goodbye, 2020!","quiz":"/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20201230_ZaragozaSpain%22&FORM=HPQUIZ","wp":True,"hsh":"94a94bf792bca917b87ec6cc2c9059c9","drk":1,"top":1,"bot":1,"hs":[]}],"tooltips":{"loading":"Loading...","previous":"Previous image","next":"Next image","walle":"This image is not available to download as wallpaper.","walls":"Download this image. Use of this image is restricted to wallpaper only."}},
		status=200
	)

	response = services.list_images(market='en-AU', records=2, start=0)
	response_json = response.json()

	assert response.status_code == 200
	assert 'images' in response_json.keys()
	assert len(response_json['images']) == 2

@responses.activate
def test_download_image():

	responses.add(
		responses.GET,
		"https://bing.com/th?id=OHR.LoonyDook_EN-AU4013491478_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp",
		status=200,
		body="file content"
	)

	url = '/th?id=OHR.LoonyDook_EN-AU4013491478_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'
	filename = 'filename.jpg'
	services.download_image(url, filename)
	assert os.path.isfile(filename)

	os.remove(filename)





