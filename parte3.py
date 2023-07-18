import csv

from  parte2 import Vehiculo, Particular, Carga, Bicicleta, Motocicleta
class SistemaVehiculos:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
       # Añadir el vehículo a la lista de vehículos
        self.vehiculos.append(vehiculo)

    def guardar_datos_csv(self, nombre_archivo):
        try:
            # Abrir el fichero en modo escritura
            with open(nombre_archivo, "w", newline="") as archivo:
              # Crear un objeto escritor csv
                archivo_csv = csv.writer(archivo)
                # Iterar a través de los vehículos de la lista
                for vehiculo in self.vehiculos:
                   # Obtener el nombre de la clase del vehículo
                    clase = vehiculo.__class__.__name__
                   # Obtener los atributos del vehículo
                    atributos = str(vehiculo)
                    # Escribe el nombre de la clase y los atributos en el archivo csv
                    archivo_csv.writerow([clase, atributos])
            # Imprime un mensaje para indicar que el archivo se ha guardado correctamente
            print("Datos guardados en el archivo vehiculos.csv.")
        except IOError as e:
          # Imprime un mensaje de error si no se puede guardar el archivo
            print(f"Error al guardar los datos en el archivo: {e}")

#Esta función lee datos de un fichero csv y los almacena en una lista de objetos
def leer_datos_csv(self, nombre_archivo):
        try:
      #Abrir el archivo csv
            with open(nombre_archivo, "r") as archivo:
             #Crear un objeto lector csv
                archivo_csv = csv.reader(archivo)
               #Recorrer cada fila del archivo csv
                for row in archivo_csv:
                   #Guarda la clase del vehículo en una variable
                    clase = row[0]
                        #Guardar los atributos del vehículo en una variable
                    atributos = eval(row[1])
                    #Comprueba la clase del vehículo
                    if clase == "Particular":
                       #Crea un objeto Particular con los atributos almacenados en la variable
                        vehiculo = Particular(**atributos)
                       
                        print("Lista de Vehiculos Particular")
                    elif clase == "Carga":
                        
                        vehiculo = Carga(**atributos)
                        
                        print("Lista de Vehiculos Carga")
                    elif clase == "Bicicleta":
                        #Crea un objeto Bicicleta con los atributos almacenados en la variable
                        vehiculo = Bicicleta(**atributos)
                     
                        print("Lista de Vehiculos Bicicleta")
                    elif clase == "Motocicleta":
                        #Crea un objeto Motocicleta con los atributos almacenados en la variable
                        vehiculo = Motocicleta(**atributos)
                     
                        print("Lista de Vehiculos Motocicleta")
                    else:
                       #Crea un objeto Vehiculo con los atributos almacenados en la variable
                        vehiculo = Vehiculo(**atributos)
                    print(vehiculo)
                       
                    print(vehiculo)
        #Capturar los errores que se produzcan
        except IOError as e:
                #Imprime un mensaje de error si hay un IOError
            print(f"Error al leer los datos del archivo: {e}")
        except Exception as e:
            #Imprimir un mensaje de error si hay una excepción
            print(f"Error inesperado: {e}")


# Crear instancia del sistema de vehículos
sistema_vehiculos = SistemaVehiculos()

# Crear instancias de los vehículos
particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# Agregar los vehículos al sistema
sistema_vehiculos.agregar_vehiculo(particular)
sistema_vehiculos.agregar_vehiculo(carga)
sistema_vehiculos.agregar_vehiculo(bicicleta)
sistema_vehiculos.agregar_vehiculo(motocicleta)

# Guardar los datos en el archivo vehiculos.csv
sistema_vehiculos.guardar_datos_csv("vehiculos.csv")
