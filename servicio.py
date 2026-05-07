from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass


class ReservaSala(Servicio):

    def __init__(self):
        super().__init__("Reserva de Sala", 50000)

    def calcular_costo(self, horas=1):
        return self.precio * horas


class AlquilerEquipo(Servicio):

    def __init__(self):
        super().__init__("Alquiler de Equipo", 30000)

    def calcular_costo(self, dias=1):
        return self.precio * dias


class AsesoriaEspecializada(Servicio):

    def __init__(self):
        super().__init__("Asesoría Especializada", 80000)

    def calcular_costo(self, sesiones=1):
        return self.precio * sesiones