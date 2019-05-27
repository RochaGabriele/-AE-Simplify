import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
class Cadastro:
    #metodo para confirmação de Senha
    def cadastrar(self,evt):
        if self.senCad.get_text()!= self.senhaCon.get_text():
            print("Senhas diferentes!")
        else:
            print(self.nome.get_text())
            print(self.senCad.get_text())
            print(self.senhaCon.get_text())
            print(self.matCad.get_text())
            print(self.diaNas.get_active_text())
            print(self.mesNas.get_active_text())
            print(self.anoNas.get_active_text())
            print(self.serie.get_active_text())
            print(self.curso.get_active_text())
    #metodo para utilizacao de estilos css
    def cad_style(self):
        css = b"""
            
            .winCad{
                
                background-color:#035b03;
                color:#fff;
            }    
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
    
    #construtor para criar a janela
    def __init__(self):
        builder=Gtk.Builder()
        builder.add_from_file("../visual2/cadas.glade")
        self.janela=builder.get_object("winCad")
        self.nome=builder.get_object("entNom")
        self.matCad=builder.get_object("entMat")
        self.senCad=builder.get_object("pasSenh")
        self.senhaCon=builder.get_object("pasCon")
        self.diaNas=builder.get_object("cbtDia")
        self.mesNas=builder.get_object("cbtMes")
        self.anoNas=builder.get_object("cbtAno")
        self.serie=builder.get_object("cbtSer")
        self.curso=builder.get_object("cbtCur")
        self.cad_style()
        builder.connect_signals(self)
        self.janela.show_all()
        Gtk.main()
