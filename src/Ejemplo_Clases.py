class Carro:
    max_speed = 120  
    def __init__(self, make, modelo, color, velocidad=0):
        self.make = make
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad 
    
    def accelerate(self, acceleracion):
        if self.velocidad + acceleracion <= Carro.max_speed:
            self.velocidad += acceleracion
        else:
            self.velocidad = Carro.max_speed
    def get_velocidad(self):
        return self.velocidad


car1 = Carro("Mazda", "Mazda 3", "Azul")
car2 = Carro("Mitusbishi", "Lancer", "Rojo")


car1.accelerate(180)
car2.accelerate(190)    


print(f"{car1.make} {car1.modelo} Velocidad maxima es de  {car1.get_velocidad()} km/h. es {car1.color}")
print(f"{car2.make} {car2.modelo} Velocidad maxima es de {car2.get_velocidad()} km/h. es {car2.color}")

