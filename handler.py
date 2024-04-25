import mend_table as MT
def FormulToMass(formulIn):
	formul= []
	status = "nil"
	formulNumb = 1
	tempMass =[]
	tempForm = ""

	newF = True
	for sumbol in formulIn:
		if sumbol in MT.upReg and newF:
			newF = False
			tempForm += sumbol
		elif sumbol in MT.downReg:
			tempForm += sumbol
		elif sumbol in MT.num:
			tempForm += sumbol
		elif sumbol in MT.upReg:
			tempMass.append(tempForm)
			tempForm = sumbol
		elif sumbol == " ":
			pass
		elif sumbol in MT.funcSumbol:
			tempMass.append(tempForm)
			formul.append(tempMass)
			formul.append([sumbol])
			tempMass = []
			tempForm = ""
		#print(str(formul)+str(tempMass)+tempForm+ str(t))
	tempMass.append(tempForm)
	formul.append(tempMass)
	for obje in formul:
		for obj in obje:
			if obj == "" or obj == " ":
				obj.remove(obj)
	return formul
