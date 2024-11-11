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
            #print("!!!!!!!!!!" + str(formul)+str(tempMass)+tempForm)
    tempMass.append(tempForm)
    formul.append(tempMass)
    for obje in formul:
        
        for obj in obje:
            #print(f"{formul}         {obje}       {obj}")
            if obj == "" or obj == " ":
                obje.remove(obj)
    return formul

def objToText(obj_):
    if obj_ == "":
        return "Не найдено"
    else:
        return f"Формула: {obj_["formul"]}  Название: {obj_["name"]}  Описание: {obj_["description"]}  Атомная масса: {obj_["atom_mass"]}  Атомный номер: {obj_["id"]}"
        
def organickDetect(formul):
    has_C = 'C' in formul  # Проверяем, есть ли 'C' в формуле
    has_H = 'H' in formul  # Проверяем, есть ли 'H' в формуле
    
    # Проверяем наличие углерода и водорода
    return has_C and has_H  # Возвращаем True, если есть углерод и водород

def get_compound_type(formula):
    """
    Determines the type of a chemical compound based on its formula.

    Parameters:
    formula (list): A list of subformulas, as returned by handler.FormulToMass().

    Returns:
    str: A string indicating the type of the compound (either 'oxide', 'hydroxide', 'acid', 'salt', or an error message for organic compounds).
    """
    if organickDetect(formula):
        return 'Органические формулы не поддерживаются'

    # Получаем атомные массы всех элементов в формуле
    atomic_masses = {element['formul']: element['atom_mass'] for element in MT.table_mend}

    # Вычисляем массу формулы
    total_mass = sum([MT.get_use_atom_mass(mass) or 0 for subformula in formula for mass in subformula])

    # Проверка, является ли формула оксидом
    if len(formula) == 2 and formula[0][-1] == 'O' and formula[1].startswith('H'):
        return 'oxide'

    # Проверка, является ли формула гидроксидом
    if len(formula) == 2 and formula[0] == 'H' and formula[1] == 'O':
        return 'hydroxide'

    # Проверка, является ли формула кислотой
    if len(formula) == 2 and formula[0] == 'H' and MT.get_use_name(formula[1]) == 'Неметалл':
        return 'acid'

    # Если ни одно из условий не выполнено, определяем формулу как соль
    return 'salt'

# Примеры использования
# print(get_compound_type(['H2O']))  # Например для воды
# print(get_compound_type(['NaCl']))  # Например для поваренной соли

def infoFormul(formul):
    out ={}

    return out