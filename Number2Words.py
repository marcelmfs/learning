class Number2Words(object):

	def __init__(self):
		'''Initialise the class with useful data'''

		self.wordsDict = {1: 'UM', 2: 'DOIS', 3: 'TRES', 4: 'QUATRO', 5: 'CINCO', 6: 'SEIS', 7: 'SETE',
				  8: 'OITO', 9: 'NOVE', 10: 'DEZ', 11: 'ONZE', 12: 'DOZE', 13: 'TREZE',
				  14: 'CATORZE', 15: 'QUINZE', 16: 'DEZESSEIS', 17: 'DEZESSETE',
				  18: 'DEZOITO', 19: 'DEZENOVE', 20: 'VINTE', 30: 'TRINTA', 40: 'QUARENTA',
				  50: 'CINQUENTA', 60: 'SESSENTA', 70: 'SETENTA', 80: 'OITENTA', 90: 'NOVENTA',
				  100: 'CENTO', 200: 'DUZENTOS', 300: 'TREZENTOS', 400: 'QUATROCENTOS', 500: 'QUINHENTOS',
				  600: 'SEISCENTOS', 700: 'SETECENTOS', 800: 'OITOCENTOS', 900: 'NOVECENTOS'}

		self.powerNameList = ['MIL', 'MILHOES', 'BILHOES']


	def convertNumberToWords(self, number):

		# Check if there is decimal in the number. If Yes process them as paisa part.
		formString = str(number)
		if formString.find('.') != -1:
			withoutDecimal, decimalPart = formString.split('.')

			paisaPart =  str(round(float(formString), 2)).split('.')[1]
			inPaisa = self._formulateDoubleDigitWords(paisaPart)

			formString, formNumber = str(withoutDecimal), int(withoutDecimal)
		else:
			# Process the number part without decimal separately
			formNumber = int(number)
			inPaisa = None

		if not formNumber:
			return 'ZERO'

		self._validateNumber(formString, formNumber)

		inRupees = self._convertNumberToWords(formString)

		if inPaisa:
			return 'Rs. %s and %s paisa' % (inRupees.title(), inPaisa.title())
		else:
			import re
			output = re.sub(r" E$", "", inRupees.title().upper())
			return '%s' % output


	def _validateNumber(self, formString, formNumber):

		assert formString.isdigit()

		# Developed to provide words upto 999999999
		if formNumber > 999999 or formNumber < 0:
			raise AssertionError('Out Of range')


	def _convertNumberToWords(self, formString):

		MSBs, hundredthPlace, teens = self._getGroupOfNumbers(formString)

		wordsList = self._convertGroupsToWords(MSBs, hundredthPlace, teens)

		return ' '.join(wordsList)


	def _getGroupOfNumbers(self, formString):

		hundredthPlace, teens = formString[-3:-2], formString[-2:]

		msbUnformattedList = list(formString[:-3])

		#---------------------------------------------------------------------#

		MSBs = []
		tempstr = ''
		for num in msbUnformattedList[::-1]:
			tempstr = '%s%s' % (num, tempstr)
			if len(tempstr) == 3:
				MSBs.insert(0, tempstr)
				tempstr = ''
			if tempstr:
				MSBs.insert(0, tempstr)

		#---------------------------------------------------------------------#

		return MSBs, hundredthPlace, teens


	def _convertGroupsToWords(self, MSBs, hundredthPlace, teens):

		wordList = []

		#---------------------------------------------------------------------#
		if teens:
			teens = int(teens)
			tensUnitsInWords = self._formulateDoubleDigitWords(teens)
			if tensUnitsInWords:
				wordList.insert(0, tensUnitsInWords)

		#---------------------------------------------------------------------#
		if hundredthPlace:
			hundredthPlace = int(hundredthPlace)*100
			if not hundredthPlace:
				# Might be zero. Ignore.
				pass
			else:
				if(hundredthPlace == 100 and (not teens)):
					hundredsInWords = 'CEM'
					wordList.insert(0, hundredsInWords)
				else:
					hundredsInWords = '%s E' % self.wordsDict[hundredthPlace]
					wordList.insert(0, hundredsInWords)

		#---------------------------------------------------------------------#
		if MSBs:
			MSBs.reverse()

			for idx, item in enumerate(MSBs):
				inWords = self.convertNumberToWords(item)
				#inWords = self._formulateDoubleDigitWords(item)
				if inWords:
					inWordsWithDenomination = '%s %s E' % (inWords, self.powerNameList[idx])
					wordList.insert(0, inWordsWithDenomination)

		return wordList


	def _formulateDoubleDigitWords(self, doubleDigit):

		if not int(doubleDigit):
			# Might be zero. Ignore.
			return None
		elif self.wordsDict.has_key(int(doubleDigit)):
			# Global dict has the key for this number
			tensInWords = self.wordsDict[int(doubleDigit)]
			return tensInWords
		else:
			doubleDigitStr = str(doubleDigit)
			tens, units = int(doubleDigitStr[0])*10, int(doubleDigitStr[1])
			tensUnitsInWords = '%s E %s' % (self.wordsDict[tens], self.wordsDict[units])
			return tensUnitsInWords


#wGenerator = Number2Words()
#for i in range(0,1000050):
#	print wGenerator.convertNumberToWords(i)
