"""    
        classe utilizada para o cadastro do administrador do aplicativo
"""

__author__="Jefferson Brito de Oliveira"
__version__="1.0.1"

from Controle.BotoesAdm import BotoesAdm
from visual.dadosPessoais import dadosPessoais
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
 

class cadAdm:
    def cad_style(self):
        css = b"""
        
        .admDca{
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

    def ca_li(self,evt):
        self.bot = BotoesAdm()
        if self.bot.espacos_em_branco(self.nomAdm.get_text(),self.carAdm.get_text(), self.senAdm.get_text(),self.conAdm.get_text()) == True:
                    self.aviLab.set_text("------Algum campo está em Branco-------")
        elif self.bot.senhas_diferem(self.conAdm.get_text(),self.senAdm.get_text()) == True:
                    self.aviLab.set_text("-------Senhas de confirmação diferente de senha--------")
        else:
            self.bot.mudar(self.nomAdm.get_text(),self.carAdm.get_text())
            self.admDca.hide()
            self.dados = dadosPessoais()

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/cadAdm.glade")
        self.admDca = builder.get_object("admDca")
        self.admDca.connect("destroy",Gtk.main_quit)
        self.butDca = builder.get_object("butDca")
        self.nomAdm = builder.get_object("nomAdm")
        self.carAdm = builder.get_object("carAdm")
        self.senAdm = builder.get_object("senAdm")
        self.conAdm = builder.get_object("conAdm")
        self.aviLab = builder.get_object("aviLab")
        self.cadasAdm = builder.get_object("cadasAdm")
        self.cad_style()
        builder.connect_signals(self)     
        self.admDca.show_all()

        Gtk.main()
    
    def limpar(self,evt):
        self.nomAdm.set_text("")
        self.carAdm.set_text("")
        self.senAdm.set_text("")
        self.conAdm.set_text("")