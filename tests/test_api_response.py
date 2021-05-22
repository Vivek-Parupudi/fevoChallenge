from challenge.http.httpClient import HttpClient
from challenge.nasa.nasaClient import NasaClient
from challenge.output.outputGenerator import OutputGenerator
from challenge.cache.fileCache import FileCache

import datetime
import json
import sys
import unittest

sys.path.append('..')

today = datetime.date.today()
dayLimit = 10
imageLimit = 3

httpClient = HttpClient()
cacheClient = FileCache()
nasaApiClient = NasaClient(today, dayLimit, imageLimit, httpClient, cacheClient)
outputGenerator = OutputGenerator(nasaApiClient, cacheClient, dayLimit)
uri = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2021-05-18&camera=NAVCAM&api_key=DEMO_KEY"


class TestApiResponse(unittest.TestCase):
	def test_response_code(self):
		response = httpClient.get_response(uri)
		self.assertEqual(200, response.status_code)


if __name__ == "__main__":
	unittest.main()
