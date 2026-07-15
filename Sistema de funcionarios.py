
class Funcionario:
    def __init__(self, nome, salario):
        self.nome=nome
        self.salario= salario
    def info_func(self):
        return (f"Funcionario: {self.nome} \n"
                f"Salário: {self.salario:.2f} \n")
class Cargo(Funcionario):
    def __init__(self,nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento=departamento

    def info_func(self):
        dados= super().info_func()
        return dados+ (f"Departamento: {self.departamento}\n"
                       f"--------------------------")

fun1= Cargo(nome="Josemar", salario=1300.121, departamento="TI")
fun2= Cargo("Claudio", 3400, "Logistica")
print(fun1.info_func())
print(fun2.info_func())