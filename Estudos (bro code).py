#Polimorfismo (varias formas ou faces)
#Como alcançar o polimorfismo 1. Herança:Um objeto pode ser tratado como o mesmo tipo de uma classe parente
#2: "Duck typing", Objeto deve ter os metodos/atributos necessarios

#Herança:
from abc import  ABC,abstractmethod

class Forma:
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio=raio

    def area(self):
        return 3.14 * self.raio ** 2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado=lado

    def area(self):
        return self.lado**2

class Triangulo(Forma):
    def __init__(self, altura, base):
        self.altura=altura
        self.base=base

    def area(self):
        return (self.base * self.altura)/2


formas=[Circulo(4), Quadrado(6), Triangulo(3,2)]

for forma in formas:
    print(f"{forma.area()}m²")





#circulo=Circulo()
#um circulo (objeto) pode ser considerado um circulo (classe), mas também como uma forma, por herança