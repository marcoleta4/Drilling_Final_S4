class Vehicule: 
        def __init__(self, marca, modelo, nro_ruedas):
                self.marca = marca 
                self.modelo = modelo
                self.nro_ruedas =nro_ruedas


class Automovil(Vehicule):
        def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
                super().__init__(marca, modelo, nro_ruedas)
                self.velocidad = velocidad
                self.cililndrada = cilindrada

class particulares (Automovil):
        def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, numero_puestos):
                super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada, numero_puestos)
                self.numero_puestos = numero_puestos


class carga (Automovil):
        def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
                super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
                self.carga = carga

class motocicleta (Vehicule):
        def __init__(self, marca, modelo, nro_ruedas, tipo, motor, numero_radios, cuadro):
                super().__init__(marca, modelo, nro_ruedas) 
                self.tipo = tipo 
                self.motor = motor
                self.numero_radios = numero_radios
                self.cuadro = cuadro

class bicicleta(Vehicule):
        def __init__(self, marca, modelo, nro_ruedas, tipos):
                super().__init__(marca, modelo, nro_ruedas)
                self.tipos = tipos





        


                
            