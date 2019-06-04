import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from Modelo.Agenda import Agenda
from Controle.AgendaControle import AgendaControle
class MAgenda(AgendaControle):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("../visual/Agenda.glade")
        self.janela = builder.get_object("winAge")
        self.Fds = builder.get_object("diaF")
        self.prim = builder.get_object("cbtPri")
        self.seg = builder.get_object("cbtSeg")
        self.ter = builder.get_object("cbtTer")
        self.qua = builder.get_object("cbtQuar")
        self.qui = builder.get_object("cbtQui")
        self.sex = builder.get_object("cbtSex")
        self.set = builder.get_object("cbtSet")
        self.oi = builder.get_object("cbtOi") 
        self.no = builder.get_object("cbtNo") 
        self.logo = builder.get_object("labLogo")
        self.Agenda = builder.get_object("labAgenda")
        self.dP = builder.get_object("labDaP")
        self.desemp = builder.get_object("labDes")
        self.Aagenda = builder.get_object("calAge")
        builder.connect_signals(self)
        self.janela.show_all()
        self.janela.connect("destroy",Gtk.main_quit)
        Gtk.main()
        
    def Fds2(self,evt):
        self.janela.hide()
        self.Fds.show_all()
    def cancelar(self,evt):
            self.Fds.hide()
            self.janela.show_all()
            
    def ok(self,evt):
        self.pri = self.prim.get_active_text()
        self.segu = self.seg.get_active_text()
        self.terc = self.ter.get_active_text()
        self.quar = self.qua.get_active_text()
        self.quin = self.qui.get_active_text()
        self.sext = self.sex.get_active_text()
        self.seti = self.set.get_active_text()
        self.oit = self.oi.get_active_text()
        self.nov = self.no.get_active_text()
m = MAgenda()