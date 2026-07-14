#metodo-estatico= melhor para funções que não precisam de acesso a data de classes
#metodos de instancias= melhor para operações que utilizam classes (objetos)

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

print(clt4.get_info())

