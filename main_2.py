from modelos.cliente import Cliente
from modelos.servicios_especializados import *
from modelos.reserva import Reserva
from utilidades.logger import registrar_log

clientes = []
reservas = []

# OPERACIONES

operaciones = [

    # Válida
    ("Juan", "juan@gmail.com", "123456"),

    # Inválida
    ("Lu", "correoMAL", "abc"),

    # Válida
    ("Maria", "maria@gmail.com", "987654"),
]

for datos in operaciones:

    try:

        cliente = Cliente(*datos)
        clientes.append(cliente)

        registrar_log(f"Cliente registrado: {cliente.get_nombre()}")

    except Exception as e:

        registrar_log(f"ERROR cliente: {e}")

# Servicios

try:

    sala = ReservaSala("Sala VIP", 50000)
    equipo = AlquilerEquipo("Computador", 30000)
    asesoria = AsesoriaEspecializada("Consultoría", 80000)

except Exception as e:

    registrar_log(f"ERROR servicio: {e}")

# Reservas

try:

    r1 = Reserva(clientes[0], sala, 3)
    r1.confirmar()

    total = r1.procesar_pago()

    reservas.append(r1)

    registrar_log(f"Reserva confirmada. Total: {total}")

except Exception as e:

    registrar_log(f"ERROR reserva: {e}")

# Reserva inválida

try:

    r2 = Reserva(clientes[0], equipo, -5)

    r2.confirmar()

except Exception as e:

    registrar_log(f"ERROR reserva inválida: {e}")

print("Sistema funcionando correctamente")
