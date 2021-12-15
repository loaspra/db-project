import psycopg2

def persona(cur):
    file_per = open("csv_files/persona1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO persona VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def trabajador(cur): 
    file_per = open("csv_files/trabajador1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO trabajador VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def cliente(cur):
    file_per = open("csv_files/cliente1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO cliente VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def usuario(cur):
    file_per = open("csv_files/users1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO usuario VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def local_de_pizza(cur):
    file_per = open("csv_files/local_de_pizza1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO localdepizza VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def cl_usuario(cur):
    file_per = open("csv_files/cl_usuario1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO cl_usuario VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def rol(cur):
    file_per = open("csv_files/rol1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO rol VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def turno(cur):
    file_per = open("csv_files/turno1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO turno VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def ingredientes(cur):
    file_per = open("csv_files/ingrediente1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO ingrediente VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pedido(cur):
    file_per = open("csv_files/Pedido1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO pedido VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pedido_bebida(cur):
    file_per = open("csv_files/pedido_bebida1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO pedido_bebida VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pedido_pizza(cur):
    file_per = open("csv_files/pedido_pizza1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO pedido_pizza VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def pizza(cur):
    file_per = open("csv_files/pizza1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO pizza VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def bebida(cur):
    file_per = open("csv_files/bebida1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO bebida VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

def usuario_rol(cur):
    file_per = open("csv_files/usu_rol1000000.csv")
    linea = file_per.readline()
    cur = "INSERT INTO usu_rol VALUES "  # cola a ejecutar
    while(linea):
        cur += linea
        linea = file_per.readline()[:-1]
        if(linea != ""):
            cur += ","

    cur += ";"
    return cur

conect = psycopg2.connect(host="localhost", 
                 user="loaspra", 
#                 password="password", 
                 database="serv", 
                 options="-c search_path=public")
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

print("Inserting into: ")
quer = ""
quer = persona(quer)
print("Persona")
cur.execute(quer)
quer = cliente(quer)
print("Cliente")
cur.execute(quer)
quer = local_de_pizza(quer)
print("Local de pizza")
cur.execute(quer)
conect.commit()
conect.close()

conect = psycopg2.connect(host="localhost", 
                 user="loaspra", 
#                 password="password", 
                 database="serv", 
                 options="-c search_path=public")
cur = conect.cursor()
quer = usuario(quer)
print("Usuario")
cur.execute(quer)
quer = trabajador(quer)
print("Trabajador")
cur.execute(quer)
quer = cl_usuario(quer)
print("CL_usuario")
cur.execute(quer)
quer = rol(quer)
print("Rol")
cur.execute(quer)
quer = turno(quer)
print("Turno")
cur.execute(quer)
quer = ingredientes(quer)
print("Ingredientes")
cur.execute(quer)
quer = bebida(quer)
print("Bebida")
cur.execute(quer)
quer = pedido_bebida(quer)
print("Pedido-bebida")
cur.execute(quer)
quer = pizza(quer)
print("Pizza")
cur.execute(quer)
quer = pedido_pizza(quer)
print("Pedido-pizza")
cur.execute(quer)
quer = pedido(quer)
print("Pedido")
cur.execute(quer)
conect.commit()
print("DONE!")