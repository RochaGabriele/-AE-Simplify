from visual.miniAluno import miniAluno

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Inicio:
    def alu(self,evt):
        self.alu=miniAluno()
        self.Gtk.destroy()
    
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("entrada.glade")
        self.janela = builder.get_object("winEnt")
        self.labels= builder.get_object("BoxLab")
        self.labLog= builder.get_object("labLog")
        self.labCnc= builder.get_object("labCnc")
        self.butoes = builder.get_object("GriBut")
        builder.connect_signals(self)
        self.janela.show_all()
        Gtk.main()     
         

minia=Inicio()
        