from string import Template 
import requests

bing_base_url = "https://bing.com"
list_images_url_template = Template('$base/HPImageArchive.aspx?format=js&idx=$start&n=$records&mkt=$market')

def get_list_images_url(market, records, start):
	return list_images_url_template.substitute(base=bing_base_url, start=start, records=records, market=market)

def list_images(market, records, start):
	url = get_list_images_url(market=market, records=records, start=start)
	return requests.get(url)
