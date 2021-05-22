import json
import os


class FileCache:
	"""
	FileCache class is the interface through which the other classes access the file cache stored
	in 'cache.json' file

	Attributes
	__________
	None

	Methods
	_______
	read_file(None)
		Reads the json file and returns a dictionary of responses where key is the date and
		list of images for that date is the value

	is_file_empty(None)
		Checks if the file cache is empty. Returns the truth value of the check

	write_to_file(data)
		Writes the data passed in a dictionary format to the file cache. Returns None

	"""

	absolute_path = os.path.dirname(os.path.abspath(__file__))
	file_path = absolute_path + '/cache.json'

	def __init__(self):
		pass

	@staticmethod
	def read_file():
		with open(FileCache.file_path, 'r') as file_reader:
			file_content = json.load(file_reader)
			return file_content

	@staticmethod
	def is_file_empty():
		file_size = os.path.getsize(FileCache.file_path)
		return True if file_size == 0 else False

	@staticmethod
	def write_to_file(data):
		with open(FileCache.file_path, 'w') as file_writer:
			json.dump(data, file_writer, indent=4)
