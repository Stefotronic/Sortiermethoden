import time
import random

class InsertionSort():

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        l = len(self.arr)
        
        for i in range(l):
            elementToSort = self.arr[i]
            j = i

            while j > 0 and elementToSort < self.arr[j-1]:
                self.arr[j] = self.arr[j-1]
                j -= 1
            self.arr[j] = elementToSort

        return self.arr


# Zum Testen der Klasse --------------------------------------------------------------------------
if __name__ == '__main__':
    daten = []
    for i in range(1000000): # Anzahl der verschiedenen Zahlen angeben 
            daten.append(random.randint(1,10000))
    n = len(daten)

    ist = InsertionSort(daten)
    print('Generierter Array: ', daten)

    t1 = time.perf_counter()
    res = ist.sort()    
    t2 = time.perf_counter()
    t = t2 - t1

    print('Rechenzeit: ', t, ' sekunden')
    print(res)


