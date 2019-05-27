from visual2.Cadastro import Cadastro
from visual2.Login import Login
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
class EntAluno:
    def log(self,evt):
        self.diaAlu.destroy()
        self.diaAlu.hide()
        self.log = Login()
    def cad(self,evt):
        self.diaAlu.destroy()
        self.diaAlu.hide()
        self.ca = Cadastro()

    def alu_style(self):
        css = b"""
          
        .diaAlu{
              
                background-color:#035b03;
                color:#fff;
        }
          
        .labAlu{
            
            font-style:italic;
            font-size:25px;
              font-size:60px;
        }
          
          
        
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("../visual2/diaAlu.glade")
        self.diaAlu = builder.get_object("diaAlu")
        self.alu_style()
        builder.connect_signals(self)
        self.diaAlu.connect("destroy",Gtk.main_quit)
        self.diaAlu.show_all()
        Gtk.main()
        
