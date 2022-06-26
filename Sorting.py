from winreg import QueryValueEx
from BubbleSort import *
from InsertionSort import *
from QuickSort import QuickSort
from MergeSort import MergeSort


class Sorting:

    def __init__(self, arr) -> None:
        self.arr = arr


    def BubbleSort(self):
        bs = BubbleSort(self.arr)
        return bs.sort()
 
    def InsertionSort(self):
        ist = InsertionSort(self.arr)
        return ist.sort() 
    
    def MergeSort(self):
        ms = MergeSort()
        return ms.sort(self.arr)
    
    def QuickSort(self):
        qs = QuickSort(self.arr)
        return qs.sort()
        

