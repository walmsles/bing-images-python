from bing_images.Downloader import Downloader
import bing_images.utils as utils

if __name__ == "__main__": # pragma: no cover
	"""Everything in main must be imported from a unti tested file - anything in main is excluded from coverage reports"""
	downloader = Downloader(image_path=utils.get_image_path())
	downloader.download_all()
