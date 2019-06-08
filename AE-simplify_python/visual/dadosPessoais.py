"""
    Classe usada para mostrar os dados do usuário
"""
__author__="Jefferson Brito de Oliveira"
__version__="1.0.1"

from visual.Desempenho import Desempenho
from Controle.BotoesAdm import BotoesAdm
from visual.MAgenda import MAgenda
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk


class dadosPessoais:
    def cad_style(self):
        css = b"""
        
        .winDad{
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
    def butDes(self,evt):
        self.des = Desempenho()
    def butAgenda(self,evt):
       
        self.age = MAgenda()
    
    def __init__(self):
        builder = Gtk.Builder()   
        builder.add_from_file("visual/dadosPessoais.glade")
        self.winDad = builder.get_object("winDad")
        self.nomEnt = builder.get_object("nomEnt")
        self.carEnt = builder.get_object("carEnt")
        self.winDad.connect("destroy",Gtk.main_quit)
        builder.connect_signals(self)
        self.cad_style()
        self.winDad.show_all()
        self.bot = BotoesAdm()
        Gtk.main()
    

    
