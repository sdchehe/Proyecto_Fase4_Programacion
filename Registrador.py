# ==========================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Archivo de registro de eventos del sistema
# Autora: Maria Clara Lopera Causil
#
# Funciones principales:
# - Registrar acciones del sistema
# - Guardar mensajes en logs.txt
# - Registrar fecha y hora automática
# - Control de eventos y procesos
# - Apoyo al manejo de excepciones
# ==========================================================
from datetime import datetime


class Registrador:

    @staticmethod
    def registrar(mensaje):

        # Abrir el archivo en modo agregar
        with open("logs.txt", "a", encoding="utf-8") as archivo:

            # Obtener fecha y hora actual
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Guardar mensaje en el archivo
            archivo.write(f"{fecha} - {mensaje}\n")
from datetime import datetime

class Registrador:

    @staticmethod
    def registrar(mensaje):

        with open("logs.txt", "a", encoding="utf-8") as archivo:

            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            archivo.write(f"{fecha} - {mensaje}\n")
