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

        try:

            archivo = open(
                "log.txt",
                "a"
            )

            archivo.write(
                mensaje + "\n"
            )

            archivo.close()

            print(
                "Mensaje guardado correctamente"
            )

        except Exception as e:

            print(
                f"ERROR AL GUARDAR LOG: {e}"
            )


logger = Logger()

logger.log(
    "Sistema iniciado correctamente"
)


       
