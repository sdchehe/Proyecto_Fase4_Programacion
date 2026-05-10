# ==========================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Clase abstracta Servicio
# Autor: Bladimir Alfonso España
#
# Funciones principales:
# - Representar servicios generales del sistema
# - Definir atributos básicos de servicios
# - Implementar herencia y abstracción
# - Obligar a las clases hijas a definir métodos
# - Calcular costos y describir servicios
# ==========================================================

from abc import ABC, abstractmethod
from modelos.entidad import Entidad


class Servicio(Entidad, ABC):

    # Constructor de la clase Servicio
    def __init__(self, nombre, tarifa):

        self.nombre = nombre
        self.tarifa = tarifa

    # Método abstracto para calcular costos
    @abstractmethod
    def calcular_costo(self, horas):
        pass

    # Método abstracto para mostrar descripción
    @abstractmethod
    def descripcion(self):
        pass
from abc import ABC, abstractmethod
from modelos.entidad import Entidad

class Servicio(Entidad, ABC):

    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass
