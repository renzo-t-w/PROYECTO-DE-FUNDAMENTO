import csv
from datetime import datetime

class Evento:
    """Clase que representa un evento con detalles como nombre, fecha, hora y categoría."""

    def __init__(self, nombre, fecha, hora):  # constructor con parámetros
        self.nombre = nombre  # atributos
        self.fecha = fecha
        self.hora = hora

    def __str__(self):  # cadena de texto
        return (f"{self.nombre} - {self.fecha} {self.hora}")

# Clase que gestiona los eventos
class GestorEventos:
    def __init__(self):
        self.eventos = []  # lista vacía

    # Método
    def agregar_evento(self, evento):
        self.eventos.append(evento)  # el append agrega el evento al final de la lista
        print("Evento agregado exitosamente.\n")

    # Buscar eventos por fecha
    def buscar_eventos_por_fecha(self, fecha):
        # creamos una instancia para filtrar los eventos
        eventos_en_fecha = [evento for evento in self.eventos if evento.fecha == fecha]
        return eventos_en_fecha

    # Listar todos los eventos ordenados por fecha
    def listar_eventos(self):
        for evento in sorted(self.eventos, key=lambda e: e.fecha):  # sorted devuelve una lista ordenada
            print(evento)

    # Modificar un evento
    def modificar_evento(self, nombre_evento, nuevos_datos):
        for evento in self.eventos:  # bucle que nos recorre cada objeto de la lista
            if evento.nombre == nombre_evento:
                evento.__dict__.update(nuevos_datos)
                print("Evento modificado exitosamente.\n")
                return
        print("Evento no encontrado.\n")

    # Eliminar un evento
    def eliminar_evento(self, nombre_evento):
        self.eventos = [evento for evento in self.eventos if evento.nombre != nombre_evento]
        print("Evento eliminado exitosamente.\n")

    # Guardar eventos en un archivo CSV
    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "fecha", "hora"])
            writer.writeheader()
            for evento in self.eventos:
                writer.writerow(evento.__dict__)
        print("Eventos guardados en archivo CSV.\n")

    # Cargar eventos desde un archivo CSV
    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                reader = csv.DictReader(f)
                self.eventos = [Evento(**row) for row in reader]
            print("Eventos cargados desde archivo CSV.\n")
        except FileNotFoundError:
            print("Archivo no encontrado.\n")

# Función principal (interfaz básica)
def main():
    gestor = GestorEventos()
    gestor.cargar_desde_archivo("eventos.csv")

    while True:
        print("\n--- Gestor de Eventos ---")
        print("1. Agregar eventos")
        print("2. Buscar eventos")
        print("3. Mostrar eventos")
        print("4. Modificar eventos")
        print("5. Eliminar eventos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del evento: ")
            fecha = input("Fecha (DD-MM-YYYY): ")
            hora = input("Hora (HH:MM): ")

            evento = Evento(nombre, fecha, hora)
            gestor.agregar_evento(evento)

        elif opcion == "2":
            fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
            eventos = gestor.buscar_eventos_por_fecha(fecha)
            if eventos:
                for e in eventos:
                    print(e)
            else:
                print("No hay eventos en esa fecha.")

        elif opcion == "3":
            gestor.listar_eventos()

        elif opcion == "4":
            nombre = input("Nombre del evento a modificar: ")
            print("Ingrese los nuevos datos (deje vacío para mantener el actual):")
            nuevos_datos = {
                "nombre": input("Nuevo nombre: ") or None,
                "fecha": input("Nueva fecha (DD-MM-YYYY): ") or None,
                "hora": input("Nueva hora (HH:MM): ") or None,
            }
            nuevos_datos = {k: v for k, v in nuevos_datos.items() if v is not None}
            gestor.modificar_evento(nombre, nuevos_datos)

        elif opcion == "5":
            nombre = input("Nombre del evento a eliminar: ")
            gestor.eliminar_evento(nombre)

        elif opcion == "6":
            gestor.guardar_en_archivo("eventos.csv")
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
