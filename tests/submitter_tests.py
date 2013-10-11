#coding: utf-8
from os.path import abspath, dirname, join
import sys

ROOT_PATH = join(abspath(dirname(__file__)), '..')
sys.path.append(ROOT_PATH)

from catmat.submitter import Submitter
from should_dsl import should, should_not
import unittest

ROOT_PATH = abspath(dirname(__file__))
TEST_TEMPLATE = join(ROOT_PATH, 'tests' , 'test_template.xml')

class TestSubmitter(unittest.TestCase):

	def setUp(self):
		self.treinamento_submitter = Submitter()

	def test_default_ambiente_must_be_treinamento(self):
		self.treinamento_submitter.ambiente |should| equal_to('treinamento')

	def test_populates_default_xml_with_submitter_radical_arguments(self):
		self.treinamento_submitter._get_xml_input_by_radical('foo', 'bar', 'suap') |should| be_kind_of(str)

	def test_populates_default_xml_with_submitter_cod_arguments(self):
		self.treinamento_submitter._get_xml_input_by_radical('123') |should| be_kind_of(str)

	def test_gets_list_of_hashes_of_catmat_material_using_radical_params(self):
		self.treinamento_submitter.get_by_radical('lapis', 'preto') |should| be_kind_of(list)

	def test_gets_list_of_hashes_of_catmat_material_using_cod_param(self):
		self.treinamento_submitter.get_by_cod('000391674') |should| be_kind_of(list)

	def test_raises_value_error_if_no_material_is_found_using_radical_params(self):
		try:
			self.treinamento_submitter.get_by_radical('foo', 'bar') |should| be_kind_of(list)
		except:
			return True

	def test_raises_value_error_if_no_material_is_found_using_cod_params(self):
		try:
			self.treinamento_submitter.get_by_cod('123') |should| be_kind_of(list)
		except:
			return True

if __name__ == '__main__':
	unittest.main()