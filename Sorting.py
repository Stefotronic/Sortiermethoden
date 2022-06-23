import BubbleSort


class Sorting:

    def __init__(self, arr) -> None:
        self.arr = arr

    def BubbleSort(self):
        n = len(self.arr)
        swapped = False
    
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.arr[j] > arr[j + 1]:
                    swapped = True
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
         
            if not swapped:
                return
            
        return self.arr
 

    def InsertionSort(self):
        pass
    
    def MergeSort(self):
        pass

    def QuickSort(self):
        pass

