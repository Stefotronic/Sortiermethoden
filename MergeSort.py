import sys
import time
import random

class MergeSort():

    def __init__(self):
        sys.setrecursionlimit(2000)

    def sort(self, arr):
        if len(arr) > 1:
            r = len(arr)//2
            L = arr[:r]
            M = arr[r:]

            self.sort(L)
            self.sort(M)

            i = j = k = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = M[j]
                    j += 1
                k += 1
            
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < len(M):
                arr[k] = M[j]
                j += 1
                k += 1
            
        return  arr
    
    def printList(self):
        for i in range(len(self.arr)):
            print(self.arr[i], end=" ")
        print()


# Zum Testen der Klasse --------------------------------------------------------------------------
if __name__ == '__main__':
    daten = []
    for i in range(1000000): # Anzahl der verschiedenen Zahlen angeben 
            daten.append(random.randint(1,10000))
    n = len(daten)

    ms = MergeSort()
    print('Generierter Array: ', daten)

    t1 = time.perf_counter()
    res = ms.sort(daten)    
    t2 = time.perf_counter()
    t = t2 - t1

    print('Rechenzeit: ', t, ' sekunden')
    print(res)



# Hiermit kann diese Klasse gestartet werden
lst = [64, 34, 25, 12, 22, 11, 90]
ms = MergeSort()
res = ms.sort(lst)
print(res)

