from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva


def guardar_log(error):

    with open("logs.txt", "a") as archivo:
        archivo.write(str(error) + "\n")


print("SISTEMA SOFTWARE FJ")


# OPERACION 1
try:
    cliente1 = Cliente("Sandy", 20, "sandy@gmail.com")
    servicio1 = ReservaSala()

    reserva1 = Reserva(cliente1, servicio1, 2)
    reserva1.confirmar()
    reserva1.mostrar_reserva()

except Exception as e:
    print("Error:", e)
    guardar_log(e)


# OPERACION 2
try:
    cliente2 = Cliente("", 19, "correo@gmail.com")

except Exception as e:
    print("Error:", e)
    guardar_log(e)


# OPERACION 3
try:
    cliente3 = Cliente("Carlos", -5, "correo@gmail.com")

except Exception as e:
    print("Error:", e)
    guardar_log(e)


# OPERACION 4
try:
    cliente4 = Cliente("Ana", 25, "correo")

except Exception as e:
    print("Error:", e)
    guardar_log(e)


# OPERACION 5
try:
    cliente5 = Cliente("Laura", 22, "laura@gmail.com")
    servicio2 = AlquilerEquipo()

    reserva2 = Reserva(cliente5, servicio2, 3)
    reserva2.confirmar()
    reserva2.mostrar_reserva()

except Exception as e:
    print("Error:", e)
    guardar_log(e)


# OPERACION 6
try:
    cliente6 = Cliente("Pedro", 30, "pedro@gmail.com")
    servicio3 = AsesoriaEspecializada()

    reserva3 = Reserva(cliente6, servicio3, -1)

except Exception as e:
    print("Error:", e)
    guardar_log(e)
    # OPERACION 7
try:
    cliente7 = Cliente("Mario", 28, "mario@gmail.com")
    servicio4 = ReservaSala()

    reserva4 = Reserva(cliente7, servicio4, 4)
    reserva4.confirmar()
    reserva4.mostrar_reserva()

except Exception as e:
    print("Error:", e)
    guardar_log(e)


# OPERACION 8
try:
    cliente8 = Cliente("Luisa", 21, "luisa@gmail.com")
    servicio5 = AlquilerEquipo()

    reserva5 = Reserva(cliente8, servicio5, 2)
    reserva5.cancelar()
    reserva5.mostrar_reserva()

except Exception as e:
    print("Error:", e)
    guardar_log(e)


# OPERACION 9
try:
    cliente9 = Cliente("", 15, "malcorreo")

except Exception as e:
    print("Error:", e)
    guardar_log(e)


# OPERACION 10
try:
    cliente10 = Cliente("Andres", 35, "andres@gmail.com")
    servicio6 = AsesoriaEspecializada()

    reserva6 = Reserva(cliente10, servicio6, 5)
    reserva6.confirmar()
    reserva6.mostrar_reserva()

except Exception as e:
    print("Error:", e)
    guardar_log(e)