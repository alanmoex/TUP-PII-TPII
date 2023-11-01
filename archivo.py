from datetime import date

class Archivo:
    def __init__(self, nombre:str, formato:str) -> None:
        self.__nombre = nombre
        self.__fecha = date.today()
        self.__formato = formato
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre
    
    @property
    def fecha(self) -> object:
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha: object):
        self.__fecha = fecha
    
    @property
    def formato(self) -> str:
        return self.__formato
    
    @formato.setter
    def formato(self, formato: str):
        self.__formato = formato
    
    def __str__(self) -> str:
        return f"{self.nombre}.{self.formato}"