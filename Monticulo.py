import random 
import math

class Monticulo:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap_size = 0
        self.A = [] * capacity
        self.size = len(self.A)
        

    def inicializar(self):
        self.A = [random.randint(1,100) for _ in range(self.capacity)]

    def mostrar(self):
        print(self.A)

    def parent(self, i):        #indice del hijo
        R = math.ceil((i/2)-1)      #Para aproximar decimales al entero mayor más cercano
        if R < 0:
            return 0
        else:
            return R

    def Left(self, i):      #indice del padre
        return 2*i+ 1

    def Right(self, i):     #indice del padre
        return 2*i + 2

    def  max_heapify(self, j):     
        l = self.Left(j)
        r = self.Right(j)
        if l <= self.heap_size and self.A[l] > self.A[j]:     
            larguest = l
        else: 
            larguest = j

        if r <= self.heap_size and self.A[r] > self.A[larguest]:      
            larguest = r
        if larguest != j:
            temp = self.A[j]
            self.A[j] = self.A[larguest]
            self.A[larguest] = temp
            self.max_heapify(larguest)        

    def build_max_heap(self):
        for i in range(len(self.A) // 2 - 1, -1, -1):  
            self.max_heapify(i)     

    def heap_sort(self):
        self.build_max_heap()
        heap_size = len(self.A)     
        for i in range(len(self.A) - 1, 0, -1):
            temp = self.A[i]
            self.A[i] = self.A[0]
            self.A[0] = temp
            heap_size -= 1
            self.max_heapify(0)     

    #Cola prioritaria
    def max_heap_insert(self, k):        #A = arreglo, k = numero a insertar
        self.heap_size += 1          
        i = self.heap_size
        self.A[i] = k
        while i > 0 and self.A[self.parent(i)] < self.A[i]:
            temp = self.A[self.parent(i)]
            self.parent(i) == self.A[i]        
            self.A[i] = temp
            i = self.parent(i)

    def heap_extract_max(self):       
        max = self.A[0]
        self.A[0] = self.A[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(0)
        return max 

    def heap_maximum(self):
        return self.A[0]








