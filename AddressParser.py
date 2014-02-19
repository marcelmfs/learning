# coding: utf-8

from NerCnefe import *
from Number2Words import *
		
class AddressParser:
	"""
	Brazilian postal address parser class. It expects CSV with 6 fields as input:
		1st: Address
		2nd: Complement
		3rd: zipcode
		4th: Neighborhood
		5th: City
		6th: State Code
	"""
	def __init__(self,input):
		self.fieldnames=('ENDEREÇO','COMPLEMENTO','CEP','BAIRRO','CIDADE','ESTADO')
		self.rawinput=input.rstrip()
		self.input=self.rawinput.replace('"','').replace('.',' ').replace(',',' ').upper()
		self.fields=self.input.split(';')
		self.address_tokens=[" ".join(n.split()).split(' ') for n in self.fields]
		self.uf=self.address_tokens[-1]
		self.municipio=self.address_tokens[-2]

	def normalize(self,*multipleArrays):
		""" method to normalize output """
		out = []
		for a in self.address_tokens[0:5]:
			output = []
			for word in a:
				if word in abbr:
					output.append(abbr[word])
				elif word in corrections:
					output.append(corrections[word])
				elif self.uf == 'DF':
					if word in bsb:
						output.append(bsb[word])
					else:
						output.append(word)
				else:
					output.append(word)
			out.append(output)
		out.append(self.address_tokens[-1])
		if multipleArrays:
			return out
		else:
			return [j for i in out for j in i]

	def strip(self):
		""" method to strip input to address constituents after normalizing it """
		out = {}
		count = 0
		for array in self.normalize(1):
			out[self.fieldnames[count]] = " ".join(array)
			count = count + 1
		return out

	def numbers(self):
		""" try to determine the number from the address or from complement """
		number = 0




