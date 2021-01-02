import os
import os.path
from bing_images.Downloader import Downloader


if __name__ == "__main__":
	image_path = os.environ.get('BING_IMAGE_PATH')
	if image_path == None:
		print('Failed: BING_IMAGE_PATH env var not defined')
		exit(-1)
	if not os.path.isdir(image_path):
		print('Failed: BING_IMAGE_PATH does not exist')
		exit(-1)
	
	downloader = Downloader(image_path=image_path)
	downloader.download_all()
		

