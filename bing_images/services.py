from string import Template 
import requests

bing_base_url = "https://bing.com"
list_images_url_template = Template('$base/HPImageArchive.aspx?format=js&idx=$start&n=$records&mkt=$market')

def get_list_images_url(market, records, start):
	"""creates the bing image web service query string for querying the API"""
	return list_images_url_template.substitute(base=bing_base_url, start=start, records=records, market=market)

def list_images(market, records, start):
	"""calls the bing image web service and returns the response object"""
	url = get_list_images_url(market=market, records=records, start=start)
	return requests.get(url)

def download_image(image_url, filename):
	"""downloads the partial relative image_url link into the provided filename """
	response = requests.get(f'{bing_base_url}/{image_url}')

	with open(filename, 'wb') as f:
		for chunk in response.iter_content(chunk_size=8192):
			f.write(chunk)

	return filename