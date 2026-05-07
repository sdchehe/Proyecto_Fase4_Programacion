class Cliente:

    def __init__(self, nombre, edad, correo):

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")

        if edad <= 0:
            raise ValueError("Edad inválida")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__edad = edad
        self.__correo = correo

    def mostrar_datos(self):
        print(f"Cliente: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Correo: {self.__correo}")