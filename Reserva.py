from registros import Registros

class Reserva:

    def __init__(self, cliente, servicio, horas):

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):

        try:

            if self.horas <= 0:
                raise ValueError("Las horas deben ser mayores a 0")

            self.estado = "Confirmada"

            Registros.guardar(
                f"Reserva confirmada para {self.cliente}"
            )

        except Exception as e:

            Registros.guardar(f"ERROR EN RESERVA: {e}")

    def cancelar(self):

        self.estado = "Cancelada"

        Registros.guardar(
            f"Reserva cancelada para {self.cliente}"
        )

    def mostrar(self):

        return (
            f"Cliente: {self.cliente} | "
            f"Servicio: {self.servicio} | "
            f"Horas: {self.horas} | "
            f"Estado: {self.estado}"
        )
