class Robot:
    def __init__(self, nombre, tipo, nivel_bateria=100):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel_bateria = nivel_bateria
        self.estado = "inactivo"

    def mostrar_estado(self):
        print(f"--- Información del Robot: {self.nombre} ---")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel de Batería: {self.nivel_bateria}%")
        print(f"Estado: {self.estado}")
        print("-" * 30)

    def moverse(self, distancia):
        if self.nivel_bateria >= 10:
            print(f"{self.nombre} se está moviendo {distancia} metros.")
            self.nivel_bateria -= distancia // 5
            if self.nivel_bateria < 0:
                self.nivel_bateria = 0
            self.estado = "en movimiento"
            print(f"Nivel de batería actual: {self.nivel_bateria}%")
        else:
            print(f"{self.nombre} tiene poca batería ({self.nivel_bateria}%). No puede moverse.")
            self.estado = "batería baja"

    def recargar_bateria(self):
        print(f"{self.nombre} está recargando su batería...")
        self.nivel_bateria = 100
        self.estado = "cargando"
        print(f"Batería de {self.nombre} recargada al 100%.")

print("--- Demostración del Robot ---")

mi_robot = Robot("Wall-E", "limpieza")
mi_robot.mostrar_estado()
mi_robot.moverse(30)
mi_robot.moverse(80)
mi_robot.recargar_bateria()
mi_robot.moverse(60)