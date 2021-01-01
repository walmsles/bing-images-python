import pytest
import bing_images.services as services

# Tests for web service interactions that are isolated out to seperate utility file

def test_get_list_images_url():
	url = services.get_list_images_url(market='en-AU', records=10, start=0)
	assert url == 'https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=en-AU'

def test_list_images():
	response = services.list_images(market='en-AU', records=2, start=0)
	response_json = response.json()

	assert response.status_code == 200
	assert 'images' in response_json.keys()
	assert len(response_json['images']) == 2
