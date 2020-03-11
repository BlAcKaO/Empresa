# coding=utf-8
"""Modulo que gestiona los servicios.

Este módulo contiene las funciones siguientes:

"""
import variables, conexion, sqlite3

def clearEntry(fila):
    """
    Limpia las entradas de datos de la pestana servicios
    @param fila:
    Contiene un listado de widgets de servicios que se van a limpiar tras ejecutar un evento
    @return:
    No devuelve nada
    """
    variables.lblerrordni[1].set_text('')
    for i in range(len(fila)):
        fila[i].set_text('')

def insertarSer(fila):
    """
    Inserta un nuevo servicio en la BD.
    @param fila:
    Contiene un conjunto de valores _Concepto, _Precio, -CodRes y _numHab los cuales seran utilizados para insertar un nuevo servicio.
    @return:
    No retorna nada
    """
    try:
        conexion.cur.execute('insert into Servicios (concepto, precio, iva, codRes, numHab) values (?,?,?,?,?)',fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


# Select para utilizar en las operaciones de datos

def listar():
    """
    Metodo para mostrar todos los servicios.
    @return:
    Retorna el conjunto de valores de todos los servicios
    """
    try:
        conexion.cur.execute('Select * from Servicios')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def bajaSer(cod):
    """
    Metodo para borrar servicios de la BD.
    @param cod:
    Valor del _Cod de servicios.
    @return:
    No retorna nada.
    """
    try:
        conexion.cur.execute("delete from Servicios where cod = ?",(cod,))
        conexion.conex.commit()
        listadoSer(variables.listservicios)
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def modifSer(registro,cod):
    """
    Metodo para modificar los servicios.
    @param registro:
    Contiene los valores _Concepto y _Precio.
    @param cod:
    Valor del _Cod de servicios.
    @return:
    No retorna nada.
    """
    try:
        conexion.cur.execute("update Servicios set concepto = ? , precio = ? where cod = ?",(registro[0],registro[1],cod))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()



def listadoSer(listservicios):
    """
    Metodo para listar los servicios, borra el listView y lo vuelve insertar ya con los datos nuevos.
    @param listservicios:
    Datos de los servicios que estan cargados en el ListView.
    @return:
    No retorna nada.
    """
    try:
        variables.listado = listar()
        print(variables.listado)
        listservicios.clear()
        for registro in variables.listado:
            codigo = variables.listado[0]
            listservicios.append(registro[0:3])

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()



def selectServicios(cod):
    """
    Devuelve los datos de un servicio por su codigo.
    @param cod:
    Valor del _Cod de servicios.
    @return:
    Devuelve los datos de un servicio.
    """
    try:
        conexion.cur.execute('select precio from Servicios where cod = ?',(cod,))
        listado = conexion.cur.fetchone()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarServicios(codRes):
    """
    Devuelve el concepto de un servicio segun su codigo de reserva.
    @param codRes:
    Valor del _Cod de reservas.
    @return:
    Retorna el valor del concepto.
    """
    try:
        conexion.cur.execute('select concepto, precio, iva from Servicios where codRes = ?', (codRes,))
        concepto = conexion.cur.fetchall()
        conexion.conex.commit()
        print(concepto)
        return concepto
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def comprobarExistencia(codRes, concepto):
    """
    Metodo para comprobar la existencia de un servicio en concreto para una reserva.
    @param codRes:
    Valor del _Cod de reservas.
    @param concepto:
    Valor del _Concepto de servicios.
    @return:
    Si no encuentra el servicio lo retorna y si lo encuentra retorna null.
    """
    servicios = buscarServicios(codRes)

    i = 0
    for registro in servicios:
        if registro[0] == concepto:
            i = 1
    if i == 1:
        return servicios
    else:
        return ''