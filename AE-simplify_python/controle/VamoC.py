"""    
        metodo de controle para o funcionamento da classe vamo, importante para a criação
        do gráfico
"""

__author__="Gabriele rocha Barbosa"
__version__="1.0.1"


import numpy as np
import matplotlib.pyplot as plt
class VamoC:
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
        
    def pax(self,f,g,h,i,j,k,l):
        m = int(f)+int(g)+int(h)+int(i)+int(j)
        if k == '1° Ano':
            if l == 'Fevereiro':
                self.prifev = m/5
                return self.prifev
            if l == 'Março':
                self.primar = m/5
                return self.primar
            if l == 'Abril':
                self.priabr = m/5
                return self.priabr
            if l == 'Maio':
                self.primai = m/5
                return self.primai
            if l == 'Junho':
                self.prijun = m/5
                return self.prijun
            if l == 'Agosto':
                self.priago = m/5
                return self.priago
            if l == 'Setembro':
                self.priset = m/5
                return self.priset
            if l == 'Outubro':
                self.priout = m/5
                return self.priout
            if l == 'Novembro':
                self.prinov = m/5
                return self.prinov
            if l == 'Dezembro':
                self.pridez = m/5
                return self.pridez
    
        if k == '2° Ano':
            if l == 'Fevereiro':
                self.segfev = m/5
                return self.segfev
            if l == 'Março':
                self.segmar = m/5
                return self.segmar
            if l == 'Abril':
                self.segabr = m/5
                return self.segabr
            if l == 'Maio':
                self.segmai = m/5
                return self.segmai
            if l == 'Junho':
                self.segjun = m/5
                return self.segjun
            if l == 'Agosto':
                self.segago = m/5
                return self.segago
            if l == 'Setembro':
                self.segset = m/5
                return self.segset
            if l == 'Outubro':
                self.segout = m/5
                return self.segout
            if l == 'Novembro':
                self.segnov = m/5
                return self.segnov
            if l == 'Dezembro':
                self.segdez = m/5
                return self.segdez
    
        if k == '3° Ano':
            if l == 'Fevereiro':
                self.terfev = m/5
                return self.ter
            if l == 'Março':
                self.termar = m/5
                return self.termar
            if l == 'Abril':
                self.terabr= m/5
                return self.terabr
            if l == 'Maio':
                self.termai = m/5
                return self.termai
            if l == 'Junho':
                self.terjun = m/5
                return self.terjun
            if l == 'Agosto':
                self.terago = m/5
                return self.terago
            if l == 'Setembro':
                self.terset = m/5
                return self.terset
            if l == 'Outubro':
                self.terout = m/5
                return self.terout
            if l == 'Novembro':
                self.ternov = m/5
                return self.ternov
            if l == 'Dezembro':
                self.terdez = m/5
                return self.terdez
        
        f.set_active(0)
        g.set_active(0)
        h.set_active(0)
        i.set_active(0)
        j.set_active(0)
            
    def criar(self,z):  
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
