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
class Logger:

    def log(self, mensaje):

        with open("logs/sistema.log", "a", encoding="utf-8") as archivo:
            archivo.write(f"{mensaje}\n")

        print(f"LOG: {mensaje}")

           
