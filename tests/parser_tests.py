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

if __name__ == '__main__':
	unittest.main()