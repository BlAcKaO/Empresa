# coding=utf-8
"""Modulo que gestiona las habitaciones.

Este módulo contiene las funciones siguientes:

"""
import variables, conexion, sqlite3


def clearEntry(fila):
    """
    Limpia las entradas de datos de la pestana habitaciones
    @param fila:
    Contiene un listado de widgets de habitaciones que se van a limpiar tras ejecutar un evento.
    @return:
    No retorna nada.
    """
    variables.lblerrordni[1].set_text('')
    for i in range(len(fila)):
        fila[i].set_text('')


def insertarhab(fila):
    """
    Metodo para insertar nuevas habitaciones en la BD.
    @param fila:
    Contiene un conjunto de valores de habitaciones: _numeroHabitacion, _Tipo, _Precio, _Ocupado.
    @return:
    No retorna nada.
    """
    try:
        conexion.cur.execute('insert into habitaciones (numeroHabitacion,tipo,precio,ocupado) values (?,?,?,?)', fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def bajaHab(numero):
    """
    Metodo para dar de baja una habitacion, segun su numero, en la BD.
    @param numero:
    Valor del _Numero de una habitacion.
    @return:
    No retorna nada
    """
    try:
        conexion.cur.execute("delete from habitaciones where numeroHabitacion = ?", (numero,))
        listadohab(variables.listhabitaciones)
        clearEntry(variables.filahab)
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def modificarHab(registro):
    """
    Metodo para modificar una habitacion en la BD.
    @param registro:
    Conjunto de valores de una habitacion: _NumeroHabitacion, _Tipo, _Precio, _Ocupado.
    @return:
    No devuelve nada.
    """
    try:

        conexion.cur.execute(
            "update habitaciones set numeroHabitacion = ?, tipo = ?, precio = ?, ocupado = ? where numeroHabitacion = ?",
            (registro[0], registro[1], registro[2], registro[3], registro[0]))
        conexion.conex.commit()

    except Exception as e:
        print("Error funcion modificar", e)


def listar():
    """
    Retorna todas las habitaciones de la BD.
    @return:
    Retorna un los valores de todas las habitaciones de la BD.
    """
    try:
        conexion.cur.execute('Select * from habitaciones')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        conexion.conex.rollback()


def listadohab(listhabitaciones):
    """
    Metodo para listar las habitaciones, borra el listView y lo vuelve insertar ya con los datos nuevos.
    @param listhabitaciones:
    Datos de las habitaciones que estan cargados en el ListView.
    @return:
    No retorna nada.
    """
    try:
        variables.listado = listar()
        listhabitaciones.clear()
        for registro in variables.listado:
            listhabitaciones.append(registro[0:4])

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def cambiaestadohab(libre, numhabres):
    """
    Metodo para cambiar de estado de libre a ocupado la habitacion.
    @param libre:
    Valor _Libre de la habitacion.
    @param numhabres:
    Valor _Numero de la habitacion.
    @return:
    No retorna nada.
    """
    try:
        print(libre)
        conexion.cur.execute('update habitacion set libre = ? where numero = ?',
                             (libre[0], numhabres))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def findPrecio(habitacion):
    """
    Metodo para buscar el precio de una habitacion.
    @param habitacion:
    Valor _numeroHabitacion.
    @return:
    No retorna nada.
    """
    try:

        conexion.cur.execute('select precio from habitaciones where numeroHabitacion = ?', (habitacion,))
        precio = conexion.cur.fetchall()
        conexion.conex.commit()
        return precio[0][0]

    except Exception as e:
        print("Error funcion buscar precio", e)


def precioTotal(noches, precio):
    """
    Metodo para calcular el precio total segun las noches y el precio por noche.
    @param noches:
    Valor _Noches de reservas.
    @param precio:
    Valor _Precio de habitaciones.
    @return:
    Retorna el precio total.
    """
    total = int(noches) * precio
    round(total)
    return total
