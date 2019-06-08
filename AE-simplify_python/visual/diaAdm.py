"""

        uma diálog usada para  entrar em cadastro

"""

__author__="Jefferson Brito de Oliveira"
__version__="1.0.1"
from visual.cadAdm import cadAdm



import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk



class diaAdm:
    def diaAd_style(self):
        css = b"""
        
        .DiaAdm{
            background-color:#1d771d;
            font-weight:bold;
            font-family:Times New Roman;
        }
        .labelAdm{
            font-size:45px;
        }
        
        
        
        
        
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
    def cadAd(self,evt):
        self.diaAdm.hide()
        self.caa = cadAdm()
        self.caa.admDca.show_all()
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/diaAdm.glade")
        self.diaAdm = builder.get_object("DiaAdm")
        self.diaAdm.connect("destroy",Gtk.main_quit)
        builder.connect_signals(self)
        self.diaAd_style()
        self.diaAdm.show_all()
        Gtk.main()