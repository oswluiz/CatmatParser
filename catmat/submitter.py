# coding: utf-8
from xml.etree import ElementTree as ET
from catmat.parser import CatmatParser
from os.path import join, abspath, dirname
import requests

ROOT_PATH = join(abspath(dirname(__file__)))

class Submitter(object):

    def __init__(self, cpf=1, password=1):
        url = "http://www.comprasnet.gov.br/XML"
        self.production_url = join(url, "producao/consultamatserv.asp")
        self.development_url = join(url, "treinamento/consultamatserv.asp")
        self.__input_xml_path = join(ROOT_PATH, 'input_template.xml')
        tree = ET.parse(self.__input_xml_path)
        self.__cpf = cpf
        self.__password = password
        self.__root = tree
        self.__data = []

    def _get_xml_input_by_radical(self, radical1, radical2='', radical3=''):
        codigo = ''
        return open(self.__input_xml_path, 'rw').read() %(self.__cpf, self.__password, 
                                                         codigo, radical1, radical2, radical3)

    def _get_xml_input_by_cod(self, codigo):
        radical1, radical2, radical3 = '', '', ''
        return open(self.__input_xml_path, 'rw').read() %(self.__cpf, self.__password, 
                                                         codigo, radical1, radical2, radical3)

    def _post_data(self, input_xml):
        param_data = {'xml': input_xml}
        output_xml = requests.post(self.development_url, data=param_data)
        output_xml_string = output_xml.text.encode('utf-8')
        return CatmatParser(output_xml_string)

    def get_by_radical(self, radical1, radical2='', radical3=''):
        input_xml = self._get_xml_input_by_radical(radical1, radical2, radical3)
        return self._post_data(input_xml).to_hash()

    def get_by_cod(self, codigo):
        input_xml = self._get_xml_input_by_cod(codigo)
        return self._post_data(input_xml).to_hash()
