#metodo-estatico= melhor para funções que não precisam de acesso a data de classes
#metodos de instancias= melhor para operações que utilizam classes (objetos)
"""
class Trabalhador:
    def __init__(self, nome, cargo):
        self.nome=nome
        self.cargo=cargo

    def get_info(self):
        return (f"{self.nome}= {self.cargo}") #metodo de instancia, pois precisa de uma classe superior para pegar as informações

    @staticmethod
    def is_cargo_valido(cargo_1):#metodos estaticos não utilizam o "self"

        cargo_validos= ["Supervisor","Auxiliar", "Zelador", "Chapeiro"]
        return cargo_1 in cargo_validos

clt1= Trabalhador("Leoncio", "Supervisor")
clt2= Trabalhador("Zeca", "Chapeiro")
clt3= Trabalhador("Pica-Pau", "Auxiliar")
clt4= Trabalhador("Mandy", "Zelador")


print(clt1.get_info())
print(clt2.get_info())
print(clt3.get_info())
print(clt4.get_info())
"""

#Metodos de Classe= Permite operações relacionadas a propria classe/
#Pega (cls) como 1 parametro

class Estudante:
    num_alunos=0
    media_idade= 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade=idade
        Estudante.num_alunos+=1
        Estudante.media_idade+=idade
    @classmethod
    def get_num(cls):
        return f"Total de alunos é de: {cls.num_alunos}"

    @classmethod #cls consegue manipular variaveis pre definidas dentro da Classe
    def get_idade(cls):
        if cls.media_idade==0:
            return 0
        else:
            return f"A media de idade dos alunos é de: {cls.media_idade/ cls.num_alunos:.1f}"

aluno1= Estudante("Carlos", 20)
aluno2= Estudante("Arthur", 10)
print(Estudante.get_num())
print(Estudante.get_idade())