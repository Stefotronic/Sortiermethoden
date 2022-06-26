import time
import random

class BubbleSort():

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        # optimize code, so if the array is already sorted, it doesn't need
        # to go through the entire process
        swapped = False
        # Traverse through all array elements
        for i in range(n-1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.
            # Last i elements are already in place
            for j in range(0, n-i-1):
     
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if self.arr[j] > self.arr[j + 1]:
                    swapped = True
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
             
            if not swapped:
                # if we haven't needed to make a single swap, we
                # can just exit the main loop.
                return

        return self.arr
 
 
# Zum testen dieser Klasse -----------------------------------------------------------------------
if __name__ == '__main__':
    daten = []
    for i in range(1000000): # Anzahl der verschiedenen Zahlen angeben 
            daten.append(random.randint(1,10000))
    n = len(daten)

    bs = BubbleSort(daten)
    print('Generierter Array: ', daten)

    t1 = time.perf_counter()
    res = bs.sort()    
    t2 = time.perf_counter()
    t = t2 - t1

    print('Rechenzeit: ', t, ' sekunden')
    print(res)