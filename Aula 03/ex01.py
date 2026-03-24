# implementar classes em python para representar um círculo
# A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área e sua circunferência.
# criar um programa que teste a classe.
class circulo:
    def __init__(self):
        self.raio = 0
        self.pi = 3.14

    def calculaArea(self):
        return self.raio**2 * self.pi
    
    def calculaCircunferencia(self):
        return self.raio * self.pi * 2

        
x = circulo()

x.raio = 5 
print(x.calculaArea())
print(x.calculaCircunferencia())
