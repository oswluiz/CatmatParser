#coding: utf-8
from xml.etree import ElementTree as ET

class CatmatParser(object):

    def __init__(self, xml_string):
        self.__access_error = xml_string
        self.__tree = ET.fromstring(xml_string)
        self.__data = []

    def to_hash(self):
        itens = self.__tree.find('itens')
        if itens is not None:
            for item in itens.findall('item'):
                hash_data = {}
                unidades = []
                codigo = item.find('codigo').text
                descricao = item.find('descricao').text.strip().encode('ISO-8859-1')
                descricao_resumida = item.find('descricaoPDM').text.strip().encode('ISO-8859-1')
                for unidade in item.find('unidades').findall('unidade'):
                    unidades.append([unidade.find('sigla_unidade_fornecimento').text.strip(),
                                     unidade.find('capacidade').text.strip(),
                                     unidade.find('unidade_medida').text.strip()])
                hash_data['codigo']               = codigo
                hash_data['descricao']            = descricao
                hash_data['descricao_resumida']   = descricao_resumida
                hash_data['unidades']             = unidades
                self.__data.append(hash_data)
        else:
            raise ValueError(self.__access_error)
        return self.__data
