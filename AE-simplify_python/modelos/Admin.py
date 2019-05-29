from Aluno import Aluno
class Admin:
    #atributos privados por serem caracteristicas proprias
    __nome=""
    __cargo=""  
    discente = Aluno() #composicao necessaria para acessar/modificar os atributos da classe Aluno
#encapsulamentos
#getters/acesso
    def getNome(self):
        return self.__nome
    def getCargo(self):
        return self.__cargo
#setters/modificacao
    def setNome(self, nome):
        self.__nome = nome
    def setCargo(self, cargo):
        self.__cargo = cargo
#os atributos de admin serao acessados/modificados no arquivo de execucao

    def __del__(self): #destrutor que sera executado caso haja troca de coordenador
        print("Dados do antigo coodernador apagados. Troca de coordenador do projeto!")
        #mensagem para indicar ao usuario a acao realizada!



