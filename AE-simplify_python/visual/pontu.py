import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
class pontu:
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
        
    def calc(self,evt):
        c = int(self.atraso.get_active_text())+int(self.assiduo.get_active_text())+int(self.ocorrencia.get_active_text())+int(self.postura.get_active_text())+int(self.desempenho.get_active_text())
        if c < 35:
            self.media.hide()
            self.window4()
        else:
            self.media.hide()
            self.window5()
    
    def inicialA(self,evt):
        self.apro.hide()
        #linkar p pagina inicial(maik) self.window()
    
    def inicialR(self,evt):
        self.repro.hide()
        #linkar p pagina inicial(maiks) self.window4()
    
    def calNovA(self,evt):
        self.apro.hide()
        self.window6()
    
    def calNovR(self,evt):
        self.repro.hide()
        self.window3()
    
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/novatos/NovUm.glade")
        self.NovUm = builder.get_object("winEnt")   
        #self.gtk_style()
        builder.connect_signals(self)
        self.NovUm.show_all()
        self.NovUm.connect("destroy",Gtk.main_quit)
        Gtk.main()

    def window2(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/novatos/NovDoi.glade")
        self.NovDoi = builder.get_object("winCom")       
        builder.connect_signals(self)
        self.gtk_style()
        self.NovDoi.show_all()
        self.NovDoi.connect("destroy",Gtk.main_quit)
        Gtk.main()
        
    def window3(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/novatos/NovTre.glade")
        self.NovTre = builder.get_object("winRec")       
        builder.connect_signals(self)
        self.gtk_style()
        self.NovTre.show_all()
        self.NovTre.connect("destroy",Gtk.main_quit)
        Gtk.main()
        
    def window4(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/novatos/repro.glade")
        self.repro = builder.get_object("winRep")       
        builder.connect_signals(self)
        self.gtk_style()
        self.repro.show_all()
        self.repro.connect("destroy",Gtk.main_quit)
        Gtk.main()
            
    def window5(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/novatos/apro.glade")
        self.apro = builder.get_object("winApr")       
        builder.connect_signals(self)
        self.gtk_style()
        self.apro.show_all()
        self.apro.connect("destroy",Gtk.main_quit)
        Gtk.main()
    
    def window6(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/novatos/media.glade")
        self.media = builder.get_object("winPon")  
        self.atraso = builder.get_object("cbtAtr")
        self.assiduo = builder.get_object("cbtAss")
        self.ocorrencia = builder.get_object("cbtOco")
        self.postura = builder.get_object("cbtPos")
        self.desempenho = builder.get_object("cbtDes")     
        builder.connect_signals(self)
        self.gtk_style()
        self.media.show_all()
        self.media.connect("destroy",Gtk.main_quit)
        Gtk.main()
    