
"""

        classe usada para criar o visual pontuação do aluno, e ver se pode ou não participar do projeto
"""
__author__="Gabriele rocha Barbosa"
__version__="1.0.1"

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
from Controle.pontuC import pontuC
class pontu:
    def gtk_style(self):
        css = b"""
        .winApr,.winPon,.winCom,.winRec,.winEnt,.winRep{
            background-color:#1d771d;    
            font-size: 15px;
            font-weight: bold;
            font-family: Times New Roman;
            text-shadow: 1px 1px 3px black;
            }    
        
        .butA{
            background-color:#d1d1d1;
            color:#0d0d0d;
            font-family:Garamond;
            font-weight:bold;
            text-shadow:none;
        }
        .boxBor{
            border-width:5px;  
            border-right-style:double;
            border-right-color:white;
        }
        
        """
 
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
    def entendi(self,evt):
        self.NovUm.hide()
        self.window2()
        
    def comecar(self,evt):
        self.NovDoi.hide()
        self.window3()
        
    def naodeu(self,evt):
        self.NovTre.hide()
        self.window4()
        
    def prox(self,evt):
        self.NovTre.hide()
        self.window6()
        
    '''
    def inicialA(self,evt):
        self.apro.hide()
        #linkar p pagina inicial(maik) self.window()
    
    def inicialR(self,evt):
        self.repro.hide()
        #linkar p pagina inicial(maik) self.window4()
    
    '''
    def calNovA(self,evt):
        self.apro.hide()
        self.window3()
    
    def calNovR(self,evt):
        self.repro.hide()
        self.window3()
    
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/NovUm.glade")
        self.NovUm = builder.get_object("winEnt")   
        ##self.gtk_style()
        builder.connect_signals(self)
        self.NovUm.show_all()
        self.gtk_style()
        self.NovUm.connect("destroy", Gtk.main_quit)
        Gtk.main()

    def window2(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/NovDoi.glade")
        self.NovDoi = builder.get_object("winCom")       
        builder.connect_signals(self)
        ##self.gtk_style()
        self.NovDoi.show_all()
        self.gtk_style()
        
    def window3(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/NovTre.glade")
        self.NovTre = builder.get_object("winRec")       
        builder.connect_signals(self)
        ##self.gtk_style()
        self.NovTre.show_all()
        self.gtk_style()
        
    def window4(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/repro.glade")
        self.repro = builder.get_object("winRep")       
        builder.connect_signals(self)
        ##self.gtk_style()
        self.repro.show_all()
        self.gtk_style()
            
    def window5(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/apro.glade")
        self.apro = builder.get_object("winApr")       
        builder.connect_signals(self)
        #self.gtk_style()
        self.apro.show_all()
        self.gtk_style()
    
    def window6(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/media.glade")
        self.media = builder.get_object("winPon")  
        self.atraso = builder.get_object("cbtAtr")
        self.assiduo = builder.get_object("cbtAss")
        self.ocorrencia = builder.get_object("cbtOco")
        self.postura = builder.get_object("cbtPos")
        self.desempenho = builder.get_object("cbtDes")     
        builder.connect_signals(self)
        self.media.show_all()
        self.gtk_style()
        
    def mostra(self,evt):
        self.ok = pontuC()
        m = self.ok.calc(self.atraso.get_active_text(),self.assiduo.get_active_text(),self.ocorrencia.get_active_text(),self.postura.get_active_text(),self.desempenho.get_active_text())
        if m < 35:
            self.media.hide()
            self.window4()
        else:
            self.media.hide()
            self.window5()
        