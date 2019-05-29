class Agenda:
    __dia=0
    __mes= 0
    __ano=0

#getters/acesso
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getAno(self):
        return self.__ano

#setters/modificacao

    def setDia(self,dia):
        self.__dia=dia
    def setMes(self,mes):
        self.__mes=mes
    def setAno(self,ano):
        self.__ano=ano

