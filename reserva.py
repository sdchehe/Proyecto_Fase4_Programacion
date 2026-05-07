class Reserva:

    def __init__(self, cliente, servicio, tiempo):

        if tiempo <= 0:
            raise ValueError("El tiempo debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def mostrar_reserva(self):

        costo = self.servicio.calcular_costo(self.tiempo)

        print("----- RESERVA -----")
        self.cliente.mostrar_datos()
        print(f"Servicio: {self.servicio.nombre}")
        print(f"Tiempo: {self.tiempo}")
        print(f"Costo: {costo}")
        print(f"Estado: {self.estado}")