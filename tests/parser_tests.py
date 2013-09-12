#coding: utf-8
from os.path import abspath, dirname, join
import sys

ROOT_PATH = join(abspath(dirname(__file__)), '..')
TEST_TEMPLATE = join(ROOT_PATH, 'tests', 'test_template.xml')
sys.path.append(ROOT_PATH)

from catmat.parser import CatmatParser
from should_dsl import should, should_not
import unittest

class TestCatmatParser(unittest.TestCase):

	def setUp(self):
		xml_string = open(TEST_TEMPLATE).read()
		self.catmat_parser = CatmatParser(xml_string)

	def test_parser_instance_should_accept_strings(self):
		self.catmat_parser |should| be_kind_of (CatmatParser)

	def test_parser_tohash_method_returns_something(self):
		self.catmat_parser.to_hash() |should_not| be_empty

	def test_parser_tohash_method_returns_a_list_of_hashes(self):
		self.catmat_parser.to_hash() |should| be_kind_of (list)

if __name__ == '__main__':
	unittest.main()