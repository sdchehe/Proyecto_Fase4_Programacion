# ==========================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Archivo de gestión de reservas
# Autor: Bladimir Alfonso Espana
#
# Funciones principales:
# - Crear reservas de clientes
# - Confirmar reservas
# - Cancelar reservas
# - Mostrar información de reservas
# - Registrar eventos y errores del sistema
# ==========================================================

from registros import Registros


class Reserva:

    # Constructor de la clase Reserva
    def __init__(self, cliente, servicio, horas):

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    # Método para confirmar la reserva
    def confirmar(self):

        try:

            # Validar que las horas sean mayores a 0
            if self.horas <= 0:
                raise ValueError("Las horas deben ser mayores a 0")

            # Cambiar estado de la reserva
            self.estado = "Confirmada"

            # Registrar confirmación en logs
            Registros.guardar(
                f"Reserva confirmada para {self.cliente}"
            )

        except Exception as e:

            # Registrar errores encontrados
            Registros.guardar(f"ERROR EN RESERVA: {e}")

    # Método para cancelar la reserva
    def cancelar(self):

        self.estado = "Cancelada"

        # Registrar cancelación en logs
        Registros.guardar(
            f"Reserva cancelada para {self.cliente}"
        )

    # Método para mostrar información de la reserva
    def mostrar(self):

        return (
            f"Cliente: {self.cliente} | "
            f"Servicio: {self.servicio} | "
            f"Horas: {self.horas} | "
            f"Estado: {self.estado}"
        )
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
