import datetime


class NasaClient:
	"""
	NasaClient class, upon being called by OutputGenerator class, interacts with HttpClient class to
	generate the API response for each day in the range of last 10 days and with FileCache class to
	store the generate API responses in the required format in the cache

	Attributes
	----------
	date: date
		a date of date type. (Default - current date)
	dayLimit: int
		the number of days for which the API response should be generated. (Default 10)
	imageLimit: int
		the number of images per day to be displayed. (Default 3)
	http_client : an instance of class HttpClient
		An instance of HttpClient used to request a response from the given URI
	cache_client: an instance of class FileCache
		An instance of FileCache class used to retrieve data from the cache and store API responses to it
	list_of_last_ten_days: List
		Stores string formatted dates of 10 days from the current date

	Methods
	-------------
	generate_uri(given_date)
		Formats the URI string for a given date, where 'earth_date' = given_date and returns
		the formatted URI

	generate_list_of_last_ten_days(None)
		Generates 10 days from the current date and stores them in the object's attribute
		list_of_last_ten_days

	generate_response_data(None)
		This is the entry point method of the class. It is called by the OutputGenerator class
		Upon being called, it calls generate_list_of_last_ten_days, checks if cache is empty
		and if empty, generates API response for all the 10 days in the list and stores them in cache.
		If the cache is not empty, it checks for the dates in the list not present in the cache and generates
		API response only for missing dates and stores them in cache

	get_api_response(list)
		Takes in a list of dates and calls http_client.get_response() method for each date
		and returns a dictionary where each key denotes a date and value is the images for that date

	parse_response_images(response)
		Parses the API responses and returns the images as a list for that corresponding response

	store_response_in_cache(response)
		Stores given response in the cache(file)
	"""

	def __init__(self, date, dayLimit, imageLimit, http_client, cache_client):
		self.date = date
		self.dayLimit = dayLimit
		self.imageLimit = imageLimit
		self.http_client = http_client
		self.cache_client = cache_client
		self.list_of_last_ten_days = []

	@staticmethod
	def generate_uri(given_date):
		uri_for_given_date = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={given_date}&camera=NAVCAM&api_key=DEMO_KEY"
		return uri_for_given_date

	def generate_list_of_last_ten_days(self):
		for number in range(self.dayLimit):
			single_day = self.date - datetime.timedelta(days=number)
			self.list_of_last_ten_days.append(str(single_day))

	def generate_response_data(self):
		"""Generates list of last 10 days, checks if cache is empty. If empty, stores API responses in it.
		If not empty, checks cache for the date, generates response if date not found,
		and stores in cache"""
		self.generate_list_of_last_ten_days()
		is_file_empty = self.cache_client.is_file_empty()
		if is_file_empty:
			date_list = self.list_of_last_ten_days
			response_data = self.get_api_response(date_list)
			response_to_store_in_cache = response_data
		else:
			data_from_cache_file = self.cache_client.read_file()
			missing_dates = []
			for day in self.list_of_last_ten_days:
				if day not in data_from_cache_file:
					missing_dates.append(day)
			missing_dates_response_data = self.get_api_response(missing_dates)
			response_to_store_in_cache = {**missing_dates_response_data, **data_from_cache_file}
		self.store_response_in_cache(response_to_store_in_cache)

	def get_api_response(self, list_of_dates):
		"""Calls HttpClient to get a response from the API"""
		response = dict()
		for day in list_of_dates:
			uri = self.generate_uri(day)
			api_response = self.http_client.get_response(uri)
			images_from_response = self.parse_response_images(api_response)
			response[day] = images_from_response
		return response

	def parse_response_images(self, api_response):
		"""If the number of images in a response are less than the limit for images to be displayed,
		it returns only the available number of images """
		given_limit = self.imageLimit
		images_in_response = list()
		photos = api_response.json()['photos']
		actual_limit = min(len(photos), given_limit)
		for i in range(actual_limit):
			images_in_response.append(photos[i]['img_src'])
		return images_in_response

	def store_response_in_cache(self, response_data):
		self.cache_client.write_to_file(response_data)
