class Monitor:
    contador_monitores=0
    def __init__(self,marca,tamaño):
        Monitor.contador_monitores +=1
        self._id_monitores=Monitor.contador_monitores
        self._marca=marca
        self._tamaño=tamaño
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca=marca
    @property
    def tamaño(self):
        return self._tamaño
    @tamaño.setter
    def tamaño(self,tamaño):
        self._tamaño=tamaño

    def __str__(self):
        return f'Id: {self._id_monitores}, Marca: {self._marca}, Tamaño: {self._tamaño}'
if __name__=='__main__':
    monitor1=Monitor('LG',15)
    print(monitor1)




