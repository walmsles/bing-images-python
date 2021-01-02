import pytest
import bing_images.utils as utils

def test_get_image_path(mocker):
	# test environment variable not there
	mocker.patch('os.environ.get', return_value=None)
	with pytest.raises(Exception) as e:
		path = utils.get_image_path()

	assert 'Failed: BING_IMAGE_PATH env var not defined' == str(e.value)

	mocker.patch('os.environ.get', return_value='test/path/image_path')
	mocker.patch('os.path.isdir', return_value=False)
	with pytest.raises(Exception) as e:
		path = utils.get_image_path()

	assert 'Failed: BING_IMAGE_PATH (test/path/image_path) does not exist' == str(e.value)

	mocker.patch('os.path.isdir', return_value=True)
	path = utils.get_image_path()

	assert path == 'test/path/image_path'


