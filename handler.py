import mend_table as MT

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def toint(s):
    try:
        if float(s).is_integer():
            return int(float(s))
        else:
            return s
    except ValueError:
        return s

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

def objToText(obj_):
    if obj_ == "":
        return "Не найдено"
    else:
        return f"Формула: {obj_["formul"]}  Название: {obj_["name"]}  Описание: {obj_["description"]}  Атомная масса: {obj_["atom_mass"]}  Атомный номер: {obj_["id"]}"
        
def organickDetect(formul):
    f=""
    for obj in formul:
        if "C" in obj:
            f+="C"
        if "H" in obj:
            f+="H"
    if f=="CH" or f=="HC":
        return True
    else:
        return False




def get_compound_type(formula):
    """
    Determines the type of a chemical compound based on its formula.

    Parameters:
    formula (list): A list of subformulas, as returned by handler.FormulToMass().

    Returns:
    str: A string indicating the type of the compound (either 'oxide', 'hydroxide', 'acid', or 'salt').
    """
    if organickDetect():
        return 'Органические формулы не подерживаются'
    else:
        # Get the atomic masses of all elements in the formula
        atomic_masses = {element['formul']: element['atom_mass'] for element in MT.table_mend}

        # Calculate the total mass of the formula
        total_mass = sum([MT.get_use_atom_mass(mass) for subformula in formula for mass in subformula])

        # Check if the formula is an oxide
        if len(formula) == 2 and formula[0][-1] == formula[1][-1] == 'O' and total_mass == MT.get_use_atom_mass(formula[0][:-1]) * 2 + MT.get_use_atom_mass('O'):
            return 'oxide'

        # Check if the formula is a hydroxide
        if len(formula) == 2 and formula[0] == ['O', 'H'] and MT.get_use_name(formula[1][0]) == 'Металл' and total_mass == MT.get_use_atom_mass('H') + MT.get_use_atom_mass(formula[1][0]):
            return 'hydroxide'

        # Check if the formula is an acid
        if len(formula) == 2 and formula[0] == ['H'] and MT.get_use_name(formula[1][0]) == 'Неметалл' and total_mass == MT.get_use_atom_mass('H') + MT.get_use_atom_mass(formula[1][0]):
            return 'acid'

        # If none of the above conditions are met, the formula is a salt
        return 'salt'

def infoFormul(formul):
    out ={}

    return out