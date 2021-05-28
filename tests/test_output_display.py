import datetime
import json
import sys
import unittest

sys.path.append('../')

from challenge.http.httpClient import HttpClient
from challenge.nasa.nasaClient import NasaClient
from challenge.output.outputGenerator import OutputGenerator
from challenge.cache.fileCache import FileCache

today = datetime.date.today()
dayLimit = 10
imageLimit = 3

httpClient = HttpClient()
cacheClient = FileCache()
nasaApiClient = NasaClient(today, dayLimit, imageLimit, httpClient, cacheClient)
outputGenerator = OutputGenerator(nasaApiClient, cacheClient, dayLimit)
uri = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2021-05-18&camera=NAVCAM&api_key=DEMO_KEY"


class TestOutput(unittest.TestCase):
	def test_output_display(self):
		output_json = \
			{
				"2021-05-25": [],
				"2021-05-24": [],
				"2021-05-23": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03127/opgs/edr/ncam/NRB_675072523EDR_S0880366NCAM00567M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03127/opgs/edr/ncam/NRB_675072485EDR_S0880366NCAM00567M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03127/opgs/edr/ncam/NRB_675072447EDR_S0880366NCAM00567M_.JPG"
				],
				"2021-05-22": [],
				"2021-05-21": [
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03125/opgs/edr/ncam/NRB_674930007EDR_F0880366NCAM00551M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03125/opgs/edr/ncam/NRB_674929967EDR_F0880366NCAM00551M_.JPG",
					"https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03125/opgs/edr/ncam/NRB_674929927EDR_F0880366NCAM00551M_.JPG"
				],
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
				]
			}
		desired_output = json.dumps(output_json, indent=4)
		generated_display_output = outputGenerator.print_response()
		self.assertEqual(desired_output, generated_display_output)


if __name__ == "__main__":
	unittest.main()
