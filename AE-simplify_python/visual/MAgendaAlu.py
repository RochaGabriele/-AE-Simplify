import gi
from Controle.AgendaControle import AgendaControle
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class MAgendaAlu(AgendaControle):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("../visual/AgendaAlu.glade")
        self.janela = builder.get_object("aluAge")
        self.diaAlu = builder.get_object("DiaAlu")
        self.pri = builder.get_object("entP")
        self.segu = builder.get_object("entS")
        self.terc = builder.get_object("entTre")
        self.quar = builder.get_object("entQua")
        self.quin = builder.get_object("entQui")
        self.sext = builder.get_object("entSex")
        self.sete = builder.get_object("entSet")
        self.oi = builder.get_object("entOi")
        self.no = builder.get_object("entNo")
        self.logo = builder.get_object("logoLa")
        self.Agenda = builder.get_object("labAge")
        self.dP = builder.get_object("labDP")
        self.desemp = builder.get_object("labDese")
        self.Aagenda = builder.get_object("ageCal")
        builder.connect_signals(self)
        self.janela.show_all()
        self.janela.connect("destroy",Gtk.main_quit)
        Gtk.main()
    def mostrar(self,evt):
        self.janela.hide()
        self.diaAlu.show_all()
    def voltar(self,evt):
        self.diaAlu.hide()
        self.janela.show_all()
        
aAge = MAgendaAlu()
