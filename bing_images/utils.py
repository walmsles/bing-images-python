import os
import os.path

def get_image_path():
	"""get image path from environment var and validate it is a valid folder"""
	image_path = os.environ.get('BING_IMAGE_PATH')
	if image_path == None:
		raise Exception('Failed: BING_IMAGE_PATH env var not defined')
		
	if not os.path.isdir(image_path):
		raise Exception(f'Failed: BING_IMAGE_PATH ({image_path}) does not exist')

	return image_path