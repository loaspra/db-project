from numpy.lib.function_base import append
from numpy.ma.core import array, asarray
import psycopg2
import numpy as np
import random

# Valores a considerar:
# INT
# FLOAT
# VARCHAR (STRING)
# TIME 	'16:44:50'
# TIMESTAMP (DATE + TIME)  '2004-10-19 10:23:54'

schema_name = "public"
n = 10
table_name = "Persona"

# genera cadenas random de Strings (devuelve lista)
def generar_strings(n):
	lista = []
	for e in range(0, n):
		estr = ""
		for i in range(0, 5):
			rand = random.randrange(97, 122)
			estr = estr + chr(rand)
		lista.append("'" + estr + "'")
	return lista

# genera numereos random (devuelve lista)
def generar_entero(n):
	numero = []
	for i in range(0, n):
		numero.append(random.randrange(2500001,8041000))
	return numero

# genera un vector de numeros flotantes
def generar_floats(n):
	numero = []
	for i in range(0, n):
		numero.append(round(random.uniform(1,100), 2))
	return numero


# genera fechas (timepo + fecha)
def generar_fechas(n):
	#formato 
	#'2004-10-19 10:23:54'
	vec = []
	for i in range(0,n):
		stri = "'" + str(random.randrange(1900, 2100)) + "-" + str(random.randrange(1,12)) + "-" + str(random.randrange(1,25)) + " " + str(random.randrange(0,23)) + ":" + str(random.randrange(0,59)) + ":" + str(random.randrange(0, 59)) + "'"
		vec.append(stri)
	return vec

# genera tiempos:
def generar_tiempos(n):
	#formato 
	#'10:23:54'
	vec = []
	for i in range(0,n):
		stri = "'" + str(random.randrange(0,23)) + ":" + str(random.randrange(0,59)) + ":" + str(random.randrange(0, 59)) + "'"
		vec.append(stri)
	return vec


# ver que dato es
def crear_data(att, n):
	print(att)
	if att.find("char") != -1:
		# es un varchar o char (por simplicidad diré que es un varchar)
		return generar_strings(n)
	elif att.find("int") != -1:
		# es un entero (hay que implementar una funcion que distinga entre DNIs y numeros mas pequeños)
		return generar_entero(n)
	elif att.find("stamp") != -1:
		# es una fecha
		return generar_fechas(n)
	elif att.find("oat") != -1:
		# es un float
		return generar_floats(n)
	else:
		# es una marca temporal
		return generar_tiempos(n)

conect = psycopg2.connect("dbname=serv user=loaspra")
cur = conect.cursor()

cur.execute("SELECT oid, typname FROM pg_catalog.pg_type")
type_mappings = {
    int(oid): typname
    for oid, typname in cur.fetchall()}

cur.execute("SELECT * FROM " + table_name)
uer = []
val = cur.description
for i in val:
	tipo = type_mappings[i[1]]
	uer.append(np.asarray(crear_data(tipo, n)).T)
aa = np.asmatrix(uer)

print(len(asarray(aa[:,0])))

# preparando query:

q = "INSERT INTO " + table_name + " VALUES ("

for i in range(0,n):
	aux = ""
	for e in range(0, len(asarray(aa[:,0]))):
		aux += aa[e,i] + ","
	aux = aux[:-1]
	q += aux + "),("

q = q[:-3]
q += ")"
# print(q)
#cur.execute("SELECT * FROM " + table_name)
#print(cur.fetchone())
#cur.execute(q)

cons = "SELECT con.* FROM pg_catalog.pg_constraint con INNER JOIN pg_catalog.pg_class rel ON rel.oid = con.conrelid INNER JOIN pg_catalog.pg_namespace nsp ON nsp.oid = connamespace WHERE nsp.nspname =" + "'" + schema_name + "'" + " AND rel.relname = " + "'" + table_name + "'" + ";"
cur.execute(cons)
print("aaaa")
print(cur.fetchone())
#conect.commit()

#cur.execute("SELECT * FROM " + table_name)
#print(cur.fetchone())