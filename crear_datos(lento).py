from numpy.core import arrayprint
from numpy.lib.function_base import append
from numpy.ma.core import array
import psycopg2
import numpy as np
import random

# Valores a considerar:
# INT
# FLOAT
# VARCHAR (STRING)
# TIME 	'16:44:50'
# TIMESTAMP (DATE + TIME)  '2004-10-19 10:23:54'


n = 100000
tabla = "boleta"

# genera cadenas random de Strings (devuelve lista)
def generar_strings():
	estr = ""
	for i in range(0, 5):
		rand = random.randrange(97, 122)
		estr = estr + chr(rand)
	return estr

# genera numereos random (devuelve lista)
def generar_entero():
	return random.randrange(2500001,8041000)

# genera fechas (timepo + fecha)
def generar_fechas():
	#formato 
	#'2004-10-19 10:23:54'
	stri = str(random.randrange(1900, 2100)) + "-" + str(random.randrange(1,12)) + "-" + str(random.randrange(1,25)) + " " + str(random.randrange(0,23)) + ":" + str(random.randrange(0,59)) + ":" + str(random.randrange(0, 59))
	return stri

# genera tiempos:
def generar_tiempos():
	#formato 
	#'10:23:54'
	stri = str(random.randrange(0,23)) + ":" + str(random.randrange(0,59)) + ":" + str(random.randrange(0, 59))
	return stri


# ver que dato es
def crear_data(att, n):
	lecs = []
	for i in att:
		if i.find("char") != -1:
			# es un varchar o char (por simplicidad diré que es un varchar)
			lecs.append(generar_strings)
		elif i.find("int") != -1:
			# es un entero (hay que implementar una funcion que distinga entre DNIs y numeros mas pequeños)
			lecs.append(generar_entero)
		elif i.find("time") != -1:
			# es un tiempo
			lecs.append(generar_tiempos)
		else:
			# es una fecha
			lecs.append(generar_fechas)
	# acabo de indentificar

	# preparar query
	print("!!!!!!!!!!!!!!!")
	qer = "INSERT INTO " + tabla + " VALUES ("
	V = ""
	for i in range(0, n):
		for e in lecs:
			V = V + "," + "'" + str(e()) + "'"
		V = V + ")"
	qer = qer + V
	print(qer)




conect = psycopg2.connect("dbname=serv user=loaspra")
cur = conect.cursor()

cur.execute("SELECT oid, typname FROM pg_catalog.pg_type")
type_mappings = {
    int(oid): typname
    for oid, typname in cur.fetchall()}

cur.execute("SELECT * FROM " + tabla)
val = np.asmatrix(cur.description)
val = val[:,1]
enviar = []
for i in val:
	enviar.append(type_mappings[np.asscalar(i)])
crear_data(enviar, n)

conect.commit()

cur.close()
conect.close()