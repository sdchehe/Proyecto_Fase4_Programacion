# =========================================================
# Sistema de Gestión de Clientes y Reservas
# Fase 4 - Componente práctico - Prácticas simuladas
# Autor: Keimer Manuel Sanchez Gutierrez
# =========================================================
# Importamos las clases necesarias desde los módulos del proyecto
from cliente import Cliente
from Servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from Reserva import Reserva
from Registrador import Registrador

# Listas para almacenar clientes y reservas
clientes = []
reservas = []

# OPERACIONES: Lista de tuplas con datos de clientes para probar (válidos e inválidos)
operaciones = [
    # Cliente válido
    ("Juan", "juan@gmail.com", "123456"),
    # Cliente inválido (nombre corto, correo malo, teléfono no numérico)
    ("Lu", "correoMAL", "abc"),
    # Cliente válido
    ("Maria", "maria@gmail.com", "987654"),
]

# Bucle para procesar cada operación y crear clientes
for datos in operaciones:
    try:
        # Creamos un cliente con los datos de la tupla
        cliente = Cliente(*datos)
        # Agregamos el cliente a la lista
        clientes.append(cliente)
        # Registramos en el log que el cliente fue registrado
        Registrador.registrar(f"Cliente registrado: {cliente.get_nombre()}")
    except Exception as e:
        # Si hay error, lo registramos en el log
        Registrador.registrar(f"ERROR cliente: {e}")

# Servicios: Intentamos crear instancias de servicios especializados
try:
    # Creamos una reserva de sala
    sala = ReservaSala("Sala VIP", 50000)
    # Creamos un alquiler de equipo
    equipo = AlquilerEquipo("Computador", 30000)
    # Creamos una asesoría especializada
    asesoria = AsesoriaEspecializada("Consultoría", 80000)
except Exception as e:
    # Si hay error al crear servicios, lo registramos
    Registrador.registrar(f"ERROR servicio: {e}")

# Reservas: Intentamos crear y confirmar una reserva válida
try:
    # Creamos una reserva para el primer cliente con la sala por 3 unidades
    r1 = Reserva(clientes[0], sala, 3)
    # Confirmamos la reserva
    r1.confirmar()
    # Procesamos el pago y obtenemos el total
    total = r1.procesar_pago()
    # Agregamos la reserva a la lista
    reservas.append(r1)
    # Registramos la confirmación en el log
    Registrador.registrar(f"Reserva confirmada. Total: {total}")
except Exception as e:
    # Si hay error en la reserva, lo registramos
    Registrador.registrar(f"ERROR reserva: {e}")

# Reserva inválida: Intentamos crear una reserva con datos inválidos (cantidad negativa)
try:
    # Creamos una reserva con cantidad negativa (inválida)
    r2 = Reserva(clientes[0], equipo, -5)
    # Intentamos confirmar (debería fallar)
    r2.confirmar()
except Exception as e:
    # Registramos el error de la reserva inválida
    Registrador.registrar(f"ERROR reserva inválida: {e}")

# Mensaje final indicando que el sistema funciona correctamente
print("Sistema funcionando correctamente")
