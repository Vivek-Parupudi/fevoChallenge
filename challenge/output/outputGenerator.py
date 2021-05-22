import json


class OutputGenerator:
	""""
	OutputGenerator Class interacts with the NasaClient class to generate API responses
	and with FileCache class to read data from the file cache and display it.

	Attributes
	__________
	nasa_api_client: An instance of NasaClient class
	cache_client: An instance of FileCache class
	dayLimit: int
		the number of days for which the API response should be generated. (Default 10)

	Methods
	_______
	print_response(None)
		This is the entry point method called from the main.py file. It calls the NasaClient class
		to generate and store API response in cache. And the reads the file cache to display the data
		with dates and the images generated for that date.
	"""
	def __init__(self, nasa_api_client, cache_client, dayLimit):
		self.nasa_api_client = nasa_api_client
		self.cache_client = cache_client
		self.dayLimit = dayLimit

	def print_response(self):
		"""Before printing the data from the file cache it trims the data to display only the
		first 10 items in the cache"""
		self.nasa_api_client.generate_response_data()
		file_content = self.cache_client.read_file()
		if len(file_content) > self.dayLimit:
			while len(file_content) != self.dayLimit:
				file_content.popitem()
		return json.dumps(file_content, indent=4)
