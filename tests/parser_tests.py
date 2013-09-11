#coding: utf-8
from os.path import abspath, dirname, join
from catmat.parser import CatmatParser
from should_dsl import should, should_not
import unittest

ROOT_PATH = abspath(dirname(__file__))
TEST_TEMPLATE = join(ROOT_PATH, 'test_template.xml')

class TestCatmatParser(unittest.TestCase):

	def setUp(self):
		self.catmat_xml_parser = CatmatParser(TEST_TEMPLATE)

	def test_parser_returns_list_of_hashes(self):
		self.catmat_xml_parser.to_hash() |should| be_kind_of(list)

	def test_parsing_response_cannot_be_empty(self):
		self.catmat_xml_parser.to_hash() |should_not| be_empty

if __name__ == '__main__':
	unittest.main()