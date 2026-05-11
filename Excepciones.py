# ==========================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Archivo de manejo de excepciones personalizadas
# Autora: Maria Clara Lopera Causil
#
# Funciones principales:
# - Manejo de errores en clientes
# - Manejo de errores en servicios
# - Manejo de errores en reservas
# - Personalización de excepciones
# - Control y validación del sistema
# ==========================================================
def dividir_numeros():

    try:

        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))

        resultado = numero1 / numero2

        print(f"Resultado: {resultado}")

    except ValueError:

        print("ERROR: Debe ingresar solo números.")

    except ZeroDivisionError:

        print("ERROR: No se puede dividir entre cero.")

    except Exception as e:

        print("ERROR DEL SISTEMA:")
        print(e)

    finally:

        print("Programa finalizado.")


dividir_numeros()

