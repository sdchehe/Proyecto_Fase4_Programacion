# ============================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES
# SERVICIOS Y RESERVAS
# ============================================
import tkinter as tk
from tkinter import messagebox

# ============================================
# CLASE LOGGER
# ============================================
class Logger:
   def log(self, mensaje):
       print(f"LOG: {mensaje}")

# ============================================
# CLASE CLIENTE
# ============================================
class Cliente:
   def __init__(self, nombre, identificacion):
       self.nombre = nombre
       self.identificacion = identificacion
   def get_nombre(self):
       return self.nombre

# ============================================
# CLASES SERVICIOS
# ============================================
class Servicio:
   def __init__(self, nombre, precio):
       self.nombre = nombre
       self.precio = precio
   def descripcion(self):
       return f"{self.nombre} - ${self.precio:.2f}"

class ServicioSala(Servicio):
   pass

class ServicioEquipo(Servicio):
   pass

class ServicioAsesoria(Servicio):
   pass

# ============================================
# CLASE RESERVA
# ============================================
class Reserva:
   def __init__(self, cliente, servicio, duracion):
       self.cliente = cliente
       self.servicio = servicio
       self.duracion = duracion
       self.estado = "Pendiente"
   def confirmar(self):
       self.estado = "Confirmada"

# ============================================
# VARIABLES GLOBALES
# ============================================
clientes = []
servicios = []
reservas = []
logger = Logger()

# ============================================
# FUNCIONES
# ============================================
def crear_cliente():
   try:
       nombre = entry_nombre.get().strip()
       identificacion = entry_id.get().strip()
       if not nombre:
           raise ValueError("Ingrese el nombre del cliente")
       if not identificacion:
           raise ValueError("Ingrese la identificación")
       cliente = Cliente(nombre, identificacion)
       clientes.append(cliente)
       actualizar_listas()
       messagebox.showinfo(
           "Éxito",
           "Cliente creado correctamente"
       )
       entry_nombre.delete(0, tk.END)
       entry_id.delete(0, tk.END)
   except Exception as e:
       logger.log(str(e))
       messagebox.showerror(
           "Error",
           str(e)
       )

def crear_servicio():
   try:
       nombre = entry_servicio.get().strip()
       precio_texto = entry_precio.get().strip()
       tipo = tipo_servicio.get()
       if not nombre:
           raise ValueError("Ingrese el nombre del servicio")
       if not precio_texto:
           raise ValueError("Ingrese el precio")
       try:
           precio = float(precio_texto)
       except:
           raise ValueError("Ingrese un precio válido")
       if precio <= 0:
           raise ValueError(
               "El precio debe ser mayor que cero"
           )
       if tipo == "Sala":
           servicio = ServicioSala(
               nombre,
               precio
           )
       elif tipo == "Equipo":
           servicio = ServicioEquipo(
               nombre,
               precio
           )
       elif tipo == "Asesoria":
           servicio = ServicioAsesoria(
               nombre,
               precio
           )
       else:
           raise ValueError(
               "Seleccione un tipo válido"
           )
       servicios.append(servicio)
       actualizar_listas()
       messagebox.showinfo(
           "Éxito",
           "Servicio creado correctamente"
       )
       entry_servicio.delete(0, tk.END)
       entry_precio.delete(0, tk.END)
   except Exception as e:
       logger.log(str(e))
       messagebox.showerror(
           "Error",
           str(e)
       )

def crear_reserva():
   try:
       if not lista_clientes.curselection():
           raise ValueError(
               "Seleccione un cliente"
           )
       if not lista_servicios.curselection():
           raise ValueError(
               "Seleccione un servicio"
           )
       duracion_texto = entry_duracion.get().strip()
       if not duracion_texto:
           raise ValueError(
               "Ingrese la duración"
           )
       try:
           duracion = int(duracion_texto)
       except:
           raise ValueError(
               "La duración debe ser numérica"
           )
       if duracion <= 0:
           raise ValueError(
               "La duración debe ser mayor que cero"
           )
       idx_cliente = lista_clientes.curselection()[0]
       idx_servicio = lista_servicios.curselection()[0]
       reserva = Reserva(
           clientes[idx_cliente],
           servicios[idx_servicio],
           duracion
       )
       reservas.append(reserva)
       actualizar_listas()
       messagebox.showinfo(
           "Éxito",
           "Reserva creada correctamente"
       )
       entry_duracion.delete(0, tk.END)
   except Exception as e:
       logger.log(str(e))
       messagebox.showerror(
           "Error",
           str(e)
       )

def confirmar_reserva():
   try:
       if not lista_reservas.curselection():
           raise ValueError(
               "Seleccione una reserva"
           )
       idx = lista_reservas.curselection()[0]
       reservas[idx].confirmar()
       actualizar_listas()
       messagebox.showinfo(
           "Éxito",
           "Reserva confirmada"
       )
   except Exception as e:
       logger.log(str(e))
       messagebox.showerror(
           "Error",
           str(e)
       )

def actualizar_listas():
   # =========================
   # CLIENTES
   # =========================
   lista_clientes.delete(0, tk.END)
   for cliente in clientes:
       lista_clientes.insert(
           tk.END,
           f"{cliente.get_nombre()} - {cliente.identificacion}"
       )
   # =========================
   # SERVICIOS
   # =========================
   lista_servicios.delete(0, tk.END)
   for servicio in servicios:
       lista_servicios.insert(
           tk.END,
           servicio.descripcion()
       )
   # =========================
   # RESERVAS
   # =========================
   lista_reservas.delete(0, tk.END)
   for reserva in reservas:
       texto = (
           f"Cliente: {reserva.cliente.get_nombre()} | "
           f"Servicio: {reserva.servicio.descripcion()} | "
           f"Duración: {reserva.duracion}h | "
           f"Estado: {reserva.estado}"
       )
       lista_reservas.insert(
           tk.END,
           texto
       )

# ============================================
# INTERFAZ GRÁFICA
# ============================================
ventana = tk.Tk()
ventana.title(
   "Sistema Integral de Reservas"
)
ventana.geometry("700x700")
ventana.resizable(False, False)

# ============================================
# TÍTULO
# ============================================
titulo = tk.Label(
   ventana,
   text="SISTEMA DE GESTIÓN DE RESERVAS",
   font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# ============================================
# CLIENTES
# ============================================
frame_clientes = tk.LabelFrame(
   ventana,
   text="Clientes",
   padx=10,
   pady=10
)
frame_clientes.pack(
   fill="x",
   padx=10,
   pady=5
)
tk.Label(
   frame_clientes,
   text="Nombre del Cliente"
).pack()
entry_nombre = tk.Entry(
   frame_clientes,
   width=40
)
entry_nombre.pack(pady=3)
tk.Label(
   frame_clientes,
   text="Identificación"
).pack()
entry_id = tk.Entry(
   frame_clientes,
   width=40
)
entry_id.pack(pady=3)
tk.Button(
   frame_clientes,
   text="Crear Cliente",
   bg="#4CAF50",
   fg="white",
   command=crear_cliente
).pack(pady=5)

# ============================================
# SERVICIOS
# ============================================
frame_servicios = tk.LabelFrame(
   ventana,
   text="Servicios",
   padx=10,
   pady=10
)
frame_servicios.pack(
   fill="x",
   padx=10,
   pady=5
)
tk.Label(
   frame_servicios,
   text="Nombre del Servicio"
).pack()
entry_servicio = tk.Entry(
   frame_servicios,
   width=40
)
entry_servicio.pack(pady=3)
tk.Label(
   frame_servicios,
   text="Precio"
).pack()
entry_precio = tk.Entry(
   frame_servicios,
   width=40
)
entry_precio.pack(pady=3)
tipo_servicio = tk.StringVar()
tipo_servicio.set("Sala")
tk.Label(
   frame_servicios,
   text="Tipo de Servicio"
).pack()
tk.OptionMenu(
   frame_servicios,
   tipo_servicio,
   "Sala",
   "Equipo",
   "Asesoria"
).pack(pady=3)
tk.Button(
   frame_servicios,
   text="Crear Servicio",
   bg="#2196F3",
   fg="white",
   command=crear_servicio
).pack(pady=5)

# ============================================
# RESERVAS
# ============================================
frame_reservas = tk.LabelFrame(
   ventana,
   text="Reservas",
   padx=10,
   pady=10
)
frame_reservas.pack(
   fill="both",
   expand=True,
   padx=10,
   pady=5
)
tk.Label(
   frame_reservas,
   text="Duración (horas)"
).pack()
entry_duracion = tk.Entry(
   frame_reservas,
   width=40
)
entry_duracion.pack(pady=3)
# LISTA CLIENTES
tk.Label(
   frame_reservas,
   text="Lista de Clientes"
).pack()
lista_clientes = tk.Listbox(
   frame_reservas,
   width=60,
   height=5
)
lista_clientes.pack(pady=5)
# LISTA SERVICIOS
tk.Label(
   frame_reservas,
   text="Lista de Servicios"
).pack()
lista_servicios = tk.Listbox(
   frame_reservas,
   width=60,
   height=5
)
lista_servicios.pack(pady=5)
tk.Button(
   frame_reservas,
   text="Crear Reserva",
   bg="#FF9800",
   fg="white",
   command=crear_reserva
).pack(pady=5)
# LISTA RESERVAS
tk.Label(
   frame_reservas,
   text="Reservas Registradas"
).pack()
lista_reservas = tk.Listbox(
   frame_reservas,
   width=90,
   height=8
)
lista_reservas.pack(pady=5)
tk.Button(
   frame_reservas,
   text="Confirmar Reserva",
   bg="#9C27B0",
   fg="white",
   command=confirmar_reserva
).pack(pady=10)

# ============================================
# INICIAR SISTEMA
# ============================================
ventana.mainloop()

       

      
        

    
   
    
