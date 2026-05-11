# =========================================================
# SISTEMA DE GESTIÓN DE RESERVAS
# Autor: Bladimir Alfonso Espana
# =========================================================

# =========================================================
# IMPORTAR LIBRERÍAS
# =========================================================

# tkinter sirve para crear interfaces gráficas
import tkinter as tk

# messagebox permite mostrar ventanas emergentes
from tkinter import messagebox


# =========================================================
# CLASE CLIENTE
# =========================================================

# Esta clase representa a un cliente del sistema
class Cliente:

    # Constructor de la clase
    def __init__(self, nombre):

        # Guardar nombre del cliente
        self.nombre = nombre


# =========================================================
# CLASE SERVICIO
# =========================================================

# Esta clase representa un servicio
class Servicio:

    # Constructor de la clase
    def __init__(self, nombre):

        # Guardar nombre del servicio
        self.nombre = nombre


# =========================================================
# CLASE RESERVA
# =========================================================

# Esta clase relaciona un cliente con un servicio
class Reserva:

    # Constructor de la clase
    def __init__(self, cliente, servicio):

        # Guardar cliente
        self.cliente = cliente

        # Guardar servicio
        self.servicio = servicio

    # Método para mostrar información de la reserva
    def mostrar(self):

        return f"{self.cliente.nombre} - {self.servicio.nombre}"


# =========================================================
# LISTAS GLOBALES
# =========================================================

# Lista para almacenar clientes
clientes = []

# Lista para almacenar servicios
servicios = []

# Lista para almacenar reservas
reservas = []


# =========================================================
# FUNCIÓN AGREGAR CLIENTE
# =========================================================

def agregar_cliente():

    # Obtener el texto escrito en el Entry
    nombre = entry_cliente.get()

    # Verificar si el campo está vacío
    if nombre == "":

        # Mostrar mensaje de error
        messagebox.showerror(
            "Error",
            "Ingrese un nombre"
        )

        return

    # Crear objeto cliente
    cliente = Cliente(nombre)

    # Guardar cliente en la lista
    clientes.append(cliente)

    # Mostrar cliente en el Listbox
    lista_clientes.insert(
        tk.END,
        cliente.nombre
    )

    # Limpiar el Entry
    entry_cliente.delete(0, tk.END)


# =========================================================
# FUNCIÓN AGREGAR SERVICIO
# =========================================================

def agregar_servicio():

    # Obtener texto del Entry
    nombre = entry_servicio.get()

    # Verificar si está vacío
    if nombre == "":

        # Mostrar mensaje de error
        messagebox.showerror(
            "Error",
            "Ingrese un servicio"
        )

        return

    # Crear objeto servicio
    servicio = Servicio(nombre)

    # Guardar servicio en la lista
    servicios.append(servicio)

    # Mostrar servicio en pantalla
    lista_servicios.insert(
        tk.END,
        servicio.nombre
    )

    # Limpiar Entry
    entry_servicio.delete(0, tk.END)


# =========================================================
# FUNCIÓN CREAR RESERVA
# =========================================================

def crear_reserva():

    # Verificar si seleccionó cliente
    if not lista_clientes.curselection():

        # Mostrar error
        messagebox.showerror(
            "Error",
            "Seleccione un cliente"
        )

        return

    # Verificar si seleccionó servicio
    if not lista_servicios.curselection():

        # Mostrar error
        messagebox.showerror(
            "Error",
            "Seleccione un servicio"
        )

        return

    # Obtener cliente seleccionado
    cliente = clientes[
        lista_clientes.curselection()[0]
    ]

    # Obtener servicio seleccionado
    servicio = servicios[
        lista_servicios.curselection()[0]
    ]

    # Crear reserva
    reserva = Reserva(
        cliente,
        servicio
    )

    # Guardar reserva en lista
    reservas.append(reserva)

    # Mostrar reserva en Listbox
    lista_reservas.insert(
        tk.END,
        reserva.mostrar()
    )

    # Mensaje de éxito
    messagebox.showinfo(
        "Éxito",
        "Reserva creada correctamente"
    )


# =========================================================
# CREAR VENTANA PRINCIPAL
# =========================================================

# Crear ventana
ventana = tk.Tk()

# Título de la ventana
ventana.title(
    "Sistema de Reservas"
)

# Tamaño de la ventana
ventana.geometry("600x500")

# Color de fondo
ventana.config(bg="#F2F2F2")


# =========================================================
# TÍTULO PRINCIPAL
# =========================================================

titulo = tk.Label(

    # Ventana donde irá el texto
    ventana,

    # Texto que aparecerá
    text="SISTEMA DE GESTIÓN DE RESERVAS",

    # Fuente
    font=("Arial", 16, "bold"),

    # Color de fondo
    bg="#F2F2F2",

    # Color de texto
    fg="black"
)

# Mostrar título
titulo.pack(pady=10)


# =========================================================
# SECCIÓN CLIENTES
# =========================================================

# Etiqueta
tk.Label(
    ventana,
    text="Cliente",
    bg="#F2F2F2"
).pack()

# Caja de texto
entry_cliente = tk.Entry(
    ventana,
    width=40
)

entry_cliente.pack()

# Botón registrar cliente
tk.Button(
    ventana,
    text="Agregar Cliente",
    bg="#4CAF50",
    fg="white",
    command=agregar_cliente
).pack(pady=5)

# Lista de clientes
lista_clientes = tk.Listbox(
    ventana,
    width=50,
    height=5
)

lista_clientes.pack(pady=10)


# =========================================================
# SECCIÓN SERVICIOS
# =========================================================

# Etiqueta
tk.Label(
    ventana,
    text="Servicio",
    bg="#F2F2F2"
).pack()

# Caja de texto
entry_servicio = tk.Entry(
    ventana,
    width=40
)

entry_servicio.pack()

# Botón agregar servicio
tk.Button(
    ventana,
    text="Agregar Servicio",
    bg="#2196F3",
    fg="white",
    command=agregar_servicio
).pack(pady=5)

# Lista de servicios
lista_servicios = tk.Listbox(
    ventana,
    width=50,
    height=5
)

lista_servicios.pack(pady=10)


# =========================================================
# SECCIÓN RESERVAS
# =========================================================

# Botón crear reserva
tk.Button(
    ventana,
    text="Crear Reserva",
    bg="#FF9800",
    fg="white",
    command=crear_reserva
).pack(pady=10)

# Lista de reservas
lista_reservas = tk.Listbox(
    ventana,
    width=60,
    height=10
)

lista_reservas.pack(pady=10)


# =========================================================
# INICIAR EL SISTEMA
# =========================================================

# Ejecutar ventana
ventana.mainloop()
