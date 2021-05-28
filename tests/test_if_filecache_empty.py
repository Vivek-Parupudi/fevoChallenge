import sys
import unittest

sys.path.append('../')

from challenge.cache.fileCache import FileCache

cacheClient = FileCache()


class TestFileEmpty(unittest.TestCase):
	def test_file_empty(self):
		is_file_empty = cacheClient.is_file_empty()
		self.assertEqual(False, is_file_empty)


if __name__ == "__main__":
	unittest.main()
