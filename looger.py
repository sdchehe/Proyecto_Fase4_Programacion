# ==========================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Archivo de manejo de registros (Logger)
# Autor: Bladimir Alfonso España
#
# Funciones principales:
# - Registrar eventos del sistema
# - Guardar mensajes en el archivo logs.txt
# - Registrar fecha y hora automáticamente
# - Controlar acciones y procesos del sistema
# - Apoyar el manejo de errores y excepciones
# ==========================================================

from datetime import datetime


class Logger:

    # Método para registrar mensajes en el archivo logs.txt
    def log(self, mensaje):

        # Abrir el archivo en modo agregar
        with open("logs.txt", "a", encoding="utf-8") as archivo:

            # Obtener fecha y hora actual
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Guardar mensaje con fecha y hora
            archivo.write(f"{fecha} - {mensaje}\n")
