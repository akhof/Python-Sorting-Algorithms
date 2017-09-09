
from PySortAlgos import BadAlgorithm, BubbleSort, SelectionSort, InsertSort, QuickSort, MergeSort, HeapSort, isSorted

import time, random

START_E = 2  # 2^2 = 4
MAX_E = 22  # 2^22 = 4.194.304
TRIES = 1

TOTEST = (
    
   #(Class,         Name,            Max)
    (BadAlgorithm,  "BadAlgorithm",  3),
    (BubbleSort,    "BubbleSort",    12),
    (SelectionSort, "SelectionSort", 13),
    (InsertSort,    "InsertSort",    14),
    (HeapSort,      "HeapSort",      19),
    (MergeSort,     "MergeSort",     22),
    (QuickSort,     "QuickSort",     22),
    
    )


nameList = ""
for r in TOTEST:
    nameList += ("\t\t" if len(nameList) > 0 else "") + r[1]
print("Elements\t\t" + nameList)

e = START_E
while e <= MAX_E:
    res = []
    max = -1
    for r in TOTEST:
        if e > r[2]:
            res.append(None)
        else:
            sum = 0
            for _ in range(TRIES):
                l = list(range(0, 2**e))
                random.shuffle(l)
                t1 = time.time()
                sortedlist = r[0]().sort(l)
                sum += time.time() - t1
                if not isSorted(sortedlist):
                    print("Error in " + r[1])
            res.append(sum / TRIES)
            if res[-1] > max:
                max = res[-1]
    
    tp = "2^" + str(e) + " = " + str(2**e) + " \t\t"
    for v in res:
        if v == None:
            tp += " \t\t"
        else:
            p = "0"
            if max > 0:
                p = str(round(100*v/max, 2))
            tp += str(round(v, 5)) + "s (" + p + "%)"
            if v == 0: tp += "   "
        tp += "    \t"
    print(tp)
    
    e += 1
        
print("\nFinish :)")