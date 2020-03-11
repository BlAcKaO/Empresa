# coding=utf-8
"""Modulo que gestiona las reservas.

Este módulo contiene las funciones siguientes:

"""

import conexion, sqlite3, variables
from datetime import datetime

def clearEntry(fila):
    """
    Limpia las entradas de datos de la pestana reservas.
    @param fila:
    Contiene un listado de widgets de reservas que se van a limpiar tras ejecutar un evento.
    @return:
    No retorna nada.
    """
    for i in range(len(fila)):
        fila[i].set_text('')
    variables.cmbreserhabitacion.set_active(-1)

def calculardias():
    """
    Metodo para calcular el numero de dias que va a tener la reserva segun la fecha de entrada y la  de salida.
    @return:
    No retorna nada.
    """
    diaentrada = variables.filareserva[2].get_text()
    diasalida = variables.filareserva[3].get_text()
    if diaentrada != '' and diasalida !='':
        date_in = datetime.strptime(diaentrada, '%d/%m/%Y').date()
        date_out = datetime.strptime(diasalida, '%d/%m/%Y').date()
        noches = (date_out-date_in).days
        if noches < 0:
            variables.lblnumnoches.set_text("0")
        else:
            variables.lblnumnoches.set_text(str(noches))

def insertarReservas(fila):
    """
    Metodo para insertar nuevas reservas en la BD.
    @param fila:
    Contiene un conjunto de valores de reservas: _Dni, _Apellidos, _NumHabitacion, _CheckIn, _CheckOut y _Noches.
    @return:
    No retorna nada
    """
    try:

        conexion.cur.execute('insert into reservas (dni,Apellidos,numHabitacion,checkIn,checkOut,Noches) values(?,?,?,?,?,?)',fila)
        conexion.conex.commit()
        clearEntry(variables.filareserva)
    except Exception as e:
        print("Insertar Reserva Funcion",e)

def bajasReservas(dni,fecha):
    """
    Metodo para dar de baja reservas en la BD.
    @param dni:
    Valor _Dni de reservas.
    @param fecha:
    Valor _CheckIn de reservas.
    @return:
    No retorna nada.
    """
    try:

        conexion.cur.execute('delete from Reservas where dni = ? and checkIn = ?',(dni,fecha,))
        conexion.conex.commit()
        listadoreservas(variables.listreservas)
        clearEntry(variables.filareserva)

    except Exception as e:
        print("Error bajas reservas",e)

def modificarReserva(registro):
    """
    Metodo para modificar las reservas en la BD.
    @param registro:
    Conjunto de valores de la reserva: _Dni, _Apellidos, _numHabitacion, _CheckIn, _CheckOut y _Noches.
    @return:
    No devuelve nada.
    """
    try:
        if len(registro) < 6:
            conexion.cur.execute('update reservas set dni = ?, Apellidos = ?, numHabitacion = ?,checkIn = ?,checkOut = ?, Noches = ? where dni = ?',(registro[0],registro[1], registro[2],registro[3],registro[4],registro[5],registro[0]))
            conexion.conex.commit()
        else:
            conexion.cur.execute('update reservas set dni = ?, Apellidos = ?, numHabitacion = ?,checkIn = ?,checkOut = ?, Noches = ? where dni = ?',(registro[0],registro[1], registro[2],registro[3],registro[4],registro[5],registro[6]))
            conexion.conex.commit()

    except Exception as e:
        print("Error modificar funcion",e)
        conexion.conex.rollback()

def listar():
    """
    Retorna todas las reservas de la BD.
    @return:
    Retorna un los valores de todas las reservas de la BD.
    """

    try:
        conexion.cur.execute('Select * from reservas')
        listadoReservas = conexion.cur.fetchall()
        conexion.conex.commit()
        return listadoReservas

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadonumhab(self):
    """
    Metodo para buscar los numeros de las habitaciones.
    @return:
        No retorna nada.
    """
    try:
        conexion.cur.execute('select numeroHabitacion from habitaciones')
        listado = conexion.cur.fetchall()
        variables.listhabitacionescombobox.clear()
        for row in listado:
            variables.listhabitacionescombobox.append(row)
            conexion.conex.commit()
    except Exception as e:
        print(e)
        conexion.conex.rollback()

def listadoreservas(listreservas):
    """
    Metodo para listar las reservas, borra el listView y lo vuelve insertar ya con los datos nuevos.
    @param listreservas:
    Datos de las reservas que estan cargados en el ListView.
    @return:
    No retorna nada.
    """
    try:
        variables.listado = listar()
        listreservas.clear()
        for registro in variables.listado:
            listreservas.append(registro[0:6])


    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarHabitacion(habitacion):
    """
    Metodo para mostrar el numero de la habitacion en el comboBox.
    @param habitacion:
    Valor _NumeroHabitacion de habitaciones.
    @return:
    No retorna nada.
    """
    try:
        contador = 0
        conexion.cur.execute('select numeroHabitacion from habitaciones')
        variables.numhab = conexion.cur.fetchall()
        conexion.conex.commit()

        for numero in variables.numhab:

            if numero[0] == habitacion:
                variables.cmbreserhabitacion.set_active(contador)
            else:
                contador += 1

    except Exception as e:
        print(e)

def findID(dni,habitacion):
    """
    Metodo para buscar el codigo de una habitacion.
    @param dni:
    Valor _Dni de reservas.
    @param habitacion:
    Valor _NumHabitacion de reservas.
    @return:
    Retorna codigo.
    """
    try:

        conexion.cur.execute('select codigo from reservas where dni = ? and numHabitacion = ?',(dni,habitacion,))
        codigo = conexion.cur.fetchall()
        conexion.conex.commit()
        return codigo[0][0]

    except Exception as e:
        print("funcion buscar ID",e)

