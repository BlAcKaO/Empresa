# coding=utf-8
"""Modulo que gestiona la Base de Datos.

Este módulo contiene las funciones siguientes:

"""
import sqlite3, variables

#Clase de Examen

class Conexion:

    def abrirBBDD(self):
        """
        Método encargado de realizar la conexion con la BD.
        :return:
        No retorna nada.
        """
        try:

            global bbdd, conex, cur

            bbdd = 'empresa.sqlite'         #Variable almacena base de datos

            conex = sqlite3.connect(bbdd)   #Abrimos la base de datos
            cur = conex.cursor()            #cursor

            print('Conexión a base de datos realizada correctamente')

        except sqlite3.OperationalError as e:
            print('Error al abrir: ', e)

    def cerrarBBDD(self):
        """
        Metodo encargado de cerrar la BD.
        :return:
        No  retorna nada.
        """

        try:
            cur.close()
            conex.close()

            print('Conexion a base de datos cerrada correctamente')

        except sqlite3.OperationalError as e:
            print('Error al cerrar', e)