"""
    Classe feita para o controle  da modelo Agenda, e a visual MAgenda
"""
__author__="José Maik Freitas dos Santos"
__version__="1.0.0"

from Modelo.Agenda import Agenda
class AgendaControle:
    def salas(self,a,b,c,d,e,f,g,h,i):
        self.c = Agenda()
        self.c.setSala1(a)
        self.c.setSala2(b)
        self.c.setSala3(c)
        self.c.setSala4(d)
        self.c.setSala5(e)
        self.c.setSala6(f)
        self.c.setSala7(g)
        self.c.setSala8(h)
        self.c.setSala9(i)
        print(self.c.getSala1())
        print(self.c.getSala2())
        print(self.c.getSala3())
        print(self.c.getSala4())
        print(self.c.getSala5())
        print(self.c.getSala6())
        print(self.c.getSala7())
        print(self.c.getSala8())
        print(self.c.getSala9())
