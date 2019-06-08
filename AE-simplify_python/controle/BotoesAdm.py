"""
    classe de controle para os botoes das classes
"""

__author__="Jefferson brito de Oliveira"
__version__="1.0.0"
from Modelo.Admin import Admin


class BotoesAdm:
    

    def  espacos_em_branco(self,a,b,c,d):
        if a == "":
            return True
        elif b == "":
            return True 
        elif c == "":
            return True
        elif d == "":
            return True
        else:
            return False
    def senhas_diferem(self,c,d):
        if d != c:
            return True
        else:
            return False
    nome = ""
    cargo = ""
    def mudar(self,nom,car):
        self.ad = Admin()

        nome = nom
        cargo = car
        self.ad.setNome(nome)
        self.ad.setCargo(cargo)

    
        
        