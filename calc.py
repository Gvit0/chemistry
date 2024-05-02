import handler
import mend_table as MT


def TextToFormul(text):
		pass
def FindMolMass(formul):
		molMassT = 0
		for obj in formul:
			Fobj = ""
			FobjIndex = ""
			for sumbol in obj:
				if sumbol in MT.upReg or sumbol in MT.downReg:
					Fobj += sumbol
				elif sumbol in MT.num:
					FobjIndex += sumbol
			if FobjIndex == "":
				FobjIndex = "1"
			MTobj = MT.get_use_name(Fobj)
			molMassT +=float(MTobj["atom_mass"]) * int(FobjIndex)
		molMass = str(molMassT)
		return molMass
		
def PercentageByMass(formul,objF):
	objP = ""
	Fobj = ""
	for obj in formul:
		objP = ""
		for objT in obj:
			if objT not in MT.num:
				objP+= objT
		if objP == objF:
			objP = obj
		else:
			objP =""
	if objP =="":
		return 0
			break
	percentage =(float(FindMolMass([objP]))/ float(FindMolMass(formul)))*100
	return percentage
