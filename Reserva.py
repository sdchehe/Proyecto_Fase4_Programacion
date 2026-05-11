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
class Reserva:

    # Constructor de la clase
    def __init__(self, cliente, servicio):

        # Guardar cliente
        self.cliente = cliente

        # Guardar servicio
        self.servicio = servicio

    # Método para mostrar información de la reserva
    def mostrar(self):

        return f"{self.cliente.nombre} - {self.servicio.nombre}"

            
