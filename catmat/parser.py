from xml.etree import ElementTree as ET

class CatmatParser(object):

    def __init__(self, template_url):
        tree = ET.parse(template_url)
        self.__root = tree.getroot()
        self.__data = []

    def to_hash(self):
        for item in self.__root.find('itens').findall('item'):
            hash_data = {}
            unidades = []
            descricao = item.find('descricao').text
            for unidade in item.find('unidades').findall('unidade'):
                unidades.append([unidade.find('sigla_unidade_fornecimento').text,
                                 unidade.find('capacidade').text,
                                 unidade.find('unidade_medida').text])
            hash_data['descricao'] = descricao
            hash_data['unidades']  = unidades
            self.__data.append(hash_data)
        return self.__data
                