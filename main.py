import mend_table as MT
import handler
import calc
from time import sleep

print("Добро пожаловать в химический калькулятор!")

def PrintMenu():
	print("возможности:")
	print("1)Найти молярную массу")
	print("2)Уравнять-")
	print("3)Найти массовую долю")
	print("4)Информация о формуле")
	print("q- Выход")
	print("h- информация")
	print("")
def printInfo():
	print("Формулы ввод : ClHO2+H2O=Cl")
	print("почта для ошибок: gatvit@mail.ru")
	print("версия:")
	print("для обновления:")
	print("")
def MenuInput(InMen):
	if InMen == "q":
		exit()
	elif InMen == "h":
		printInfo()
	elif int(InMen)== 1:
		print(f"Молярная масса: {calc.FindMolMass(handler.FormulToMass(input('Формула:'))[0])}")
	elif int(InMen)==2:
		formul = handler.FormulToMass(input('Формула:'))
	
	elif int(InMen)==3:
		formul = handler.FormulToMass(input('Формула: '))[0]
		objF =input('Найти долю ')
		otvet = calc.PercentageByMass(formul,objF)
		print(f"Ответ: {otvet}%")
	elif int(InMen)==4:
		formulT=input("Формула: ")
		formul=handler.FormulToMass(formulT)[0]
		info=handler.infoFormul(formul)
		print(f"Информация о {formulT}:")
		print(f"Органический: {handler.organickDetect(formul)}")
	elif int(InMen) ==0:
		print(handler.FormulToMass(input("формула:")))
		
while True:
	PrintMenu()
	MenuInput(input("Номер меню: "))
	print("=================================")
