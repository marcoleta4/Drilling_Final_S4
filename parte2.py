class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad=None, cilindrada=None):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
     # Method to print the class instance
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc"


class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puestos = num_puestos
     
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc, Puestos: {self.num_puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc, Carga: {self.peso_carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)


print(particular)

print(carga)

print(bicicleta)

print(motocicleta)

#Imprime el resultado de comprobar la relación entre la instancia de la clase Motocicleta y las siguientes clases
print("\nVerificar la relación que existe de la instancia motocicleta con:\n")
#Imprimir el resultado de comprobar la relación entre la instancia de la clase Particular y la clase Vehículo
print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
#Imprimir el resultado de comprobar la relación entre la instancia de la clase Particular y la clase Automóvil
print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
#Imprime el resultado de comprobar la relación entre la instancia de la clase Particular y la clase Particular
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
 #Imprime el resultado de comprobar la relación entre la instancia de la clase Particular y la clase Carga
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
#Imprime el resultado de comprobar la relación entre la instancia de la clase Particular y la clase Bicicleta
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
#Imprimir el resultado de comprobar la relación entre la instancia de la clase Particular y la clase Motocicleta
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))