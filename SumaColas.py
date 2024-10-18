class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def ver_primero(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            return None


def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()
    
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        elemento_a = cola_a.desencolar()
        elemento_b = cola_b.desencolar()
        
        suma = elemento_a + elemento_b
        cola_resultado.encolar(suma)
    
    return cola_resultado


cola_a = Cola()
cola_b = Cola()


cola_a.encolar(3)
cola_a.encolar(4)
cola_a.encolar(2)
cola_a.encolar(8)
cola_a.encolar(12)



cola_b.encolar(6)
cola_b.encolar(2)
cola_b.encolar(9)
cola_b.encolar(11)
cola_b.encolar(3)


cola_resultado = sumar_colas(cola_a, cola_b)


while not cola_resultado.esta_vacia():  #el while not se usa mientras la condicion sea negativa que en este caso es si la cola esta vacia
    print(cola_resultado.desencolar())
