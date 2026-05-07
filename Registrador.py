from datetime import datetime

class Registrador:

    @staticmethod
    def registrar(mensaje):

        with open("logs.txt", "a", encoding="utf-8") as archivo:

            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            archivo.write(f"{fecha} - {mensaje}\n")
