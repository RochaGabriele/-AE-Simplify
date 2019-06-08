"""

        classe de execução para o agendamento de salas 
"""

__author__="José Maik Freitas dos Santos"
__version__="1.0.1"


import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
from Modelo.Agenda import Agenda
from Controle.AgendaControle import AgendaControle

class MAgenda():
    def Age_style(self):
        css = b"""
            .winAge{
                background-color:#1d771d;
                font-size: 15px;
                font-weight:bold;
                font-family:Times New Roman;

            }
            .diaF{
                background-color:#1d771d;
                font-size: 15px;
                font-weight:bold;
                font-family:Times New Roman;

            }
            .DiaALu{
                background-color:#1d771d;
                font-size: 15px;
                font-weight:bold;
                font-family:Times New Roman;
            }
            """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
   
    def __init__(self):
        self.Age_style()
        builder = Gtk.Builder()
        builder.add_from_file("visual/Agenda.glade")
        self.janela = builder.get_object("winAge")
        self.logo = builder.get_object("labLogo")
        self.Agenda = builder.get_object("labAgenda")
        self.dP = builder.get_object("labDaP")
        self.desemp = builder.get_object("labDes")
        self.Aagenda = builder.get_object("calAge")
        self.butAge = builder.get_object("butAge")
        self.Fds = builder.get_object("diaF")
        self.prim = builder.get_object("cbtPri")
        self.seg = builder.get_object("cbtSeg")
        self.ter = builder.get_object("cbtTer")
        self.qua = builder.get_object("cbtQua")
        self.qui = builder.get_object("cbtQui")
        self.sex = builder.get_object("cbtSex")
        self.set = builder.get_object("cbtSet")
        self.oi = builder.get_object("cbtOi") 
        self.no = builder.get_object("cbtNo") 
        self.diaAlu = builder.get_object("DiaAlu")
        self.labP = builder.get_object("labP")
        self.labS = builder.get_object("labS")
        self.labTer = builder.get_object("labTer")
        self.labQua = builder.get_object("labQu")
        self.labQuin = builder.get_object("labQuinta")
        self.labSext = builder.get_object("labSext")
        self.labSete = builder.get_object("labSeti")
        self.labOit = builder.get_object("labOita")
        self.labNov = builder.get_object("labNona")
        builder.connect_signals(self)
        self.Age_style()
        self.janela.show_all()
        self.janela.connect("destroy",Gtk.main_quit)
        Gtk.main()
        
    def Definir(self,evt):
        self.janela.hide()
        self.Fds.show_all()
    def cancelar(self,evt):
        self.Fds.hide()
        self.janela.show_all()
            
    def ok(self,evt):
        self.ac.salas(self.prim.get_active_text(), self.seg.get_active_text(),
        self.ter.get_active_text(), self.qua.get_active_text(), self.qui.get_active_text(),self.sex.get_active_text(), self.set.get_active_text(),self.oi.get_active_text(),self.no.get_active_text())
        self.Fds.hide()
        self.janela.show_all()
    def ver(self,evt):
        self.Agec = AgendaControle()
        self.a = Agenda()
        self.janela.hide()
        self.diaAlu.show_all()
        self.Agec.salas(self.prim.get_active_text(), self.seg.get_active_text(),
        self.ter.get_active_text(),self.qua.get_active_text(),self.qui.get_active_text(),self.sex.get_active_text(), self.set.get_active_text(),self.oi.get_active_text(),self.no.get_active_text())
        self.labP.set_text(self.prim.get_active_text())
        self.labS.set_text(self.seg.get_active_text())
        self.labTer.set_text(self.ter.get_active_text())
        self.labQua.set_text(self.qua.get_active_text())
        self.labQuin.set_text(self.qui.get_active_text())
        self.labSext.set_text(self.sex.get_active_text())
        self.labSete.set_text(self.set.get_active_text())
        self.labOit.set_text(self.oi.get_active_text())
        self.labNov.set_text(self.no.get_active_text())
        self.Age_style()
    def voltar(self,evt):
            self.diaAlu.hide()
            self.janela.show_all()
