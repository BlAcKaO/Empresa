# coding=utf-8
"""Modulo que gestiona los clientes.

Este módulo contiene las funciones siguientes:

"""
import conexion, sqlite3, variables, time

def clearEntry(fila):
    """
    Limpia las entradas de datos de la pestana clientes
    @param fila:
    Contiene un listado de widgets de clientes que se van a limpiar tras ejecutar un evento.
    @return:
    No devuelve nada.
    """
    variables.lblerrordni[1].set_text('')
    for i in range(len(fila)):
        fila[i].set_text('')

def validarDNI(dni):
    """
    Controla que el dni sea correcto.
    @param dni:
    Valor del _Dni cliente.
    @return:
    Devuelve un boolean.
    """

    try:

        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0','Y':'1','Z':'2'}
        numeros = "1234567890"
        dni = dni.upper()

        if len(dni) == 9:

            dig_control = dni[8]
            dni = dni[:8]

            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])

            return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23] == dig_control

        return False

    except Exception as e:
         print (e)
         return None

# Inserta un registro
def insertarcli(fila):
    """
    Inserta un nuevo cliente en la BD.
    @param fila:
    Contiene un conjunto de valores _Dni, _Apellidos, _Nombre y _Fecha los cuales seran utilizados para insertar un nuevo cliente.
    @return:
    No retorna nada
    """

    try:
        conexion.cur.execute('insert into clientes (dni,Apellidos,Nombre,Fecha) values (?,?,?,?)',fila)
        conexion.conex.commit()

        variables.lbladded.set_text('Cliente creado')
        variables.lblfecha.set_text(time.strftime("%c"))

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


# Select para utilizar en las operaciones de datos

def listar():
    """
    Retorna todos los clientes de la BD.
    @return:
    Retorna el conjunto de variables de todos los clientes registrados en la BD.
    """

    try:
        conexion.cur.execute('Select * from clientes')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def bajaCli(dni):
    """
    Metodo para dar de baja un cliente especifico.
    @param dni:
    Valor del _Dni de un cliente.
    @return:
    No retorna nada.
    """
    try:
        conexion.cur.execute("delete from clientes where dni = ?",(dni,))
        listadocli(variables.listclientes)
        clearEntry(variables.filacli)
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def modifCli(registro,cod):
    """
    Metodo para modificar un cliente.
    @param registro:
    Conjunto de variables _Dni, _Apellidos, _Nombre y _Fecha de un cliente.
    @param cod:
    Valor del _Cod de un cliente.
    @return:
    No retorna.
    """
    try:
        conexion.cur.execute("update clientes set dni = ?, Apellidos = ? , Nombre = ?, Fecha = ? where id = ?",(registro[0],registro[1],registro[2],registro[3],cod))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


# Esta funcion carga el treeview con los datos de la tabla clientes

def listadocli(listclientes):
    """
    Metodo para listar los clientes, borra el listView y lo vuelve insertar ya con los datos nuevos.
    @param listclientes:
    Datos de los clientes que estan cargados en el ListView.
    @return:
    No retorna nada.
    """
    try:
        variables.listado = listar()
        listclientes.clear()
        for registro in variables.listado:
            codigo = variables.listado[0]
            listclientes.append(registro[1:5])

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def selectcli(dni):
    """
    Devuelve los datos de un cliente por su dni.
    @param dni:
    Valor del _Dni de un cliente.
    @return:
    Devuelve los datos de un cliente.
    """
    try:
        conexion.cur.execute('select id from clientes where dni = ?',(dni,))
        listado = conexion.cur.fetchone()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def findNombre(dni):
    """
    Devuelve el nombre de un cliente segun su DNI.
    @param dni:
    Valor del _Dni de un cliente.
    @return:
    Devuelve el nombre de un cliente.
    """
    try:

        conexion.cur.execute('select nombre from clientes where dni = ? ',(dni,))
        nombre = conexion.cur.fetchall()
        conexion.conex.commit()
        return nombre[0][0]
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def findApellidos(dni):
    """
    Devuelve los apellidos de un cliente segun su DNI.
    @param dni:
    Valor del _Dni de un cliente.
    @return:
    Devuelve los apellidos de un cliente.
    """
    try:

        conexion.cur.execute('select apellidos from clientes where dni = ? ',(dni,))
        apellido = conexion.cur.fetchall()
        conexion.conex.commit()
        return apellido[0][0]
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def apelnomfac(dni):
    """
    Devuelve los apellidos y el nombre de un cliente segun su DNI.
    @param dni:
    Valor del _Dni de un cliente.
    @return:
    Devuelve los apellidos y nombre de un cliente.
    """
    try:

        conexion.cur.execute('select Apellidos, Nombre from clientes where dni = ?',(dni,))
        apelnome = conexion.cur.fetchall()
        conexion.conex.commit()
        return apelnome[0]

    except sqlite3.OperationalError as e:
        print(e)
