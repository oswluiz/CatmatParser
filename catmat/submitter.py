from xml.etree import ElementTree as ET
from splinter import Browser
from os.path import join
import urllib2

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

    def input_xml(self, radical1, radical2, radical3):
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
    	xml_string = ET.tostring(root, encoding="UTF-8")
    	return xml_string

	def post(self, url, data, contenttype):
		request = urllib2.Request(url, data)
		request.add_header('Content-Type', contenttype)
		response = urllib2.urlopen(request)
		return response.read()

	def post_xml(radical1, radical2, radical3):
		url = self.production_url
		data = input_xml(radical1, radical2, radical3)
		return post(url, data, "text/xml")
