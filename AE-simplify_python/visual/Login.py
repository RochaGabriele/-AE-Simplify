import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class Login:
    def entrar(self,evt):
        print(self.matLog.get_text())
        print(self.senLog.get_text())
    def __init__(self):
        builder=Gtk.Builder()
        builder.add_from_file("../visual2/log.glade")
        self.janela=builder.get_object("winLog")
        self.matLog=builder.get_object("entMat")
        self.senLog=builder.get_object("entSen")
        builder.connect_signals(self)
        self.janela.show_all()
        Gtk.main()