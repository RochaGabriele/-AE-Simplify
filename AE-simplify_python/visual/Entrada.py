from visual.EntAdm import EntAdm
from visual.Cadastro import Cadastro
from visual.Login import Login
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
class Entrada:
#metodos da primeira janela
    def Alu(self,evt):
        self.janela.hide()
        self.janela2()
    def Adm(self,evt):
        self.janela.hide()
        self.janela3()
        
  
#metodos da segunda janela
    def log(self,evt):
        self.diaAlu.destroy()
        self.diaAlu.hide()
        self.log = Login()
    def cad(self,evt):
        self.diaAlu.destroy()
        self.diaAlu.hide()
        self.ca = Cadastro()  
    def voltar(self,evt):
        self.diaAlu.hide()
        self.janela.show_all()
    def voltarAd(self,evt):
        self.diaAdm.hide()
        self.janela.show_all()
        
#css das janelas        
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
        .diaAlu{
              
                background-color:#035b03;
                color:#fff;
        }
          
        .labAlu{
            
            font-style:italic;
            font-size:25px;
              font-size:60px;
        }
        .DiaAdm{
                background-color:#035b03;
            }
        .labAdm{
                color:#fff;
                font-size:40px;
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
        builder.add_from_file("../visual/Ent.glade")
        self.janela = builder.get_object("janEnt")
        self.janela.connect("destroy",Gtk.main_quit)   
        self.janela.show_all()
        builder.connect_signals(self)
        self.gtk_style()
        Gtk.main()
    def janela2(self):
        builder = Gtk.Builder()
        builder.add_from_file("../visual/diaAlu.glade")
        self.diaAlu = builder.get_object("diaAlu")
        self.diaAlu.connect("destroy",Gtk.main_quit)
        self.gtk_style()
        builder.connect_signals(self)
        self.diaAlu.show_all()
        Gtk.main()

    def janela3(self):
            builder = Gtk.Builder()
            builder.add_from_file("../visual/diaAdm.glade")
            self.diaAdm = builder.get_object("DiaAdm")
            self.diaAlu.connect("destroy",Gtk.main_quit)
            builder.connect_signals(self)
            self.diaAdm.show_all()
            self.gtk_style()
            Gtk.main()

        
    
