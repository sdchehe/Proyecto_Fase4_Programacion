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
class Registrador:

    def registrar_cliente(self, nombre):

        try:

            if nombre == "":
                raise ValueError(
                    "El nombre no puede estar vacío"
                )

            print(
                f"Cliente {nombre} registrado correctamente"
            )

        except ValueError as e:

            print(f"ERROR: {e}")

        except Exception as e:

            print(f"ERROR DEL SISTEMA: {e}")


registro = Registrador()

registro.registrar_cliente("Bladimir")
