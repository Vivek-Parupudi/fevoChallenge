import requests


class HttpClient:
	""""
	HttpClient class is the interface through which the NasaClient class interacts. It calls the API to
	generate a response for the URI

	Attributes
	__________
	None

	Methods
	______
	get_response(url)
		It takes in a URI and generates a response from the NASA API
	"""

	def __init__(self):
		pass

	@staticmethod
	def get_response(url):
		response = requests.get(url)
		if response.status_code == 200:
			return response
		else:
			return "Exception occurred"
