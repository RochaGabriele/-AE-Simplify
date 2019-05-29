import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class EntAdm:
    
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/diaAdm.glade")
        self.diaAlu = builder.get_object("DiaAdm")
        builder.connect_signals(self)
        self.diaAlu.show_all()
        Gtk.main()
