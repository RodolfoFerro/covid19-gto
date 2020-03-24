from time import time
import json

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_img(img_url, img_name):
	"""Function to download image form URL.
	
	Parameters
	----------
	img_url : str
		The URL pointing to the image that will be downloaded.
	img_name : str
		The name for the image to be saved.
	
	Returns
	-------
	bool
		A `True` flag, if the image was successfuly downloaded.
	"""

	pic = False
	response = requests.get(img_url, stream=True)
	with open(img_name, 'wb') as file:
		for chunk in response.iter_content():
			file.write(chunk)
		pic = True
	response.close()
	
	return pic


def scraper():
	"""Simulates a browser search on the official state site."""

	start = time()
	opts = Options()
	opts.headless = True

	driver = webdriver.Chrome(options=opts, executable_path='./chromedriver')
	driver.get('https://coronavirus.guanajuato.gob.mx/')

	# Download totals
	data = driver.find_elements_by_class_name('datos-num')
	numbers = [int(num.text) for num in data]
	numbers = {
		"descartados": numbers[0],
		"investigacion": numbers[1],
		"confirmados": numbers[2],
		"comunitarios": numbers[3]
	}

	# Download table
	img = driver.find_element_by_class_name('datos-covid19dosdos')	
	img_url = img.get_attribute('src')
	get_img(img_url, 'table.jpg')

	driver.quit()
	end = time()
	print("Total time:", end - start)

	with open('numbers.json', 'w') as outfile:
		json.dump(numbers, outfile, indent=4)

	return


if __name__ == "__main__":
	scraper()
