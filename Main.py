import time
import random
from Sorting import *

class Main():
	
    def __init__(self):
        print("Herzlich Willkommen!!")
        print("")
     
    def startProgramm(self):
        print("Bubble = 1")
        print("Insertion = 2")
        print("Merge = 3")
        print("Quick = 4")
        print("")
        
        md = int(input("Bitte wähle eine Sortiermethode: "))
        return md
    
    def createData(self):
        print("Erzeuge 1 Mio Daten ...")
        daten = []
        
        for i in range(10): # standardmäßig 1 Mio
            daten.append(random.randint(1,10000))
        n = len(daten)
        
        return daten
    
    def startSorting(self, data, mtd):      
        print("Daten gelesen, Sortierung beginnt...")
        print('Array: ', data)
        s = Sorting(data)

        switcher = {
            1: s.BubbleSort(),
            2: s.InsertionSort(),
            3: s.MergeSort(),
            4: s.QuickSort()
        }
        t1 = time.perf_counter()
        res = switcher.get(mtd, "Invalid Input")
        t2 = time.perf_counter()
        t = t2 - t1

        print('Sortierungs-Zeit',t, ' seconds')
        print('Sortierte Daten:' , res)
			
                       
if __name__ == "__main__":
    m = Main()
    typ = m.startProgramm()
    if typ > 0 and typ < 5:
        d = m.createData()
        m.startSorting(d, typ)
        
    
    

