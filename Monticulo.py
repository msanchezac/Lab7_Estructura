import random 
import math

class Monticulo:
    def __init__(self):  
        self.heap_size = 0
        self.A = [] 
        

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
        if l < self.heap_size and self.A[l] > self.A[j]:     
            larguest = l
        else: 
            larguest = j

        if r < self.heap_size and self.A[r] > self.A[larguest]:      
            larguest = r
        if larguest != j:
            temp = self.A[j]
            self.A[j] = self.A[larguest]
            self.A[larguest] = temp
            self.max_heapify(larguest) 
      

    def build_max_heap(self, arreglo):
        self.A = arreglo
        self.heap_size = len(arreglo)
        for i in range(len(self.A) // 2 - 1, -1, -1):  
            self.max_heapify(i)     

    def heap_sort(self):
        self.build_max_heap(self.A)   
        for i in range(len(self.A) - 1, 0, -1):
            temp = self.A[i]
            self.A[i] = self.A[0]
            self.A[0] = temp
            self.heap_size -= 1
            self.max_heapify(0)     







