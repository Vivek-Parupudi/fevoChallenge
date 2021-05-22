from challenge.http.httpClient import HttpClient
from challenge.nasa.nasaClient import NasaClient
from challenge.output.outputGenerator import OutputGenerator
from challenge.cache.fileCache import FileCache

import datetime

if __name__ == "__main__":
	today_date = datetime.date.today()
	dayLimit = 10
	imageLimit = 3

	http_client = HttpClient()
	cache_client = FileCache()
	nasa_api_client = NasaClient(today_date, dayLimit, imageLimit, http_client, cache_client)
	output_generator_client = OutputGenerator(nasa_api_client, cache_client, dayLimit)

	print(output_generator_client.print_response())
