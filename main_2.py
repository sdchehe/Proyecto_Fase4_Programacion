# =========================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Autor: BLADIMIR ALFONSO ESPANA
# =========================================================

# =========================================================
# IMPORTAR LIBRERÍAS
# =========================================================

import tkinter as tk
from tkinter import messagebox

# =========================================================
# CLASE LOGGER
# =========================================================

class Logger:
    
    def log(self, mensaje):
        print(f"LOG: {mensaje}")

# =========================================================
# CLASE CLIENTE
# =========================================================

class Cliente:

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_cliente(self):
        return f"Cliente: {self.nombre} | Correo: {self.correo}"

# =========================================================
# CLASE SERVICIO
# =========================================================

class Servicio:

    def __init__(self, nombre_servicio, precio):
        self.nombre_servicio = nombre_servicio
        self.precio = precio

    def mostrar_servicio(self):
        return f"Servicio: {self.nombre_servicio} | Precio: ${self.precio}"

# =========================================================
# CLASE RESERVA
# =========================================================

class Reserva:

    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar_reserva(self):
        self.estado = "Confirmada"

    def mostrar_reserva(self):
        return (
            f"{self.cliente.nombre} reservó "
            f"{self.servicio.nombre_servicio} "
            f"- Estado: {self.estado}"
        )

# =========================================================
# CLASE PRINCIPAL DEL SISTEMA
# =========================================================

class SistemaGestion:

    def __init__(self, ventana):

        self.logger = Logger()

        self.ventana = ventana
        self.ventana.title("Sistema Integral de Gestión")
        self.ventana.geometry("500x500")

        # =========================================
        # TÍTULO
        # =========================================

        titulo = tk.Label(
            ventana,
            text="SISTEMA DE GESTIÓN DE CLIENTES",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=10)

        # =========================================
        # NOMBRE CLIENTE
        # =========================================

        tk.Label(ventana, text="Nombre del Cliente").pack()

        self.entry_cliente = tk.Entry(ventana, width=40)
        self.entry_cliente.pack(pady=5)

        # =========================================
        # CORREO
        # =========================================

        tk.Label(ventana, text="Correo Electrónico").pack()

        self.entry_correo = tk.Entry(ventana, width=40)
        self.entry_correo.pack(pady=5)

        # =========================================
        # SERVICIO
        # =========================================

        tk.Label(ventana, text="Nombre del Servicio").pack()

        self.entry_servicio = tk.Entry(ventana, width=40)
        self.entry_servicio.pack(pady=5)

        # =========================================
        # PRECIO
        # =========================================

        tk.Label(ventana, text="Precio del Servicio").pack()

        self.entry_precio = tk.Entry(ventana, width=40)
        self.entry_precio.pack(pady=5)

        # =========================================
        # BOTÓN REGISTRAR
        # =========================================

        boton = tk.Button(
            ventana,
            text="Registrar Reserva",
            command=self.registrar_reserva,
            bg="green",
            fg="white",
            width=25
        )

        boton.pack(pady=15)

        # =========================================
        # ÁREA DE RESULTADOS
        # =========================================

        self.texto_resultado = tk.Text(
            ventana,
            width=60,
            height=10
        )

        self.texto_resultado.pack(pady=10)

    # =====================================================
    # MÉTODO REGISTRAR RESERVA
    # =====================================================

    def registrar_reserva(self):

        nombre = self.entry_cliente.get()
        correo = self.entry_correo.get()
        servicio_nombre = self.entry_servicio.get()
        precio = self.entry_precio.get()

        if (
            nombre == "" or
            correo == "" or
            servicio_nombre == "" or
            precio == ""
        ):

            messagebox.showerror(
                "Error",
                "Todos los campos son obligatorios"
            )

            return

        # =========================================
        # CREAR OBJETOS
        # =========================================

        cliente = Cliente(nombre, correo)

        servicio = Servicio(servicio_nombre, precio)

        reserva = Reserva(cliente, servicio)

        reserva.confirmar_reserva()

        # =========================================
        # MOSTRAR RESULTADOS
        # =========================================

        informacion = (
            cliente.mostrar_cliente() + "\n" +
            servicio.mostrar_servicio() + "\n" +
            reserva.mostrar_reserva() + "\n" +
            "====================================\n"
        )

        self.texto_resultado.insert(tk.END, informacion)

        self.logger.log("Reserva registrada correctamente")

        messagebox.showinfo(
            "Éxito",
            "Reserva registrada correctamente"
        )

# =========================================================
# EJECUTAR SISTEMA
# =========================================================

ventana = tk.Tk()

aplicacion = SistemaGestion(ventana)

ventana.mainloop()
 




   
  
       

      
        

    
   
    
