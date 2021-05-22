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

	def test_output_display(self):
		output_json = \
			{
				"2021-05-21": [],
				"2021-05-20": [],
				"2021-05-19": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03123/opgs/edr/ncam/NLB_674737022EDR_F0880366NCAM00253M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03123/opgs/edr/ncam/NLB_674736991EDR_F0880366NCAM00253M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03123/opgs/edr/ncam/NLB_674736907EDR_F0880366NCAM00253M_.JPG"
				],
				"2021-05-18": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03122/opgs/edr/ncam/NLB_674658263EDR_F0880366NCAM00312M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03122/opgs/edr/ncam/NLB_674658239EDR_F0880366NCAM00312M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03122/opgs/edr/ncam/NLB_674658214EDR_F0880366NCAM00312M_.JPG"
				],
				"2021-05-17": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03121/opgs/edr/ncam/NRB_674557024EDR_S0880366NCAM00595M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03121/opgs/edr/ncam/NRB_674557011EDR_S0880366NCAM00595M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03121/opgs/edr/ncam/NRB_674556998EDR_S0880366NCAM00595M_.JPG"
				],
				"2021-05-16": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03120/opgs/edr/ncam/NLB_674478398EDR_F0880366NCAM00312M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03120/opgs/edr/ncam/NLB_674478374EDR_F0880366NCAM00312M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03120/opgs/edr/ncam/NLB_674478350EDR_F0880366NCAM00312M_.JPG"
				],
				"2021-05-15": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03119/opgs/edr/ncam/NLB_674396385EDR_F0880156NCAM00320M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03119/opgs/edr/ncam/NLB_674396017EDR_F0880156NCAM00207M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03119/opgs/edr/ncam/NLB_674395295EDR_F0880156NCAM00207M_.JPG"
				],
				"2021-05-14": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03118/opgs/edr/ncam/NRB_674297012EDR_S0880156NCAM00599M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03118/opgs/edr/ncam/NRB_674296987EDR_S0880156NCAM00599M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03118/opgs/edr/ncam/NRB_674296962EDR_S0880156NCAM00599M_.JPG"
				],
				"2021-05-13": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03117/opgs/edr/ncam/NLB_674212139EDR_F0880114NCAM00385M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03117/opgs/edr/ncam/NLB_674212115EDR_F0880114NCAM00385M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03117/opgs/edr/ncam/NRB_674212139EDR_F0880114NCAM00385M_.JPG"
				],
				"2021-05-12": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03116/opgs/edr/ncam/NLB_674114163EDR_F0880000NCAM00320M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03116/opgs/edr/ncam/NRB_674114163EDR_F0880000NCAM00320M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03116/opgs/edr/ncam/NRB_674115785EDR_S0880000NCAM00594M_.JPG"
				]
			}
		desired_output = json.dumps(output_json, indent=4)
		generated_display_output = outputGenerator.print_response()
		self.assertEqual(desired_output, generated_display_output)


if __name__ == "__main__":
	unittest.main()
