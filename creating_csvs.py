import csv
import random
import string
from datetime import datetime, timedelta, time
import numpy as np
from tqdm import tqdm

def todo(file, cant_datos):
    # 500 trabajadores fijos
    # clientes hasta 1 millon
    # pedidos muiiichos

    
    #tablas = ['persona', 'cliente', 
    # 'ingrediente', 'pizza', 'localdePizza', 
    # 'usuario', 'rol', 'trabajador', 'pedido', 
    # 'PizzaIngrediente', 'bebida', 'Cl_Usuario', 
    # 'Usu_Rol', 'Turno', 'Boleta', 'Pedido_Bebida', 'Pedido_Pizza']
    diff = timedelta(hours = 1)
    pbebida = round(cant_datos/63)
    p_pizza =round(cant_datos/40) # hay 40 pizzas
    n_per = cant_datos*2
    n_workers = int(int(cant_datos/10) + 200)%cant_datos #papa johns tiene 150K, nosotros apuntamos a que se tenga 100k a lo más
    n_turno = 20
    mul = 2  # ratio de pedidos
    #cadena de letras
    numbers = string.digits
    leter = string.ascii_letters

    # agregando numeros a las letras
    letras = leter.join(str(random.randint(1,100)) for i in range(0,50))
    inicio_fech = datetime.fromisoformat('1500-01-01 00:00:00')


    #Persona
    clientes_data = []
    trabajadores_data = []
    tipos_doc = ["DNI", "PASAPORTE", "DNI", "DNI", "CARNE DE EXTRANJERIA", "DNI", "DNI", "DNI", "DNI"]
    with open('csv_files/persona' + file, 'w', newline='') as csvfile:
        print("Generating data for Persona")
        esc = csv.writer(csvfile, delimiter=' ', quotechar='\t', quoting=csv.QUOTE_MINIMAL)
        doc = 25799435
        for i in tqdm(range(0,n_per - n_workers)):
            tipo_doc = random.choice(tipos_doc)
            linea = ["('"+ tipo_doc +"',"]
            num_telf = "9" + "".join(random.choice(numbers) for i in range(0,8))
            doc += 1
            linea.append(str(doc) + ",")
            linea.append(str(num_telf) + ")")
            clientes_data.append([tipo_doc,doc])
            esc.writerow(linea)
        for i in range(0, n_workers):
            linea = ["('DNI',"]
            num_telf = "9" + "".join(random.choice(numbers) for i in range(0,8))
            doc += 1
            linea = ["('DNI',"]
            linea.append(str(doc) + ",")
            linea.append(str(num_telf) + ")")
            esc.writerow(linea)
            trabajadores_data.append(doc)
    csvfile.close()


    #cliente
    print("Cliente")
    n_clientes = 0
    with open('csv_files/cliente' + file, 'w', newline='') as csvfile:
        esc = csv.writer(csvfile, delimiter=',', quotechar = "\t", quoting=csv.QUOTE_MINIMAL)
        for i in tqdm(range(0, n_per - n_workers)):
            linea = ["('" + clientes_data[i][0] + "'"]
            linea.append(clientes_data[i][1])
            linea.append("'calle:" + chr(random.randrange(100,115))*20 + "')")
            n_clientes += 1
            esc.writerow(linea)
    csvfile.close()

    distritos = ['Ancón','Ate','Barranco','Breña','Carabayllo','Chaclacayo','Chorrillos','Cieneguilla','Comas','El Agustino ','Independencia ','Jesús María ','La Molina','La Victoria ','Lima ','Lince','Los Olivos','Lurigancho','Lurín','Magdalena del Mar ','Miraflores ','Pachacamac','Pucusana','Pueblo Libre','Puente Piedra','Punta Hermosa','Punta Negra','Rímac','San Bartolo','San Borja','San Isidro','San Juan de Lurigancho','San Juan de Miraflores','San Luis','San Martín de Porres','San Miguel','Santa Anita','Santa María del Mar District','Santa Rosa','Santiago de Surco','Surquillo','Villa El Salvador','Villa María del Triunfo']

    # Local de Pizza
    print("Local de Pizza")
    locales = []
    with open('csv_files/local_de_pizza' + file, 'w', newline='') as csvfile:

        esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
        for i in range(0,17):
            cisa = ''.join(random.choice(leter) for i in range(random.randrange(10,20)))
            linea = ["("]
            direc = ("'Direccion:" + cisa + "'")
            num_tef = str(random.randrange(900000000, 999999999))
            locales.append([direc, num_tef])
            linea.append(direc + ",")
            linea.append(num_tef + ",")
            linea.append(str(random.randrange(10,100)) + ",")
            linea.append(str(round(random.random()*10, 2)) + ")")
            esc.writerow(linea)
    csvfile.close()


    #TRABAJADOR
    print("Trabajador")
    usuarios_t = []
    with open('csv_files/trabajador' + file, 'w', newline='') as csvfile:
        esc = csv.writer(csvfile, delimiter=' ' ,quotechar = "\t",  quoting=csv.QUOTE_MINIMAL)
        with open('csv_files/local_de_pizza' + file, newline='') as csvfilse:
            leer = csv.reader(csvfilse, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
            cosas = []
            for row in leer:
                cosas.append(row)
        for i in tqdm(range(0, n_workers)):
            cisa = "".join(random.choice(leter) for i in range(random.randrange(10,15)))
            linea = ["('DNI',"]
            linea.append(trabajadores_data[i])
            linea.append(",'" + str(random.sample(distritos, 1)[0].strip()) + "',")
            linea.append(random.randrange(900000000,999999999))
            linea.append(",'puesto: " + "aun_no_existe" + "',")
            linea.append(locales[i%17][0] + ",")
            linea.append(locales[i%17][1])
            linea.append(",'" +  cisa + "')")
            usuarios_t.append(cisa)
            esc.writerow(linea)
    csvfile.close()

    referen = []

    #Ingrediente
    print("Ingrediente")
    with open('csv_files/ingrediente' + file, 'w', newline='') as csvfile:
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
    with open('csv_files/pizza' + file, 'w', newline='') as csvfile:
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
    with open('csv_files/users' + file, 'w', newline='') as csvfile:
        esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
        for i in usuarios_t:
            linea = ["("]
            linea.append("'" + i + "',")
            linea.append("'" + "".join(random.choice(letras) for i in range(random.randrange(8,17))) +"')")
            esc.writerow(linea)
        clientes_users = []

        for i in tqdm(range(0,n_clientes-2)):
            linea = ["("]
            randd = "'" + ''.join(random.choice(letras) for i in range(random.randrange(12,20)))
            clientes_users.append(randd)
            linea.append(randd +"',")
            linea.append("'" + ''.join(random.choice(letras) for i in range(random.randrange(10,17))) + "')")
            esc.writerow(linea)
        
    csvfile.close()


    #Pedido
    print("Pedido")
    with open('csv_files/Pedido' + file, 'w', newline='') as csvfile:
        permisos = ["create db", "cannot login", "create rol", "replication", "bypassRLS"]
        esc = csv.writer(csvfile, delimiter=' ',quotechar = "\t" , quoting=csv.QUOTE_MINIMAL)

        state = ["retrasado", "entrega", "en camino", "preparando", "cancelado"]
        entrega = ["delivery", "recojo"]
        fecha = inicio_fech
        for i in tqdm(range(0, cant_datos)):
            for k in range(0,mul):
                lista = ["("]
                fecha += diff
                lista.append("'" + str(fecha.date()) + "',") #              fecha
                lista.append("'" + str(fecha.time()) + "',") #              hora
                lista.append("'" + random.sample(state,1)[0] + "',") #      estado
                lista.append("'" + random.sample(entrega,1)[0] + "',") #        tipo_entrega
                local = random.sample(locales, 1)[0]
                cliente = random.sample(clientes_data, 1)[0]
                lista.append(local[0] + ",") #        LP direccion
                lista.append(local[1] + ",") #        LP telefono
                lista.append("'" + cliente[0] + "',") # CL tipodoc
                lista.append(str(cliente[1]) + ",")     # CL numdoc
                lista.append(str(round(random.random()*115, 2)) + ")")
                esc.writerow(lista)
    csvfile.close()


    #PizzaIngrediente
    print("Pizza-Ingrediente")
    with open('csv_files/pizzaingrediente' + file, 'w', newline='') as csvfile:
        with open('csv_files/pizza' + file, newline='') as aux:
            parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            referen = []
            for row in parent:
                referen.append(row[0:2])  #Lp_direeccion, lp_telefono
        aux.close()

        with open('csv_files/ingrediente' + file, 'r', newline='') as ref:
            parent_ing = csv.reader(ref, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            referen_cl = []
            for row in parent_ing:
                referen_cl.append(row[0])
        ref.close()

        if (len(referen_cl) > len(referen)):
            iterar = referen
        else:
            iterar = referen_cl
        
        esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
        for i in referen:
            linea = [""]
            linea.append(str(i[0]).replace(" ", "") + ",")
            linea.append(str(i[1]).replace(" ", "") + ",")
            linea.append(random.sample(referen_cl, 1)[0][1:] + ",")
            linea.append(str(random.randrange(10,500)) + ")")
            esc.writerow(linea)
    csvfile.close()


    #Bebida
    print("Bebidas")
    #bebidas = ['7 Up','A&W Root Beer','Barq\'s Root Beer','Canada Dry Ginger Ale','Cherry Coca-Cola','Coca-Cola Classic','Coca-Cola Zero','Diet Coca-Cola','Diet Dr. Pepper','Diet Pepsi','Dr. Pepper','Fanta Orange','Fresca','Mountain Dew','Mountain Dew Code Red','Mug Root Beer','Orange Crush','Pepsi','Sierra Mist','Sprite','Vanilla Coca-Cola','Wild Cherry Pepsi']
    with open('csv_files/bebida' + file, 'w', newline='') as csvfile:
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
    with open('csv_files/cl_usuario' + file, 'w', newline='') as csvfile:
        esc = csv.writer(csvfile, delimiter=",",quotechar = "\t" , quoting=csv.QUOTE_MINIMAL)
        cont = 0
        for i in tqdm(clientes_users):
            linea = []
            linea.append("('" + str(clientes_data[cont][0]) + "'")
            linea.append(str(clientes_data[cont][1]).replace(" ", ""))
            linea.append(i.strip() + "')")
            esc.writerow(linea)
            cont += 1
    csvfile.close()

    #Rol
    print("Rol")
    roles = ['administrador', 'gerente', 'asistente', 'ayudante', 'laburador', 'españa', 'cliente']
    with open('csv_files/rol' + file, 'w', newline='') as csvfile:
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
    with open('csv_files/usu_rol' + file,'w',  newline='') as csvfile:
        aux.close()
        with open('csv_files/rol' + file, newline='') as aux:
            parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            referen_r = []
            for row in parent:
                referen_r.append(row[0][2:])  #Lp_direeccion, lp_telefono
        aux.close()
        esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
        
        for i in usuarios_t:
            lain = ["('" + i.strip() + "'," + random.sample(referen_r,1)[0] + ")"]
            esc.writerow(lain)

        for i in tqdm(clientes_users):
            lain = ["(" + i.strip() + "'," + random.sample(referen_r,1)[0] + ")"]
            esc.writerow(lain)

    #Turno
    print("Turno")
    fecha = inicio_fech
    with open('csv_files/turno' + file, 'w', newline='') as csvfile:
        esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)
        aydi = 1
        for i in range(0,n_turno):
            lista = ["("]
            lista.append(str(aydi) + ",")
            fecha += diff
            lista.append("'" + str(fecha.time()) + "',")
            hora = "'" + str(random.randrange(0,23)) + ":" + str(random.randrange(0,59)) + ":" + str(random.randrange(0, 59)) + "'"
            lista.append(hora + ")")
            esc.writerow(lista)
            aydi += 1
    csvfile.close()

    #BOleta
    print("Boleta")
    with open('csv_files/boleta' +file,'w', newline='') as csvfile: 
        with open('csv_files/trabajador' + file, newline='') as aux:
            parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            referen = []
            for row in parent:
                referen.append(row[0:2])  #tipo, num de doc
        aux.close()
        fecha = inicio_fech
        dia = timedelta(days = 1)
        esc = csv.writer(csvfile, delimiter=' ',quotechar = " " , quoting=csv.QUOTE_MINIMAL)    
        for i in tqdm(referen):
            for l in range(0,15):
                lista = ["("]
                fecha += dia
                lista.append("'" + str(fecha.date()) + "',") #              fecha
                lista.append(str(round(random.random()*100, 2)) + ",")
                lista.append(i[0][1:] + ",")
                lista.append(i[1] + ",")
                lista.append(str(random.randrange(2,n_turno)) + ")")
                esc.writerow(lista)

    #pedido bebida
    print("Pedido-bebida")
    with open('csv_files/pedido_bebida' + file,'w', newline = "") as csvfile: 
        with open('csv_files/bebida' + file, newline='') as aux:
            parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            referen = []
            for row in parent:
                referen.append(row[0:2])  #nombre, tamaño (bebida)
        aux.close()
        fecha = inicio_fech
        esc = csv.writer(csvfile,quotechar = " " , delimiter = " ", quoting=csv.QUOTE_MINIMAL)    
        for i in tqdm(referen):
            for k in range(0,pbebida):
                fecha += diff
                lista = ["("]

                lista.append("'" + str(fecha.date()) + "',")
                lista.append("'" + str(fecha.time()) + "',")
                lista.append("'" + i[0].strip()[2:] + ",")
                lista.append(i[1].strip() + ",")
                lista.append(str(random.randrange(1,10)) + ")")
                esc.writerow(lista)

    #pedido pizza
    print("Pedido-pizza")
    with open('csv_files/pedido_pizza' + file,'w', newline = "") as csvfile: 
        with open('csv_files/pizza' + file, newline='') as aux:
            parent = csv.reader(aux, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            referen = []
            for row in parent:
                referen.append(row[0:2])  #nombre, tamaño (pizza)
        aux.close()

        esc = csv.writer(csvfile,quotechar = " " , delimiter = " ", quoting=csv.QUOTE_MINIMAL)    
        mat = len(referen)
        ka = 0
        fecha = inicio_fech
        for i in tqdm(referen):
            for k in range(0,p_pizza):
                fecha  += diff
                lista = []
                lista.append("('" + str(fecha.date()) + "',")
                lista.append("'" + str(fecha.time()) + "',")
                lista.append(i[0].strip()[1:] + ",")
                lista.append(i[1].strip() + ",")
                lista.append(str(random.randrange(1,10)) + ")")
                esc.writerow(lista)
            ka += 1
    print("Done!")


cant_datos = 1000000
file = '1000000.csv'
todo(file, cant_datos)

#