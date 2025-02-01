from Monticulo import *

class ColaPrioritaria(Monticulo):



    def max_heap_insert(self, k):        #A = arreglo, k = numero a insertar
            self.heap_size += 1          
            i = self.heap_size - 1
            self.A.append(k)
            while i > 0 and self.A[self.parent(i)] < self.A[i]:
                temp = self.A[self.parent(i)]
                self.A[self.parent(i)] = self.A[i]        
                self.A[i] = temp
                i = self.parent(i)

    def heap_extract_max(self):       
        max = self.A[0]
        self.A[0] = self.A[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max 

    def heap_maximum(self):
        return self.A[0]
