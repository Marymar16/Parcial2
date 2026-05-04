class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaSimple:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoSimple(dato)

        if not self.head:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        print(" -> ".join(resultado) + " -> None")

    def partir_voltear_intercalar(self):
        if self.head is None:
            return None, None

        lento = self.head
        rapido = self.head

        while rapido.next is not None and rapido.next.next is not None:
            lento = lento.next
            rapido = rapido.next.next

        segunda = lento.next
        lento.next = None

        # invertir segunda mitad
        prev = None
        actual = segunda

        while actual is not None:
            siguiente = actual.next
            actual.next = prev
            prev = actual
            actual = siguiente

        return self.head, prev
    if __name__ == "__main__":
        print("\n===== Punto 2 =====")
        lista_s = ListaSimple()

        for x in [1, 2, 3, 4, 5, 6]:
            lista_s.insertar_final(x)

        lista_s.mostrar()

        lista_s.partir_voltear_intercalar()

        print("Resultado:")
        lista_s.mostrar()