from string import Template 
import requests

bing_base_url = "https://bing.com"
list_images_url_template = Template('$base/HPImageArchive.aspx?format=js&idx=$start&n=$records&mkt=$market')

def get_list_images_url(market, records, start):
	"""creates the bing image web service query string for querying the API"""
	return list_images_url_template.substitute(base=bing_base_url, start=start, records=records, market=market)

def list_images(market, records, start):
	"""calls the bing image web service and returns a list of image urls from the web service"""
	url = get_list_images_url(market=market, records=records, start=start)
	response = requests.get(url)
	if response.status_code == 200:
		body = response.json()
		return list(map(lambda x: x['url'], body['images']))
	else:
		raise Exception(f'Unable to list images: {response.json()}')

def download_image(image_url, filename):
	"""downloads the partial relative image_url link into the provided filename """
	response = requests.get(f'{bing_base_url}{image_url}')

	save_image(response, filename)

	return filename

def save_image(api_response, filename):
	"""saves the data into the filename"""
	with open(filename, 'wb') as f:
		for chunk in api_response.iter_content(chunk_size=8192):
			f.write(chunk)
