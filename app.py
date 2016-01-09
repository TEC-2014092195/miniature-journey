import csv
import json
from collections import Counter
accidentes = []
def menu_principal(): #program does nothing as written
	print("-------------------Menú-------------------")
	print("[1] Carga de Datos")
	print("[2] Estadística de Accidentes por lugares")
	print("[3] Estadística de Accidentes por causas")
	print("[S] Salir")
	return input("Ingrese la opción que desea: ")
##Opciones--------------
def caso_1():
	filename = input("Ingrese el nombre del archivo: ")
	try:
		global accidentes
		##accidentes = []
		with open(filename, newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=';')
			for row in spamreader:
				accidentes.append(row)
		print("«{El archivo se cargó exitosamente}»")
		return accidentes
	except IOError as e:
		errno, strerror = e.args
		print("I/O error({0}): {1}".format(errno, strerror))
		print("<[El archivo indicado no existe]>")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		print("<[El archivo indicado no existe]>")
		raise

def caso_2():
	global accidentes
	cnt_lugar = Counter()
	for accidente in accidentes:
		lugar = accidente[0]
		cnt_lugar[lugar] += 1
	print("---Registro accidentes por lugar---")
	for nombre in cnt_lugar:
		print("{0}: {1}".format(nombre,cnt_lugar[nombre]))
	if(len(accidentes)==0):
		print("No se han registrado accidentes (utilice opción 1 del menú principal).")

def caso_3():
	global accidentes
	cnt_causa = Counter()
	for accidente in accidentes:
		causa = accidente[2]
		cnt_causa[causa] += 1
	print("---Registro accidentes por causa---")
	for nombre in cnt_causa:
		print("{0}: {1}".format(nombre,cnt_causa[nombre]))
	if(len(accidentes)==0):
		print("No se han registrado accidentes (utilice opción 1 del menú principal).")


def caso_salir():
	print("Fin del programa")

def caso_invalido():
	print('Opción Inválida. Intente de nuevo.')
##Main
opciones = { '1': caso_1,   '2': caso_2,   '3': caso_3, 
	's': caso_salir, 'S': caso_salir }
while True:
	opcion = menu_principal()
	f = opciones.get(opcion, caso_invalido)
	f()
	if (opcion == 's' or opcion == 'S'): break ##break del programa