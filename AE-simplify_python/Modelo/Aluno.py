class Aluno:
    # atributos privados por serem caracteristias proprias
    __atraso = 0
    __assiduo = 0
    __ocorrencia = 0
    __postura = 0
    __desempenho = 0
    __matricula = 0
    __dataNasc = "" #string para pessoa poder digitar barras. Ex.: 10 / 11 / 2003
    __nome  = ""
    
    #encapsulamentos 
    #getters/acesso
    def getAtraso(self):
        return self.__atraso
    def getAssiduo(self):
        return self.__assiduo
    def getOcorrencia(self):
        return self.__ocorrencia
    def getPostura(self):
        return self.__postura
    def getDesempenho(self):
        return self.__desempenho
    def getMatricula(self):
        return self.__matricula
    def getDataNasc(self):
        return self.__dataNasc
    def getNome(self):
        return self.__nome
    #setters/modificacao
    def setAtraso(self, atraso):
        self.__atraso = atraso
    def setAssiduo(self, assiduo):
        self.__assiduo = assiduo
    def setOcorrencia(self, ocorrencia):
        self.__ocorrencia = ocorrencia
    def setPostura(self,  postura):
        self.__postura = postura
    def setDesempenho(self, desempenho):
        self.__desempenho = desempenho
    def setMatricula(self, matricula):
        self.__matricula = matricula
    def setDataNasc(self, dataNasc):
        self.__dataNasc = dataNasc
    def setNome(self, nome):
        self.__nome = nome
