# ============================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Clase Cliente del sistema
# Autora: SANDY DEL CARMEN HERRERA HERRERA
#
# Funciones principales:
# - Registro de clientes
# - Almacenamiento de datos personales
# - Visualización de información del cliente
# - Gestión básica de clientes
# ============================================================

class Cliente:

    # Constructor de la clase Cliente
    # Inicializa los atributos principales del cliente
    def __init__(self, nombre, documento, telefono):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono

    # Método para mostrar la información del cliente
    # Retorna nombre y documento en formato texto
    def mostrar(self):
        return f"{self.nombre} | CC: {self.documento}"

