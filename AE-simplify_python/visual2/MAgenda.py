import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class MAgenda:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/Agenda.glade")
        self.janela = builder.get_object("winAge")
        self.Fds = builder.get_object("Fds")
        self.logo = builder.get_object("labLogo")
        self.Agenda = builder.get_object("labAgenda")
        self.dP = builder.get_object("labDaP")
        self.desemp = builder.get_object("labDes")
        self.Aagenda = builder.get_object("calAge")
        builder.connect_signals(self)
        self.janela.show_all()
        Gtk.main()
        
    def calendario(self,evt):
        print("Tudo ok")
    def Salas(self,evt):
        
    def voltarSalas(self,evt):
