from mundo_pc.teclado import Teclado
from mundo_pc.Monitor import Monitor
from mundo_pc.raton import Raton
class Computadora:
    contador_computadoras=0
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras +=1
        self._id_computadoras= Computadora.contador_computadoras
        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton
    def __str__(self):
        return f'''
        {self._nombre}:{self._id_computadoras}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton
if __name__=='__main__':
    teclado1=Teclado('HP','USB')
    raton1=Raton('LG', 'USB')
    monitor1= Monitor('HP',15)
    computadora1= Computadora('HP',monitor1,teclado1,raton1)
    print(computadora1)
    teclado2= Teclado('ACER', 'Bluetooth')
    raton2= Raton('ACER', 'Bluetooth')
    monitor2= Monitor('ACER',27)
    computadora2= Computadora('ACER',teclado2,raton2,monitor2)
    print(computadora2)


