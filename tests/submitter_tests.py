#coding: utf-8
from os.path import abspath, dirname, join
import sys

ROOT_PATH = join(abspath(dirname(__file__)), '..')
sys.path.append(ROOT_PATH)

from catmat.submitter import Submitter
from should_dsl import should, should_not
import unittest

ROOT_PATH = abspath(dirname(__file__))
TEST_TEMPLATE = join(ROOT_PATH, 'test_template.xml')

class TestSubmitter(unittest.TestCase):

	def setUp(self):
		self.submitter = Submitter(cpf=123, password=321)

	def test_xml_inputter_returns_requires_at_least_one_arg(self):
		self.submitter._input_xml('foo') |should_not| be_empty

	def test_xml_inputter_returns_a_string(self):
		self.submitter._input_xml('FOO', 'BAR', 'SUP') |should| be_kind_of(str)

	def test_post_xml_returns_a_list_of_hashes(self):
		self.submitter.post_xml('lapis', 'preto') |should| be_kind_of(list)

if __name__ == '__main__':
	unittest.main()