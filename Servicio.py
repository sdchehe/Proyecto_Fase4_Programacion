# ============================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Clase Servicio del sistema
# Autor: BLADIMIR ALFONSO ESPAÑA
#
# Funciones principales:
# - Registro de servicios
# - Clasificación de servicios por categoría
# - Gestión de precios
# - Visualización de detalles del servicio
# ============================================================

class Servicio:

    # Constructor de la clase Servicio
    # Inicializa los datos principales del servicio
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    # Método para mostrar el detalle del servicio
    # Retorna nombre, categoría y precio del servicio
    def detalle(self):
        return f"{self.nombre} - {self.categoria} - ${

     
