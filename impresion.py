# coding=utf-8
"""Modulo que gestiona la impresion de datos.

Este módulo contiene las funciones siguientes:

"""
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os, funcionesCli, variables, funcionesServ

#Hecho sin IDE

def basico():
    """
    Genera una base para la creacion de la factura.
    @return:
    No retorna nada.
    """
    try:

        global bill
        bill = canvas.Canvas('prueba.pdf', pagesize = A4)
        text1 = 'Bienvenido a nuestro hotel'
        text2 = 'CIF:00000000A'
        bill.drawImage("img/hotel.png", 475, 670, width=64, height=64)
        bill.setFont('Helvetica-Bold', size= 16)
        bill.drawString(250, 780, 'HOTEL LITE')

        bill.setFont('Times-Italic', size = 10)
        bill.drawString(240, 765, text1)
        bill.drawString(260, 755, text2)

        bill.line(50, 660, 540, 660)

        textpie = ('Hotel Lite, CIF = 000000000A, Tlf = 986000000, email =  info"hotelite.com')
        bill.setFont('Times-Italic', size = 7)
        bill.drawString(170, 20, textpie)

        bill.line(50, 30, 540, 30)


    except Exception as e:
        print('Error módulo basico', e)

def factura():
    """
    Metodo encargado de insertar datos en la factura basica.
    @return:
    No retorna nada.
    """
    try:
        basico()

        bill.setTitle('FACTURA:')

        bill.setFont('Helvetica-Bold', size = 9)
        text3 = 'Nº de Factura:'
        bill.drawString(50, 735, text3)

        bill.setFont('Helvetica', size = 8)
        bill.drawString(140,735,variables.datosfactura[0].get_text())

        bill.setFont('Helvetica-Bold', size = 8)
        text4 = 'Fecha Factura:'
        bill.drawString(320,740, text4)

        bill.setFont('Helvetica', size = 8)
        bill.drawString(385,740, variables.datosfactura[1].get_text())

        bill.setFont('Helvetica-Bold', size=8)
        text5 = 'DNI CLIENTE:'
        bill.drawString(50, 710, text5)

        bill.setFont('Helvetica', size=8)
        bill.drawString(120, 710, variables.datosfactura[2].get_text())

        bill.setFont('Helvetica-Bold', size=8)
        text6 = 'Nº de Habitación:'
        bill.drawString(320, 710, text6)

        bill.setFont('Helvetica', size=8)
        bill.drawString(385, 710, variables.datosfactura[3].get_text())

        apelnome = funcionesCli.apelnomfac(variables.datosfactura[2].get_text())
        bill.setFont('Helvetica-Bold',size = 8)
        text7 = 'Apellidos: '
        bill.drawString(50,680,text7)
        bill.setFont('Helvetica', size=8)
        bill.drawString(110,680, apelnome[0])

        bill.setFont('Helvetica-Bold',size = 8)
        text8 = 'Nombre:'
        bill.drawString(300,680,text8)

        bill.setFont('Helvetica', size=8)
        bill.drawString(350,680, apelnome[1])

        bill.setFont('Helvetica-Bold', size = 10)
        text9 = ['CONCEPTO', 'UNIDADES', 'PRECIO/UNIDAD', 'TOTAL']
        x = 75
        for i in range (0,4):
            bill.drawString(x,645, text9[i])
            x += 132
        listado = funcionesServ.buscarServicios(str(variables.datosfactura[0].get_text()))
        x = 75
        y = 620
        bill.drawString(x, y, 'Noches')
        x += 150

        for i in range(5,8):
            if i == 7:
                x += 34
                bill.drawRightString(x,y, (variables.mensfac[i].get_text() + ' €'))
            else:
                bill.drawString(x,y, variables.mensfac[i].get_text())
            x = x + 123

        x = 74
        y = y - 20
        for registro in listado:
            for i in range(2):
                if i == 1:
                    x += 40
                    bill.drawRightString(x, y, str(registro[i]) + ' €')
                else:
                    bill.drawString(x, y, str(registro[i]))
                x = 390 + x
            y = y - 20
            x = 75

        bill.line(50, 120, 540, 120)
        textsubt = ('Subtotal : ' + variables.linfacfinal[0].get_text())
        bill.drawRightString(495, 100, str(textsubt))
        textiva = ('IVA:   ' + variables.linfacfinal[1].get_text())
        bill.drawRightString(495, 80, str(textiva))
        texttotal = ('TOTAL:   ' + variables.linfacfinal[2].get_text())
        bill.drawRightString(495, 60, str(texttotal))
        bill.line(50, 635, 540, 635)
        bill.showPage()
        bill.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/prueba.pdf')

    except Exception as e:
        print('Error en el módulo factura ',e)
