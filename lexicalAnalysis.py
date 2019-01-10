keywords = { "abstract", "boolean", "byte", "case",
            "catch", "char", "class", "continue", "default", "do", "double",
            "else", "extends", "final", "finally", "float", "for", "if",
            "implements", "import", "instanceof", "int", "interface", "long",
            "native", "new", "package", "private", "protected", "public",
            "return", "short", "static", "super", "switch", "synchronized",
            "this", "throw", "throws", "transient", "try", "void", "volatile",
            "while", "false", "true", "null" }

operators = {"+" ,"<=","!",">=","-","%","/","<",">","==","&","&&","|","||","*","^","!=","="}

specialChars = {"(",")","[","]","{","}",",",";","\\","'","/","_"}



#For storing the corresponding elements
keywordsNum= []
identifiers = []
specialCharsSum =[]
operatorsSum = []
libraries = []
presentInPrint = []
presentInScan = []
numeric = []
numComments = 0
errors=[]



#Function of remove all leading tabs and spaces. Also ignore(delete) the comments
def removeComments(fileContent):
	for i in range(len(fileContent)):
		global numComments
		temp=fileContent[i]
		temp = temp.strip()
		fileContent[i]=temp
		if(fileContent[i] != ''):
			if( (fileContent[i])[0] == '/' and (fileContent[i])[1] == '/' ):
				fileContent[i] = ""
				numComments += 1
			elif(fileContent[i].find('/*') != -1):
				j =i
				numComments += 1
				while(fileContent[j].find("*/") == -1):
					fileContent[j]=""
					j += 1
				fileContent[j]=""
	return list(filter(None,fileContent))

#Funtion to handle print statement
def handlePrintStatements(printStatement):
	identifiers.append("printf")
	specialCharsSum.append("(")
	specialCharsSum.append(")")
	specialCharsSum.append(";")
	printString = printStatement[ printStatement.index('(')+1 : printStatement.index(')') ]
	if(printString[0] == "\""):
		printString = printString[1:]
	presentInPrint.append(printString[0:printString.index("\"")])
	printString = printString[printString.index("\"")+1:]
	printString = printString.split(',')
	for j in range(len(printString)):
		if(printString[j] != ''):
			presentInPrint.append(printString[j].strip())

#function to handle scanf statmenet
def handleScanfStatements(scanStatement):
	identifiers.append("scanf")
	specialCharsSum.append("(")
	specialCharsSum.append(")")
	specialCharsSum.append(";")
	scanfString = ( scanStatement[ scanStatement.index('(') + 1 : scanStatement.index(')') ] )
	if(scanfString[0] == "\""):
		scanfString = scanfString[1:]
	presentInScan.append(scanfString[0:scanfString.index("\"")])
	scanfString = scanfString[scanfString.index("\"")+1:]
	scanfString = scanfString.split(',')
	for j in range(len(scanfString)):
		if(scanfString[j] != ''):
			presentInScan.append(scanfString[j].strip())

#For printing the output
def printOutput():
	print("\nPrint statement contents- ")
	for i in range(len(presentInPrint)):
		if(presentInPrint[i] != '\n'):
			print(presentInPrint[i])

	print("\nScanf statement contents- ")
	for i in range(len(presentInScan)):
		if(presentInScan[i] != '\n'):
			print(presentInScan[i]," ")

	print("\nKeywords- ")
	for i in range(len(keywordsNum)):
		print(keywordsNum[i], end=" ")
	print("\n")

	print("Identifiers- ")
	for i in range(len(identifiers)):
		print(identifiers[i], end=" ")
	print("\n")

	print("Special Characters- ")
	for i in range(len(specialCharsSum)):
		print(specialCharsSum[i], end=" ")
	print("\n")

	print("Operators- ")
	for i in range(len(operatorsSum)):
		print(operatorsSum[i], end=" ")
	print("\n")

	print("Numeric- ")
	for i in range(len(numeric)):
		print(numeric[i], end=" ")
	print("\n")

	print("Libraries- ")
	for i in range(len(libraries)):
		print(libraries[i], end=" ")
	print("\n")

	print("Errors-")
	for i in range(len(errors)):
		print(errors[i], end=" ")
	print("\n")

	print("And ignored ",numComments," comments.")
	print("\n")


if __name__ == "__main__":
	File = open('SampleC.c')
	fileContent = File.readlines()
	fileContent = removeComments(fileContent)

	for i in range(len(fileContent)):

		if( (fileContent[i])[0:6] == 'printf' ):
			handlePrintStatements(fileContent[i])

		elif ( (fileContent[i])[0:5] == 'scanf' ):
			handleScanfStatements(fileContent[i])

		else:
			currentLine = fileContent[i].split(' ')
			if((currentLine[0])[0]=='#'):
				libraries.append((fileContent[i])[fileContent[i].index('<')+1:fileContent[i].index('>')])
				specialCharsSum.append("<")
				specialCharsSum.append(">")
				keywordsNum.append('include')
			else:
				for j in range(len(currentLine)):
					if currentLine[j] in keywords:
						keywordsNum.append(currentLine[j])
						continue
					elif currentLine[j] in operators:
						operatorsSum.append(currentLine[j])
						continue
					elif currentLine[j] in specialChars:
						specialCharsSum.append(currentLine[j])
						continue
					elif currentLine[j].isnumeric():
						numeric.append(currentLine[j])
						continue
					elif currentLine[j]!= '':
						if( len(currentLine[j])>1 and  ( (currentLine[j])[0].isnumeric() or ( (currentLine[j])[0] != "_" and ((currentLine[j][0]) in specialChars) ) )):
							errors.append(currentLine[j])
						else:
							identifiers.append(currentLine[j])

	printOutput()
		