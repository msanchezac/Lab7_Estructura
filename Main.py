from Monticulo import *

m = Monticulo(20)
m.inicializar()
print("Monticulo lleno de valores aleatorios: (20 elementos): ")
m.mostrar()

print("Implementación de la clase Monticulo(Heap): ")
print("Padre del indice 3: ")
print(m.parent(3))

print("Hijo izquierdo del indice 1: ")
print(m.Left(1))

print("Hijo derecho del indice 1")
print(m.Right(1))

print("Padre del indice 2: ")
print(m.parent(2))

print("MAX-HEAPIFY: ") 
m.max_heapify(2)
m.mostrar()


print("Implementación BUILD-MAX-HEAP: ")
m.build_max_heap()
m.mostrar()

print("Implementación cola prioritaria ")
print("Implementación HEAPSORT: ")
m.heap_sort()
m.mostrar()

print("Implementación MAX-HEAP-INSERT, insertando el número 5 al arreglo: ")
m.max_heap_insert(5)
m.mostrar()

print("Implementación HEAP-EXTRACT-MAX: ")  
m.heap_extract_max()
m.mostrar()

print("Implementación HEAP-MAXIMUM: ")
print(m.heap_maximum())



