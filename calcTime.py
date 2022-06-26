import time
import random

def calculateTime():
    print("Erzeuge 1 Mio Daten ...")
    daten = []
    
    for i in range(1000000):
        daten.append(random.randint(1,10000))
    n = len(daten)
    
    print("Daten gelesen, Sortierung beginnt...")
    # Sortiermethoden auswahl
    t1 = time.perf_counter()
    
    # Sortierungsfunktion an binden
    
    t2 = time.perf_counter()
    t = t2 - t1
    
    print('Sortierungs-Rechenzeit: ', t, ' secods')
        