from xml.etree import ElementTree as ET
from splinter import Browser
from os.path import join

class Submitter(object):

    def __init__(self, cpf, password):
    	url = "http://www.comprasnet.gov.br/XML"
    	self.production_url = join(url, "producao/consultamatserv.asp")
        self.development_url = join(url, "treinamento/consultamatserv.asp")
        self.__tree = ET.parse('catmat/input_template.xml')
        self.__cpf = cpf
        self.__password = password
        self.__root = self.__tree.getroot()
        self.__data = []

    def write_input_xml(self, radical1, radical2, radical3):
    	root         = self.__root
    	prefix_tag   = "{cnet_consultamatserv}"
    	cpf_tag      = root.find('%scpf' %prefix_tag)
    	password_tag = root.find('%ssenha' %prefix_tag)
    	r1_tag       = root.find('%sradical1' %prefix_tag)
    	r2_tag       = root.find('%sradical2' %prefix_tag)
    	r3_tag       = root.find('%sradical3' %prefix_tag)

    	# Writing Authentication params
    	cpf_tag.text, password_tag.text = self.__cpf, self.__password

    	# Writing radicals
    	r1_tag.text, r2_tag.text, r3_tag.text = radical1, radical2, radical3

    	self.__tree.write('temp_input.xml')

    def submit_xml(self):
    	pass
