import mend_table as MT
import handler 
import calc

def FindMolMass(text):
    return calc.FindMolMass(handler.FormulToMass(text)[0])

def PercentageByMass(text,obj):
    return calc.PercentageByMass(handler.FormulToMass(text)[0],obj)
  