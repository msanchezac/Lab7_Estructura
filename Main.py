from Monticulo import *
from ColaPrioritaria import *

m = Monticulo()
arreglo = random.sample(range(1,100), 20)

print("Arreglo lleno de valores aleatorios: (20 elementos): ")
print(arreglo)

print("Implementación BUILD-MAX-HEAP: ")
m.build_max_heap(arreglo.copy())
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


print("Implementación cola prioritaria ")
print("Implementación HEAPSORT: ")
m.heap_sort()
m.mostrar()

c = ColaPrioritaria()       #heredamos los atributos pero no su contenido, al usarse sus metodos, en cola prioritaria el arreglo inicia vacio.
c.build_max_heap(arreglo)

print("Implementación MAX-HEAP-INSERT, insertando el número 5 al arreglo: ")        #Al usar el metodo despues del for, reorganiza los numeros en un orden distinto pero sigue cumpliendo la propiedad de un heap
c.max_heap_insert(100)           
c.mostrar()

print("Implementación HEAP-EXTRACT-MAX: ")  
c.heap_extract_max()
c.mostrar()

print("Implementación HEAP-MAXIMUM: ")
print(c.heap_maximum())



