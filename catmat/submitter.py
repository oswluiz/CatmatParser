# coding: utf-8
from xml.etree import ElementTree as ET
from catmat.parser import CatmatParser
from os.path import join
import requests

class Submitter(object):

    def __init__(self, cpf=1, password=1):
        url = "http://www.comprasnet.gov.br/XML"
        self.production_url = join(url, "producao/consultamatserv.asp")
        self.development_url = join(url, "treinamento/consultamatserv.asp")
        self.__tree = ET.parse('catmat/input_template.xml')
        self.__cpf = cpf
        self.__password = password
        self.__root = self.__tree.getroot()
        self.__data = []

    
    def material_hash(self, radical1, radical2='', radical3=''):
        self.__r1, self.__r2, self.__r3 = radical1, radical2, radical3

        def _input_xml(self):
            xml_string = """<?xml version="1.0" encoding="ISO-8859-1"?>
                                <cnet xmlns="cnet_consultamatserv">
                                <ambiente>treinamento</ambiente>
                                <sistema>XML</sistema>
                                <cpf>%s</cpf>
                                <senha>%s</senha>
                                <acao>consulta material</acao>
                                <codigo_item></codigo_item>
                                <radical1>%s</radical1>
                                <radical2>%s</radical2>
                                <radical3>%s</radical3>
                                <sustentavel></sustentavel>
                            </cnet>""" %(self.__cpf, self.__password, self.__r1, self.__r2, self.__r3)
            return xml_string

        def _post_xml(self):
            input_xml = self._input_xml(self.__r1, self.__r2, self.__r3)
            param_data = {'xml': input_xml}
            
            output_xml = requests.post(self.development_url, data=param_data)
            output_xml_string = output_xml.text.encode('utf-8')
            self.__parse = CatmatParser(output_xml_string)
            self.__parse.to_hash()


    
