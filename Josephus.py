class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def josephus_modificado(self, m):
        if self.head is None:
            return None

        actual = self.head
        while actual.next is not None:
            actual = actual.next
        actual.next = self.head

        actual = self.head
        anterior = None

        while actual.next != self.head:
            actual = actual.next

        anterior = actual
        actual = self.head

        while actual.next != actual:
            for i in range(m - 1):
                anterior = actual
                actual = actual.next

            print("Eliminado:", actual.data)

            eliminado = actual.data

            # eliminar nodo
            anterior.next = actual.next
            actual = actual.next

            if eliminado % 5 == 0:
                actual = actual.next
                anterior = anterior.next

        print("Sobreviviente:", actual.data)
if __name__ == "__main__":

    print("===== Punto 1 =====")
    lista_c = ListaCircular()
    lista_c.crear_lista(7)
    lista_c.mostrar()

    sobreviviente = lista_c.josephus_modificado(3)
    print("Sobreviviente:", sobreviviente)


    