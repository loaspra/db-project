import csv
import random
import string
from datetime import datetime, timedelta

import numpy as np

#tablas = ['persona', 'cliente', 
# 'ingrediente', 'pizza', 'localdePizza', 
# 'usuario', 'rol', 'trabajador', 'pedido', 
# 'PizzaIngrediente', 'bebida', 'Cl_Usuario', 
# 'Usu_Rol', 'Turno', 'Boleta', 'Pedido_Bebida', 'Pedido_Pizza']

cant_datos = 1000
pbebida = round(cant_datos/63)
p_pizza =round(cant_datos/40) # hay 40 pizzas
n_per = cant_datos*2
n_turno = 20
mul = 2  # ratio de pedidos
#cadena de letras
leter = string.ascii_letters
# agregando numeros a las letras
letras = leter.join(str(random.randint(1,100)) for i in range(0,50))
inicio_fech = datetime.fromisoformat('2011-11-14 00:12:12')


#Persona
referen = []
with open('csv_files/persona1M.csv', 'w', newline='') as csvfile:
    print("Generating data for Persona")
    esc = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    dni_init = 200000000
    cel_init = 900000001
    for i in range(0,n_per):
        linea = ["('DNI',"]
        linea.append(str(dni_init) + ",")
        linea.append(str(cel_init) + ")")
        esc.writerow(linea)
        referen.append(linea)
        dni_init += 1
        cel_init += 1
csvfile.close()


#cliente
print("Cliente")
n_clientes = 0
with open('csv_files/cliente1M.csv', 'w', newline='') as csvfile:
    esc = csv.writer(csvfile, delimiter=',', quotechar = " ", quoting=csv.QUOTE_MINIMAL)
    for i in range(0,int(n_per/2)):
        linea = ["('DNI'"]
        linea.append(referen[i][1][0:-1])
        linea.append("'calle:" + chr(random.randrange(100,115))*20 + "')")
        n_clientes += 1
        esc.writerow(linea)
csvfile.close()

distritos = ['Ancón','Ate','Barranco','Breña','Carabayllo','Chaclacayo','Chorrillos','Cieneguilla','Comas','El Agustino ','Independencia ','Jesús María ','La Molina','La Victoria ','Lima ','Lince','Los Olivos','Lurigancho','Lurín','Magdalena del Mar ','Miraflores ','Pachacamac','Pucusana','Pueblo Libre','Puente Piedra','Punta Hermosa','Punta Negra','Rímac','San Bartolo','San Borja','San Isidro','San Juan de Lurigancho','San Juan de Miraflores','San Luis','San Martín de Porres','San Miguel','Santa Anita','Santa María del Mar District','Santa Rosa','Santiago de Surco','Surquillo','Villa El Salvador','Villa María del Triunfo']

#TRABAJADOR
print("Trabajador")
with open('csv_files/trabajador1M.csv', 'w', newline='') as csvfile:
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    for i in referen:
        cisa = ''.join(random.choice(leter) for i in range(random.randrange(10,20)))
        linea = ["('DNI',"]
        linea.append(i[1])
        linea.append("'" + str(random.sample(distritos, 1)[0]) + "',")
        linea.append(random.randrange(00000000,999999999))
        linea.append(",'puesto: " + "aun_no_existe" + "',")
        linea.append(("' Direccion: " + cisa + "',").replace(" ",""))
        linea.append(str(random.randrange(900000000,999999999)) + ",")
        linea.append("'" +  cisa + "')")
        esc.writerow(linea)
csvfile.close()

referen = []

#Ingrediente
print("Ingrediente")
with open('csv_files/ingrediente1M.csv', 'w', newline='') as csvfile:
    esc = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,50):
        linea = []
        linea.append("('" + "".join(random.choice(leter) for i in range(random.randrange(5,10))) + "',")
        linea.append(str(random.randrange(10,10000)) + ")")
        esc.writerow(linea)
csvfile.close()

tamaños = ['personal', 'mediana', 'grande', 'familiar']

#Pizza
print("Pizza")
with open('csv_files/pizza1M.csv', 'w', newline='') as csvfile:
    esc = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,20):
        name = "".join(random.choice(leter) for i in range(random.randrange(5,10)))
        precio_b = round(random.random()*10, 2)
        linea = ["("]
        linea.append("'" + name + "'" + ",")
        linea.append("'" + str(tamaños[0]) + "'" + ",")
        linea.append(str(precio_b))
        linea.append(")")
        esc.writerow(linea)
        
        linea = ["("]
        linea.append("'" + name + "'" + ",")
        linea.append("'" + str(tamaños[1]) + "'" +",")
        linea.append(str(precio_b + 10))
        linea.append(")")
        esc.writerow(linea)
        
        linea = ["("]
        linea.append("'" + name + "'" + ",")
        linea.append("'" + str(tamaños[2]) + "'" + ",")
        linea.append(str(precio_b + 20))
        linea.append(")")
        esc.writerow(linea)

        linea = ["("]
        linea.append("'" + name + "'" + ",")
        linea.append("'" + str(tamaños[3]) + "'" + ",")
        linea.append(str(precio_b + 50))
        linea.append(")")
        esc.writerow(linea)
csvfile.close()


permisos = ["create db", "cannot login", "create rol", "replication", "bypassRLS"]

#Usuarios
print("Usuarios")
with open('csv_files/users1M.csv', 'w', newline='') as csvfile:
    with open("csv_files/trabajador1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ' ', quotechar = ' ', quoting=csv.QUOTE_MINIMAL)
        usuarios_t = []
        for row in parent:
            usuario = row[-1][:-1]
            usuarios_t.append(usuario)  #Lp_direeccion, lp_telefono
    aux.close()
    
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    for i in usuarios_t:
        linea = ["("]
        linea.append(i + ",")
        linea.append("'" + "".join(random.choice(letras) for i in range(random.randrange(8,17))) +"')")
        esc.writerow(linea)
    clientes_users = []

    for i in range(0,n_clientes-2):
        linea = ["("]
        randd = "'" + ''.join(random.choice(letras) for i in range(random.randrange(12,20)))
        clientes_users.append(randd)
        linea.append(randd +"',")
        linea.append("'" + ''.join(random.choice(letras) for i in range(random.randrange(10,17))) + "')")
        esc.writerow(linea)
    
csvfile.close()


# Local de Pizza
print("Local de Pizza")
with open('csv_files/local_de_pizza1M.csv', 'w', newline='') as csvfile:
    with open("csv_files/trabajador1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen = []
        for row in parent:
            referen.append(row[5:7])  #Lp_direeccion, lp_telefono
    aux.close()

    it = 0
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    for i in referen:
        linea = ["("]
        linea.append(str(i[0]).replace(" ", "") + ",")
        linea.append(str(i[1]).replace(" ", "") + ",")
        linea.append(str(random.randrange(10,100)) + ",")
        linea.append(str(round(random.random()*10, 2)) + ")")
        if (it > 17):
            break
        esc.writerow(linea)
csvfile.close()

#Pedido
print("Pedido")
with open('csv_files/Pedido1M.csv', 'w', newline='') as csvfile:
    permisos = ["create db", "cannot login", "create rol", "replication", "bypassRLS"]
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    with open("csv_files/cliente1M.csv", 'r', newline='') as ref:
        parent = csv.reader(ref, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen_cl = []
        for row in parent:
            referen_cl.append(row[0:2])  #Lp_direeccion, lp_telefono
    ref.close()

    if (len(referen_cl) > len(referen)):
        iterar = referen
    else:
        iterar = referen_cl
    ola = timedelta(seconds = 1)
    
    aa = round(len(iterar)/2)
    fecha = inicio_fech
    for i in range (0, aa):
        for k in range(0,mul):
            lista = ["("]
            fecha  += ola 
            hora = fecha.time()
            lista.append("'" + str(fecha) + "',")
            lista.append("'" + str(hora) + "',")
            lista.append("'" + random.sample(["active", "completed", "delayed", "canceled"], 1)[0] + "',")
            lista.append("'" + random.sample(["tienda", "delivery"], 1)[0] + "',")
            lista.append(str(referen[i][0]).replace(" ", "") + ",")
            lista.append(str(referen[i][1]).replace(" ", "") + ",")
            lista.append(str(referen_cl[i][0][1:]).replace(" ", "") + ",")
            lista.append(str(referen_cl[i][1]).replace(" ", "") + ",")
            lista.append(str(round(random.random()*115, 2)) + ")")
            esc.writerow(lista)
        print(str(round((i/aa)*100)) + "%")
csvfile.close()


#PizzaIngrediente
print("Pizza-Ingrediente")
with open('csv_files/pizzaingrediente1M.csv', 'w', newline='') as csvfile:
    with open("csv_files/pizza1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen = []
        for row in parent:
            referen.append(row[0:2])  #Lp_direeccion, lp_telefono
    aux.close()

    with open("csv_files/ingrediente1M.csv", 'r', newline='') as ref:
        parent_ing = csv.reader(ref, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen_cl = []
        for row in parent_ing:
            referen_cl.append(row[1])
    ref.close()

    if (len(referen_cl) > len(referen)):
        iterar = referen
    else:
        iterar = referen_cl
    
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(iterar)):
        linea = [""]
        linea.append(str(referen[i][0]).replace(" ", "") + ",")
        linea.append(str(referen[i][1]).replace(" ", "") + ",")
        linea.append(str(referen_cl[i]).replace(" ", "") + ",")
        esc.writerow(linea)
csvfile.close()


#Bebida
print("Bebidas")
#bebidas = ['7 Up','A&W Root Beer','Barq\'s Root Beer','Canada Dry Ginger Ale','Cherry Coca-Cola','Coca-Cola Classic','Coca-Cola Zero','Diet Coca-Cola','Diet Dr. Pepper','Diet Pepsi','Dr. Pepper','Fanta Orange','Fresca','Mountain Dew','Mountain Dew Code Red','Mug Root Beer','Orange Crush','Pepsi','Sierra Mist','Sprite','Vanilla Coca-Cola','Wild Cherry Pepsi']
with open('csv_files/bebida1M.csv', 'w', newline='') as csvfile:
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    bebidas = range(100,115)
    for i in bebidas: #67 bebidas
        base = round(random.random()*5, 2)
        linea = []
        linea.append("('" + chr(i)*4 + "','personal'," + str(base) + ")")
        esc.writerow(linea)
        linea = []
        linea.append("('" + chr(i)*4 + "','mediana'," + str(base*2) + ")")
        esc.writerow(linea)
        linea = []
        linea.append("('" + chr(i)*4 + "','grande'," + str(base*10) + ")")
        esc.writerow(linea)
csvfile.close()


# Cliente-usuario
print("Cliente-usuario")
with open('csv_files/cl_usuario1M.csv', 'w', newline='') as csvfile:
    with open("csv_files/cliente1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen = []
        for row in parent:
            referen.append(row[0:2])  #tipodoc, numdoc
    aux.close()

    it = 0
    esc = csv.writer(csvfile, delimiter=",",quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    cont = 0
    for i in clientes_users:
        linea = []
        linea.append(str(referen[cont][0]).replace(" ", ""))
        linea.append(str(referen[cont][1]).replace(" ", ""))
        linea.append(i.strip() + "')")
        esc.writerow(linea)
        cont += 1
csvfile.close()

#Rol
print("Rol")
roles = ['administrador', 'gerente', 'asistente', 'ayudante', 'laburador', 'españa', 'cliente']
with open('csv_files/rol1M.csv', 'w', newline='') as csvfile:
    permisos = ["create db", "cannot login", "create rol", "replication", "bypassRLS"]
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    for i in roles:
        lista = ["("]
        lista.append("'" + i + "',")
        lista.append("'" + str(random.sample(permisos, 1)[0]) + "')")
        esc.writerow(lista)
csvfile.close()

# usuario rol
print("usuario-rol")
with open("csv_files/usu_rol1M.csv",'w',  newline='') as csvfile:
    with open("csv_files/users1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen = []
        for row in parent:
            referen.append(row[0][2:])  #Lp_direeccion, lp_telefono
    aux.close()
    with open("csv_files/rol1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen_r = []
        for row in parent:
            referen_r.append(row[0][2:])  #Lp_direeccion, lp_telefono
    aux.close()
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    
    for i in referen:
        linea = ["("]
        lain = i.strip() + "," + random.sample(referen_r,1)[0] + ")"
        if (lain[0] != "'"):
            lain = "'" + lain
        linea.append(lain)
        esc.writerow(linea)

#Turno
print("Turno")
fecha = inicio_fech
with open('csv_files/turno1M.csv', 'w', newline='') as csvfile:
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
    aydi = 1
    for i in range(0,n_turno):
        lista = ["("]
        lista.append(str(aydi) + ",")
        fecha += ola
        hora = fecha.time()
        lista.append("'" + str(hora) + "',")
        hora = "'" + str(random.randrange(0,23)) + ":" + str(random.randrange(0,59)) + ":" + str(random.randrange(0, 59)) + "'"
        lista.append(hora + ")")
        esc.writerow(lista)
        aydi += 1
csvfile.close()

#BOleta
print("Boleta")
with open("csv_files/boleta1M.csv",'w', newline='') as csvfile: 
    with open("csv_files/trabajador1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen = []
        for row in parent:
            referen.append(row[0:2])  #tipo, num de doc
    aux.close()
    fecha = inicio_fech
    esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)    
    for i in referen:
        for l in range(0,2):
            fecha  += ola
            lista = ["("]
            lista.append(str(fecha) + ",")
            lista.append(str(round(random.random()*100, 2)) + ",")
            lista.append(i[0][1:] + ",")
            lista.append(i[1] + ",")
            lista.append(str(random.randrange(2,n_turno)) + ")")
            esc.writerow(lista)


#pedido bebida
print("Pedido-bebida")
with open("csv_files/pedido_bebida1M.csv",'w', newline = "") as csvfile: 
    with open("csv_files/bebida1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen = []
        for row in parent:
            referen.append(row[0:2])  #nombre, tamaño (bebida)
    aux.close()
    fecha = inicio_fech
    esc = csv.writer(csvfile,quotechar = " " , delimiter = " ", quoting=csv.QUOTE_MINIMAL)    
    for i in referen:
        for k in range(0,pbebida):
            fecha  += ola
            lista = ["('"]
            lista.append(str(fecha) + "',")
            lista.append("'" + i[0].strip()[2:] + ",")
            lista.append(i[1].strip() + ",")
            lista.append(str(random.randrange(1,10)) + ")")
            esc.writerow(lista)

#pedido pizza
print("Pedido-pizza")
with open("csv_files/pedido_pizza1M.csv",'w', newline = "") as csvfile: 
    with open("csv_files/pizza1M.csv", newline='') as aux:
        parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        referen = []
        for row in parent:
            referen.append(row[0:2])  #nombre, tamaño (pizza)
    aux.close()

    esc = csv.writer(csvfile,quotechar = " " , delimiter = " ", quoting=csv.QUOTE_MINIMAL)    
    mat = len(referen)
    ka = 0
    fecha = inicio_fech
    for i in referen:
        for k in range(0,p_pizza):
            fecha  += ola
            lista = []
            lista.append("('" + str(fecha) + "',")
            lista.append(i[0].strip()[1:] + ",")
            lista.append(i[1].strip() + ",")
            lista.append(str(random.randrange(1,10)) + ")")
            esc.writerow(lista)
        ka += 1
        print(str(ka/mat*100) + "%")
print("Done!")