"""
     Essa é a classe de entrada, para poder utilizar a aplicação
"""


__author__="Jefferson Brito de Oliveira"
from visual.diaAdm import diaAdm
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
class Entrada():

#Metodos da janela de entrada    
    
    def Admin(self,evt):
        self.janEnt.hide()
        self.ad = diaAdm()
        self.ad.diaAdm.show_all()
    
    def ent_style(self):
        css = b"""
        
        .janEnt{
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
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/Ent.glade")
        self.janEnt = builder.get_object("janEnt")
        self.janEnt.connect("destroy",Gtk.main_quit)
        builder.connect_signals(self)
        self.janEnt.show_all()
        self.ent_style()
        Gtk.main()



    

   


