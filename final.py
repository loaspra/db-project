import psycopg2

def persona(cur, file, esquema):
    file_per = open("csv_files/persona" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.persona VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","
    cur += ";"
    return cur

def trabajador(cur, file, esquema): 
    file_per = open("csv_files/trabajador" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.trabajador VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","
    cur += ";"
    return cur

def cliente(cur, file, esquema):
    file_per = open("csv_files/cliente" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.cliente VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def usuario(cur, file, esquema):
    file_per = open("csv_files/users" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.usuario VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def local_de_pizza(cur, file, esquema):
    file_per = open("csv_files/local_de_pizza" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.localdepizza VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def cl_usuario(cur, file, esquema):
    file_per = open("csv_files/cl_usuario" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.cl_usuario VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def rol(cur, file, esquema):
    file_per = open("csv_files/rol" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.rol VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def turno(cur, file, esquema):
    file_per = open("csv_files/turno" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.turno VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def boleta(cur, file, esquema): 
    file_per = open("csv_files/boleta" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.boleta VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","
    cur += ";"
    return cur

def ingredientes(cur, file, esquema):
    file_per = open("csv_files/ingrediente" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.ingrediente VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pedido(cur, file, esquema):
    file_per = open("csv_files/Pedido" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.pedido VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pedido_bebida(cur, file, esquema):
    file_per = open("csv_files/pedido_bebida" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.pedido_bebida VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pedido_pizza(cur, file, esquema):
    file_per = open("csv_files/pedido_pizza" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.pedido_pizza VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pizza(cur, file, esquema):
    file_per = open("csv_files/pizza" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.pizza VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pizzaingrediente(cur, file, esquema):
    file_per = open("csv_files/pizzaingrediente" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.pizzaingrediente VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def bebida(cur, file, esquema):
    file_per = open("csv_files/bebida" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.bebida VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def usuario_rol(cur, file, esquema):
    file_per = open("csv_files/usu_rol" + file)
    linea = file_per.readline()
    cur = 'INSERT INTO ' + esquema + '.usu_rol VALUES '  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def realz(sch_name, file):
    conect = psycopg2.connect(host="localhost", 
                    user="loaspra", 
                    database="serv", 
                    options='-c search_path=' + sch_name)
    cur = conect.cursor()

    #Orden:
    # 1. Persona
    # 2. Cliente
    # 3. local de pizza
    # 4. usuario
    # 5. Trabajador
    # 6. Cliente-usuario
    # 7. Roles
    # 8. Turnos
    # 9. Ingredientes
    # xx. Bebida
    # 10. Pedido Bebida
    # 11. Pizza
    # 12. Pedido pizza
    # 13. Pedido

    print('INSERTING into: ')
    quer = ""
    quer = persona(quer, file, sch_name)
    print("Persona")
    cur.execute(quer)
    quer = cliente(quer, file, sch_name)
    print("Cliente")
    cur.execute(quer)
    quer = local_de_pizza(quer, file, sch_name)
    print("Local de pizza")
    cur.execute(quer)
    conect.commit()
    conect.close()

    conect = psycopg2.connect(host="localhost", 
                    user="loaspra", 
                    database="serv", 
                    options='-c search_path=' + sch_name)
    cur = conect.cursor()
    quer = usuario(quer, file, sch_name)
    print("Usuario")
    cur.execute(quer)
    quer = trabajador(quer, file, sch_name)
    print("Trabajador")
    cur.execute(quer)
    quer = cl_usuario(quer, file, sch_name)
    print("CL_usuario")
    cur.execute(quer)
    quer = rol(quer, file, sch_name)
    print("Rol")
    cur.execute(quer)
    quer = usuario_rol(quer, file, sch_name)
    print("Usuario-rol")
    cur.execute(quer)
    quer = turno(quer, file, sch_name)
    print("Turno")
    cur.execute(quer)
    quer = boleta(quer, file, sch_name)
    print("Boleta")
    cur.execute(quer)
    quer = ingredientes(quer, file, sch_name)
    print("Ingredientes")
    cur.execute(quer)
    quer = bebida(quer, file, sch_name)
    print("Bebida")
    cur.execute(quer)
    quer = pedido(quer, file, sch_name)
    print("Pedido")
    cur.execute(quer)
    quer = pedido_bebida(quer, file, sch_name)
    print("Pedido-bebida")
    cur.execute(quer)
    quer = pizza(quer, file, sch_name)
    print("Pizza")
    cur.execute(quer)
    quer = pizzaingrediente(quer, file, sch_name)
    print("Pizza-Ingrediente")
    cur.execute(quer)
    quer = pedido_pizza(quer, file, sch_name)
    print("Pedido-pizza")
    cur.execute(quer)

    conect.commit()
    print("DONE!")


sch_name = '"Pizza(1000000)"'

file = "1000000.csv"
realz(sch_name, file)