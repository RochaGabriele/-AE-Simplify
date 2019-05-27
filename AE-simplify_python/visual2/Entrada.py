from visual2.EntAluno import EntAluno
from visual2.EntAdm import EntAdm


import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
class Entrada:
    def Alu(self,evt):
        self.janela.destroy()
        self.janela.hide()
        self.alu = EntAluno()
    def Adm(self,evt):
        self.janela.hide()
        self.adm = EntAdm()
        
    def gtk_style(self):
        css = b"""
        .janela{
                background-color:#035b03;
                color:#fff;
            }
            
        .label1{
                font-size:60px;
                color:#fff;
                font-style:italic;
        }
        
        .butAluno{
                
                border-radius:300px;
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
        builder.add_from_file("../visual2/Ent.glade")
        self.gtk_style()
        self.janela = builder.get_object("janEnt")
        builder.connect_signals(self)
        self.janela.connect("destroy",Gtk.main_quit)
        self.janela.show_all()
        
        Gtk.main()
    
