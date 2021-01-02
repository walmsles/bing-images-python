# bing-cli [![Build Status](https://travis-ci.com/walmsles/bing-cli-python.svg?branch=main)](https://travis-ci.com/walmsles/bing-cli-python)
bing-cli is a simple program with the following requirements: 

```
Write a program to call the Microsoft Bing desktop Image API for one or more defined market codes and
download the images which have not already been downloaded to a defined download directory.  
The following should be configurable:

	* Number of records returned by the web service
	* location of files to be downloaded

An already downloaded file should never be downloaded again.
```


## goals of bing-cli
bing-cli is a simple program which involves use of a JSON web service API as well as local file system manipulations to determine files to be downloaded as well as actual downloading of file content from the web service result. Tthe idea of this simple program is to:

* be used as a way of learning different programming languages
* be used as a way of learning TDD concepts for the chosen language including mocking of remote services
* download images for personal use

# bing-cli-python
An implementation of bing-cli using the python language