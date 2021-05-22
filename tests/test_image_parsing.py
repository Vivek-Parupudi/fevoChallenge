from challenge.http.httpClient import HttpClient
from challenge.nasa.nasaClient import NasaClient
from challenge.cache.fileCache import FileCache

import datetime
import sys
import unittest

sys.path.append('..')

today = datetime.date.today()
dayLimit = 10
imageLimit = 3

httpClient = HttpClient()
cacheClient = FileCache()
nasaApiClient = NasaClient(today, dayLimit, imageLimit, httpClient, cacheClient)
uri = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2021-05-18&camera=NAVCAM&api_key=DEMO_KEY"


class TestImageParsing(unittest.TestCase):
	def test_image_parsing(self):
		response = httpClient.get_response(uri)
		desired_parsed_images = [
			"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03122/opgs/edr/ncam/NLB_674658263EDR_F0880366NCAM00312M_.JPG",
			"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03122/opgs/edr/ncam/NLB_674658239EDR_F0880366NCAM00312M_.JPG",
			"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03122/opgs/edr/ncam/NLB_674658214EDR_F0880366NCAM00312M_.JPG"
		]
		generated_parsed_images = nasaApiClient.parse_response_images(response)
		self.assertEqual(desired_parsed_images, generated_parsed_images)


if __name__ == "__main__":
	unittest.main()
