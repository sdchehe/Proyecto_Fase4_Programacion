# ============================================
# MÓDULO DE EXCEPCIONES PERSONALIZADAS
#
# Este archivo contiene las excepciones
# utilizadas en el sistema para manejar
# errores de forma robusta y controlada.
# ============================================
class ErrorSistema(Exception):
    """Clase base para todos los errores del sistema"""
    pass


# -------------------------
# ERRORES DE VALIDACIÓN
# -------------------------
class ErrorValidacion(ErrorSistema):
    """Errores de datos inválidos"""
    pass


class ErrorCliente(ErrorValidacion):
    """Errores relacionados con clientes"""
    pass


class ErrorServicio(ErrorValidacion):
    """Errores relacionados con servicios"""
    pass


class ErrorReserva(ErrorValidacion):
    """Errores relacionados con reservas"""
    pass


# -------------------------
# ERRORES DE OPERACIÓN
# -------------------------
class ErrorOperacion(ErrorSistema):
    """Errores en operaciones del sistema"""
    pass


class ErrorReservaDuplicada(ErrorOperacion):
    """Reserva ya confirmada"""
    pass


class ErrorServicioNoDisponible(ErrorOperacion):
    """Servicio no disponible"""
    pass


# -------------------------
# FUNCIÓN PARA ENCADENAMIENTO
# -------------------------
def manejar_error(mensaje, error_original):
    """Encadena excepciones para mayor detalle"""
    raise ErrorSistema(mensaje) from error_original
       

