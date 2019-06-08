"""    

        classe utilizada para a criação do visual do gráfico
"""

__author__="Gabriele rocha Barbosa"
__version__="1.0.1"

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
import numpy as np
import matplotlib.pyplot as plt
class vamo:
    def graph(self,evt):
        self.inst.hide()
        self.win2()
    
    def gtk_style(self):
        css = b"""
        .winIns,.winDesA{
            background-color:#1d771d;
            font-size: 15px;
            font-weight:bold;
            font-family:Times New Roman;
            }    
            
        .butIns{
            background-color:#d1d1d1;
            color:#aaa;
            font-family:Garamond;
            font-weight:bold;
            text-shadow:none;
        }
        .boxBor{
            border-width:2px;  
            border-left-style:double;
            border-left-color:white;
            border-left-style:dashed;
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
        builder.add_from_file("visual/instrucao.glade")
        self.inst = builder.get_object("winIns")
        builder.connect_signals(self)
        self.inst.show_all()
        self.inst.connect("destroy",Gtk.main_quit)
        self.gtk_style()
        Gtk.main()

    def win2(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/desAdm.glade")
        self.desAd = builder.get_object("winDesA")
        self.atraso = builder.get_object("cbtAtr")
        self.assiduo = builder.get_object("cbtAss")
        self.ocorrencia = builder.get_object("cbtOco")
        self.postura = builder.get_object("cbtPos")
        self.desempenho = builder.get_object("cbtDes")
        self.serie = builder.get_object("cbtSer")
        self.mes = builder.get_object("cbtMes")
        builder.connect_signals(self)
        self.desAd.show_all()
        self.desAd.connect("destroy",Gtk.main_quit)
        self.gtk_style()
        
        
    
    prifev = 0.0
    primar = 0.0
    priabr = 0.0
    primai = 0.0
    prijun = 0.0
    priago = 0.0
    priset = 0.0
    priout = 0.0
    prinov = 0.0
    pridez = 0.0
    
    segfev = 0.0
    segmar = 0.0
    segabr = 0.0
    segmai = 0.0
    segjun = 0.0
    segago = 0.0
    segset = 0.0
    segout = 0.0
    segnov = 0.0
    segdez = 0.0
    
    terfev = 0.0
    termar = 0.0
    terabr = 0.0
    termai = 0.0
    terjun = 0.0
    terago = 0.0
    terset = 0.0
    terout = 0.0
    ternov = 0.0
    terdez = 0.0
        
    def pax(self,evt):
        m = int(self.atraso.get_active_text())+int(self.assiduo.get_active_text())+int(self.postura.get_active_text())+int(self.desempenho.get_active_text())+int(self.ocorrencia.get_active_text())
        if self.serie.get_active_text() == '1° Ano': 
            if self.mes.get_active_text() == 'Fevereiro':
                self.prifev = m/5
                return self.prifev
            if self.mes.get_active_text() == 'Março':
                self.primar = m/5
                return self.primar
            if self.mes.get_active_text() == 'Abril':
                self.priabr = m/5
                return self.priabr
            if self.mes.get_active_text() == 'Maio':
                self.primai = m/5
                return self.primai
            if self.mes.get_active_text() == 'Junho':
                self.prijun = m/5
                return self.prijun
            if self.mes.get_active_text() == 'Agosto':
                self.priago = m/5
                return self.priago
            if self.mes.get_active_text() == 'Setembro':
                self.priset = m/5
                return self.priset
            if self.mes.get_active_text() == 'Outubro':
                self.priout = m/5
                return self.priout
            if self.mes.get_active_text() == 'Novembro':
                self.prinov = m/5
                return self.prinov
            if self.mes.get_active_text() == 'Dezembro':
                self.pridez = m/5
                return self.pridez
    
        if self.serie.get_active_text() == '2° Ano':
            if self.mes.get_active_text() == 'Fevereiro':
                self.segfev = m/5
                return self.segfev
            if self.mes.get_active_text() == 'Março':
                self.segmar = m/5
                return self.segmar
            if self.mes.get_active_text() == 'Abril':
                self.segabr = m/5
                return self.segabr
            if self.mes.get_active_text() == 'Maio':
                self.segmai = m/5
                return self.segmai
            if self.mes.get_active_text() == 'Junho':
                self.segjun = m/5
                return self.segjun
            if self.mes.get_active_text() == 'Agosto':
                self.segago = m/5
                return self.segago
            if self.mes.get_active_text() == 'Setembro':
                self.segset = m/5
                return self.segset
            if self.mes.get_active_text() == 'Outubro':
                self.segout = m/5
                return self.segout
            if self.mes.get_active_text() == 'Novembro':
                self.segnov = m/5
                return self.segnov
            if self.mes.get_active_text() == 'Dezembro':
                self.segdez = m/5
                return self.segdez
    
        if self.serie.get_active_text() == '3° Ano':
            if self.mes.get_active_text() == 'Fevereiro':
                self.terfev = m/5
                return self.ter
            if self.mes.get_active_text() == 'Março':
                self.termar = m/5
                return self.termar
            if self.mes.get_active_text() == 'Abril':
                self.terabr= m/5
                return self.terabr
            if self.mes.get_active_text() == 'Maio':
                self.termai = m/5
                return self.termai
            if self.mes.get_active_text() == 'Junho':
                self.terjun = m/5
                return self.terjun
            if self.mes.get_active_text() == 'Agosto':
                self.terago = m/5
                return self.terago
            if self.mes.get_active_text() == 'Setembro':
                self.terset = m/5
                return self.terset
            if self.mes.get_active_text() == 'Outubro':
                self.terout = m/5
                return self.terout
            if self.mes.get_active_text() == 'Novembro':
                self.ternov = m/5
                return self.ternov
            if self.mes.get_active_text() == 'Dezembro':
                self.terdez = m/5
                return self.terdez
            
        self.atraso.set_active(0)
        self.assiduo.set_active(0)
        self.ocorrencia.set_active(0)
        self.postura.set_active(0)
        self.desempenho.set_active(0)
    
    def criar(self,evt):
        self.pax(evt)
        priAno = [self.prifev,self.primar,self.priabr,self.primai,self.prijun,self.priago,self.priset,self.priout,self.prinov,self.pridez]
        segAno = [self.segfev,self.segmar,self.segabr,self.segmai,self.segjun,self.segago,self.segset,self.segout,self.segnov,self.segdez]
        terAno = [self.terfev,self.termar,self.terabr,self.termai,self.terjun,self.terago,self.terset,self.terout,self.ternov,self.terdez]
                
        barWidth=(0.25)
        plt.figure(figsize=(10,5))
        r1 = np.arange(len(priAno))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]
        
        plt.bar(r1, priAno, color ='#6A5ACD', width=barWidth, label="1° ano" )
        plt.bar(r2, segAno, color ='#6495ED', width=barWidth, label="2° ano" )
        plt.bar(r3, terAno, color ='#00BFFF', width=barWidth, label="3° ano" )
        
        plt.xlabel('Meses')
        plt.xticks([r + barWidth for r in range(len(priAno))],['Fevereiro','Março','Abril','Maio','Junho','Agosto','Setembro','Outubro',' Novembro  ','Dezembro'])
        plt.ylabel('Avaliação Média')
        plt.title('Seu Desempenho')
        
        plt.legend()
        plt.show()        

        
        
        
        
        