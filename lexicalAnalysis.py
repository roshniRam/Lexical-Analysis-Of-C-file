File = open('SampleC.c')

keywordsNum= []
identifiers = []
specialCharsSum =[]
operatorsSum = []
libraries = 0
stringSum = 0
numComments = 0

keywords = { "abstract", "boolean", "byte", "case",
            "catch", "char", "class", "continue", "default", "do", "double",
            "else", "extends", "final", "finally", "float", "for", "if",
            "implements", "import", "instanceof", "int", "interface", "long",
            "native", "new", "package", "private", "protected", "public",
            "return", "short", "static", "super", "switch", "synchronized",
            "this", "throw", "throws", "transient", "try", "void", "volatile",
            "while", "false", "true", "null" };
operators = {"+" ,"<=","!",">=","-","%","/","<",">","==","&","&&","|","||","*","^","!="}

specialChars = {"(",")","[","]","{","}",",",";","\\","'","/","_"}

fileContent = File.readlines()


for i in range(len(fileContent)):
	temp=fileContent[i]
	temp = temp.strip()
	
	#if( temp[0] == "/" and temp[1] == "/"):
	#	del fileContent[i]
	#else:
	fileContent[i]=temp
	if( (fileContent[i])[0] == '/' and (fileContent[i])[1] == '/' ):
		fileContent[i] = ""
		numComments += 1
	
fileContent = list(filter(None,fileContent))

for i in range(len(fileContent)):
	#print(fileContent[i]," ",len(fileContent[i]),"\n")
	
	if((fileContent[i])[0:6] == 'printf'):
		identifiers.append("printf")
		specialCharsSum.append("(")
		specialCharsSum.append(")")
		specialCharsSum.append(";")
		stringSum += 1
	elif((fileContent[i])[0:5] == 'scanf'):
		identifiers.append("scanf")
		specialCharsSum.append("(")
		specialCharsSum.append(")")
		specialCharsSum.append(";")
		stringSum += 1
	else:
		currentLine = fileContent[i].split(' ')
		#print(currentLine," ",len(currentLine),"\n")
		if((currentLine[0])[0]=='#'):
			libraries +=1
			specialCharsSum.append("(")
			specialCharsSum.append(")")
			keywordsNum.append('#')
		else:
			for j in range(len(currentLine)):
				if currentLine[j] in keywords:
					keywordsNum.append(currentLine[j])
				elif currentLine[j] in operators:
					operatorsSum.append(currentLine[j])
				elif currentLine[j] in specialChars:
					specialCharsSum.append(currentLine[j])
				else:
					identifiers.append(currentLine[j])
			

print("keywords: ",keywordsNum,"\nIdentifiers: ",identifiers,"\nSpecial Characters: ",specialCharsSum,"\nOperators: ",
	operatorsSum,"\nLibraries: ",libraries, "\nDeleted ",numComments," comments")