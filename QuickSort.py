import time
import random

class QuickSort():

    def __init__(self, arr):
        self.arr = arr
     
    def sort(self):
        self.quickSort(0, len(self.arr) - 1)
        return self.arr
    
    def quickSort(self, left, right):
        if left >= right: return
        
        pivotPos = self.partition(left, right)
        self.quickSort(left, pivotPos - 1)
        self.quickSort(pivotPos + 1, right)
    
    def partition(self, left, right):
        pivot = self.arr[right]
        
        i = left
        j = right - 1
        while i < j:
            while self.arr[i] < pivot:
                i += 1
            
            while j > left and self.arr[j] >= pivot:
                j -= 1
            
            if i < j:
                self.swap(i,j)
                i += 1
                j -= 1
        
        if i == j and self.arr[i] < pivot:
            i += 1
        
        if self.arr[i] != pivot:
            self.swap(i, right)
         
        return i
         
    def swap(self, x, y):
        temp = self.arr[x] 
        self.arr[x] = self.arr[y]
        self.arr[y] = temp
        return self.arr


# Zum Testen der Klasse --------------------------------------------------------------------------
if __name__ == '__main__':
    daten = []
    for i in range(1000000): # Anzahl der verschiedenen Zahlen angeben 
            daten.append(random.randint(1,10000))
    n = len(daten)

    qs = QuickSort(daten)
    print('Generierter Array: ', daten)

    t1 = time.perf_counter()
    res = qs.sort()    
    t2 = time.perf_counter()
    t = t2 - t1

    print('Rechenzeit: ', t, ' sekunden')
    print(res)



        
        

        

    