"""
        classe que direciona para duas escolhas , uma criar um grafico do aluno desejado
     ou fazer uma soma de notas
     e saber se o aluno pode passar ou não no projeto
"""
__author__="Jefferson Brito de Oliveira"
__version__="1.0.1"

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
from visual.pontu import pontu
from visual.vamo import vamo
class Desempenho:
    def des_style(self):
        css = b"""
        
        .desJan{
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

    
    def pontu(self,evt):
        self.desJan.hide()
        self.poo = pontu()
    def grafic(self,evt):
        self.desJan.hide()
        self.va = vamo()
   
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/dadosPessoais.glade")
        self.desJan = builder.get_object("desJan")
        builder.connect_signals(self)
        self.desJan.connect("destroy",Gtk.main_quit)
        self.des_style()
        self.desJan.show_all()
        Gtk.main()
        