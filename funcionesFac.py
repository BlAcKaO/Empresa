# coding=utf-8
"""Modulo que gestiona las reservas.

Este módulo contiene las funciones siguientes:

"""

import conexion, sqlite3, variables
from datetime import datetime

def buscarServicios(codRes):
    try:
        conexion.cur.execute('select * from Servicios where codRes = ?', (codRes))
        variables.servicios = conexion.cur.fetchall()
        conexion.conex.commit()

    except Exception as e:
        print(e)