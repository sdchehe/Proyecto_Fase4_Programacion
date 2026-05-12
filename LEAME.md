from abc import ABC, abstractmethod import logging

CONFIGURACIÓN DE LOGS
logging.basicConfig( filename="logs.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s" )

print("\n===== SISTEMA SOFTWARE FJ =====\n")

RESÚMENES DE CLASE
clase Entidad(ABC):

def __init__(self, id):
    self._id = id

@abstractmethod
def mostrar_info(self):
    pass
CLASE CLIENTE
clase Cliente(Entidad):

def __init__(self, id, nombre, email, telefono):
    super().__init__(id)

    if len(nombre) < 3:
        raise ValueError("Nombre demasiado corto")

    if "@" not in email:
        raise ValueError("Email inválido")

    if not telefono.isdigit():
        raise ValueError("Teléfono inválido")

    self.__nombre = nombre
    self.__email = email
    self.__telefono = telefono

def mostrar_info(self):
    return f"Cliente: {self.__nombre}"
CLASE ABSTRACTA SERVICIO
clase Servicio(ABC):

def __init__(self, nombre, precio):
    if precio <= 0:
        raise ValueError("Precio inválido")

    self.nombre = nombre
    self.precio = precio

@abstractmethod
def calcular_costo(self):
    pass

@abstractmethod
def descripcion(self):
    pass
SERVICIO BÁSICO
clase ServicioBásico(Servicio):

def calcular_costo(self):
    return self.precio * 1.10

def descripcion(self):
    return "Servicio Básico"
SERVICIO PREMIUM
clase ServicioPremium(Servicio):

def calcular_costo(self):
    return self.precio * 1.25

def descripcion(self):
    return "Servicio Premium"
SERVICIO EMPRESARIAL
clase ServicioEmpresarial(Servicio):

def calcular_costo(self):
    return self.precio * 1.50 - 20

def descripcion(self):
    return "Servicio Empresarial"
CLASE RESERVA
clase Reserva:

def __init__(self, cliente, servicio, duracion):

    if cliente is None:
        raise ValueError("Cliente no válido")

    if duracion <= 0:
        raise ValueError("Duración inválida")

    self.cliente = cliente
    self.servicio = servicio
    self.duracion = duracion
    self.estado = "Pendiente"

def confirmar(self):

    try:
        self.estado = "Confirmada"
        print("Reserva confirmada")
        logging.info("Reserva confirmada")

    except Exception as e:
        print("Error al confirmar")
        logging.error(e)

def cancelar(self):

    try:
        self.estado = "Cancelada"
        print("Reserva cancelada")
        logging.warning("Reserva cancelada")

    except Exception as e:
        print("Error al cancelar")
        logging.error(e)

def procesar(self):

    try:
        costo = self.servicio.calcular_costo()

    except Exception as e:
        print("Error procesando reserva")
        logging.error(e)

    else:
        print("Costo calculado: {costo}")

    finally:
        print("Proceso finalizado")

# Sobrecarga simulada
def calcular_total(self, impuesto=0.19, descuento=0):

    subtotal = self.servicio.calcular_costo() * self.duracion

    total = subtotal + (subtotal * impuesto) - descuento

    return total
10 OPERACIONES
OPERACIÓN 1
print("\nOPERACIÓN 1: Cliente válido")

prueba: cliente1 = Cliente(1, "Fernanda", " fernanda@gmail.com ", "123456789") print(cliente1.mostrar_info())

excepto Exception como e: imprimir(e)

OPERACIÓN 2
print("\nOPERACIÓN 2: Cliente inválido")

prueba: cliente2 = Cliente(2, "Fe", "correo", "abc")

excepto Exception as e: print("Error", e) logging.error(e)

OPERACIÓN 3
print("\nOPERACIÓN 3: Servicio Básico")

prueba: servicio1 = ServicioBasico("Diseño Web", 100) print(servicio1.descripcion())

excepto Exception como e: imprimir(e)

OPERACIÓN 4
print("\nOPERACIÓN 4: Servicio Premium")

prueba: servicio2 = ServicioPremium("App Móvil", 300) print(servicio2.descripcion())

excepto Exception como e: imprimir(e)

OPERACIÓN 5
print("\nOPERACIÓN 5: Servicio Empresarial")

prueba: servicio3 = ServicioEmpresarial("Sistema ERP", 500) print(servicio3.descripcion())

excepto Exception como e: imprimir(e)

OPERACIÓN 6
print("\nOPERACIÓN 6: Servicio inválido")

prueba: servicio_error = ServicioBasico("Error", -50)

excepto Exception as e: print("Error", e) logging.error(e)

OPERACIÓN 7
print("\nOPERACIÓN 7: Reserva válida")

prueba: reserva1 = Reserva(cliente1, servicio1, 2) reserva1.confirmar()

excepto Exception como e: imprimir(e)

OPERACIÓN 8
print("\nOPERACIÓN 8: Procesar reserva")

Intentar: reserva1.procesar()

excepto Exception como e: imprimir(e)

OPERACIÓN 9
print("\nOPERACIÓN 9: Calcular total")

prueba: total = reserva1.calcular_total(descuento=10) print("Total", total)

excepto Exception como e: imprimir(e)

OPERACIÓN 10
print("\nOPERACIÓN 10: Reserva inválida")

try: reserva_error = Reserva(None, servicio2, -1)

excepto Exception as e: print("Error", e) logging.error(e)

print("\n===== FIN DEL SISTEMA =====")
