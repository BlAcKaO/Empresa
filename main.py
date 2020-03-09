# coding=utf-8
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk
import eventos, conexion, variables, funcionesCli, funcionesHab, funcionesReservas, funcionesServ

"""El main contiene los elementos necesarios para lanzar la aplicación
asi como la decleración de los widgets que se usarán. También los módulos
que tenemos que importar de las librerías gráficas.

"""


class Empresa:
    def __init__(self):

        b = Gtk.Builder()
        b.add_from_file('ventana.glade')


        self.vprincipal = b.get_object("vPrincipal")

        # Declaración de Widgets
        self.entdni = b.get_object('entDni')
        self.entapellidos = b.get_object('entApellidos')
        self.entnombre = b.get_object('entNombre')
        self.lblerrordni = b.get_object('lblErrorDni')
        self.lblcodcli = b.get_object('lblCodCli')
        self.vencalendar = b.get_object('venCalendar')
        self.calendar = b.get_object('Calendar')
        self.entfechaCli = b.get_object('entFechaCli')
        variables.panel = b.get_object('Panel')
        variables.filacli = (self.entdni, self.entapellidos, self.entnombre, self.entfechaCli)
        variables.listclientes = (b.get_object('listClientes'))
        variables.treeclientes = (b.get_object('treeClientes'))
        variables.lblerrordni = (self.lblerrordni, self.lblcodcli)
        variables.lbladded = b.get_object('lblAdded')
        variables.lblfecha = b.get_object('lblFecha')
        variables.vencalendar = self.vencalendar
        variables.calendar = self.calendar

        # Variables Habitaciones
        self.entnumero = b.get_object('entNumero')
        self.rbsimple = b.get_object('rbSimple')
        self.rbdouble = b.get_object('rbDouble')
        self.rbfamiliar = b.get_object('rbFamiliar')
        self.entprecio = b.get_object('entPrecio')
        variables.switch = b.get_object('Switch')

        # Variables Acerca de:
        variables.venacercade = b.get_object('venAbout')

        variables.venfile = b.get_object('venFile')
        variables.menubar = b.get_object('menuBar').get_style_context()

        # Preparando para backup
        #variables.vendialog = b.get_object('venDialog')
        variables.lblmensajedialog = b.get_object('lblMensajeDialog')
        variables.vendialogcorrecto = b.get_object('venDialogCorrecto')
        variables.venfiledialog = b.get_object('venFileDialog')

        variables.filahab = (self.entnumero, self.entprecio)
        variables.filarbt = (self.rbsimple, self.rbdouble, self.rbfamiliar)
        variables.listhabitaciones = (b.get_object('listHabitaciones'))
        variables.treehabitaciones =  (b.get_object('TreeHabitaciones'))

        # Reservas
        variables.lblreservasdni = b.get_object('lblReservasDni')
        variables.lblreservasapellidos = b.get_object('lblReservasApellidos')
        variables.listhabitacionescombobox = b.get_object('ListHabitacionesComboBox')
        variables.lblnumnoches = b.get_object('lblNumNoches')
        variables.btncheckin = b.get_object('btnCheckIn')
        variables.btncheckout = b.get_object('btnCheckOut')
        variables.entcheckin = b.get_object('entCheckIn')
        variables.entcheckout = b.get_object('entCheckOut')
        variables.cmbreserhabitacion = b.get_object('cmbReservasHabitacion')
        variables.filareserva = (variables.lblreservasdni, variables.lblreservasapellidos,variables.entcheckin,variables.entcheckout,variables.lblnumnoches)
        variables.listreservas = (b.get_object('listReservas'))
        variables.treereservas = (b.get_object('treeReservas'))
        variables.vencalendarr1 = self.vencalendar
        variables.vencalendarr2 = self.vencalendar

        # Variables Facturación
        variables.lbldnifacturacion = b.get_object('lblDniFacturacion')
        variables.lblapellidosfacturacion = b.get_object('lblApellidosFacturacion')
        variables.lblnombrefacturacion = b.get_object('lblNombreFacturacion')
        variables.lblcodigoreserva = b.get_object('lblCodigoReserva')
        variables.lblhabitacionfacturacion = b.get_object('lblHabitacionFacturacion')
        variables.lblfechafacturacion = b.get_object('lblFechaFacturacion')

        variables.lblnochesfac = b.get_object('lblNochesFac')
        variables.lblunidadesfac = b.get_object('lblUnidadesFac')
        variables.lblpreciounidadfac = b.get_object('lblPrecioUnidadFac')
        variables.lbltotalunifac = b.get_object('lblTotalUniFac')
        
        variables.filafacturacion = (variables.lblnochesfac, variables.lblunidadesfac, variables.lblpreciounidadfac, variables.lbltotalunifac)

        variables.lblconcepto1 = b.get_object('lblConcepto1')
        variables.lbltotaulunifac1 = b.get_object('lblTotalUniFac1')
        variables.lblconcepto2 = b.get_object('lblConcepto2')
        variables.lbltotaulunifac2 = b.get_object('lblTotalUniFac2')
        variables.lblconcepto3 = b.get_object('lblConcepto3')
        variables.lbltotaulunifac3 = b.get_object('lblTotalUniFac3')
        variables.lblconcepto4 = b.get_object('lblConcepto4')
        variables.lbltotaulunifac4 = b.get_object('lblTotalUniFac4')

        variables.filaserviciosfac = (variables.lblconcepto1, variables.lbltotaulunifac1,
                                      variables.lblconcepto2, variables.lbltotaulunifac2,
                                      variables.lblconcepto3, variables.lbltotaulunifac3,
                                      variables.lblconcepto4, variables.lbltotaulunifac4)

        # Variables servicios
        variables.lblcodres = b.get_object('lblCodRes')
        variables.lblhabres = b.get_object('lblHabRes')
        variables.chkparking = b.get_object('chkParking')
        variables.chkdesayuno = b.get_object('chkDesayuno')
        variables.chkcomida = b.get_object('chkComida')
        variables.listservicios = (b.get_object('listServicios'))
        variables.entconcepto = b.get_object('entConcepto')
        variables.entprecioserv = b.get_object('entPrecioServ')
        variables.treeservicios = (b.get_object('treeServicios'))
        variables.filaservicios = (variables.lblcodres, variables.lblhabres, variables.entconcepto, variables.entprecioserv)

        b.connect_signals(eventos.Eventos())

        # Estilos
        self.set_styles()
        variables.menubar.add_class('menuBar')

        self.vprincipal.show()
        conexion.Conexion().abrirBBDD()
        funcionesCli.listadocli(variables.listclientes)
        funcionesHab.listadohab(variables.listhabitaciones)
        funcionesReservas.listadoreservas(variables.listreservas)
        funcionesReservas.listadonumhab(self)
        funcionesServ.listadoSer(variables.listservicios)


    def set_styles(self):
        """
        Metodo para cargar los estilos css.
        @return:
        No retorna nada.
        """
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('styles.css')
        Gtk.StyleContext().add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

if __name__ == '__main__':
    main = Empresa()
    Gtk.main()