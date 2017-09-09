import math, random

_defaultCompare = lambda x, y: x - y
_defaultKey = lambda a: a

def isSorted(l, compare=_defaultCompare, key=_defaultKey, ascending=False):   
    for i in range(len(l)-1):
        if 0 < compare(key(l[i]), key(l[i+1])) * (-1 if ascending else 1):
            return False
    return True


class _Template(object):
    def __init__(self, compare=_defaultCompare, key=_defaultKey, ascending=False):
        self._compare = compare
        self._key = key
        self._ascending = ascending
        
        self._sortingInput = None
        self._sortingList = []
    
    def _compareByIndex(self, a, b):
        return self._compareElements(self._sortingList[a], self._sortingList[b])
                                     
    def _compareElements(self, a, b):
        com = self._compare(self._key(a), self._key(b))
        if self._ascending: com *= -1
        return com
    
    def _exchangeByIndex(self, a, b):
        tmp = self._sortingList[a]
        self._sortingList[a] = self._sortingList[b]
        self._sortingList[b] = tmp
    
    def _copyList(self, fr):
        to = []
        for e in fr:
            to.append(e)
        return to
    
    def sort(self, o, cloneBeforeSort=True):
        self._sortingInput = o
        self._sortingList = self._copyList(o) if cloneBeforeSort else o
        
        self._do()
        
        return self._sortingList
    
    def _do(self):
        raise NotImplementedError


class BadAlgorithm(_Template):
    ## WARNING! DON'T USE THIS FUNCTION FOR MORE THEN 8 ELEMENTS!!!
    
    def _do(self):
        while not isSorted(self._sortingList, self._compare, self._key, self._ascending):
            random.shuffle(self._sortingList)

class BubbleSort(_Template):
    def _do(self):
        for i in range(0, len(self._sortingList)-1):
            changed = False
            for j in range(0, len(self._sortingList)-i-1):
                if self._compareByIndex(j, j+1) > 0:
                    self._exchangeByIndex(j, j+1)
                    changed = True

            if not changed:
                break

class SelectionSort(_Template):
    def _do(self):
        for sortedCounter in range(0, len(self._sortingList)):
            max = 0
            for i in range(1, len(self._sortingList)-sortedCounter):
                if self._compareByIndex(i, max) > 0:
                    max = i
            if max != len(self._sortingList)-sortedCounter-1:
                self._exchangeByIndex(max, len(self._sortingList)-sortedCounter-1)
    
class InsertSort(_Template):
    def _do(self):
        for i in range(1, len(self._sortingList)):
            j = i - 1
            tmp = self._sortingList[i]
            while j >= 0 and self._compareElements(self._sortingList[j], tmp) > 0:
                self._sortingList[j+1] = self._sortingList[j]
                j -= 1
            self._sortingList[j+1] = tmp

class QuickSort(_Template):
    def _do(self):
        self._rek(0, len(self._sortingList)-1)
    
    def _rek(self, links, rechts):
        li = links
        re = rechts
        vergl = self._sortingList[int((links + rechts) / 2)]

        first = True
        while first or li <= re:
            first = False
            while self._compareElements(self._sortingList[li], vergl) < 0:
                li += 1
            while self._compareElements(self._sortingList[re], vergl) > 0:
                re -= 1
            if li <= re:
                self._exchangeByIndex(li, re)
                li += 1
                re -= 1
        if links < re:
            self._rek(links, re)
        if rechts > li:
            self._rek(li, rechts)

class MergeSort(_Template):
    def _do(self):
        self._rek(1)
    
    def _rek(self, block):
        tmp = self._copyList(self._sortingList)
        
        if block < len(self._sortingList):
            for compNo in range(int(math.ceil(len(self._sortingList) / (2.0 * block)))):
                s1 = block * 2 * compNo
                s2 = s1 + block
                i1 = s1
                i2 = s2
                                
                for c in range(2 * block):
                    i1AmLimit = i1 >= s2
                    i2AmLimit = i2 >= s2 + block
                    
                    used = 1
                    if not (i1AmLimit or i2AmLimit):
                        used = 1 if self._compareByIndex(i1, i2) < 0 else 2
                    elif i1AmLimit:
                        used = 2

                    tmp[s1 + c] = self._sortingList[i1 if used == 1 else i2]
                    if used == 1:
                        i1 += 1
                    else:
                        i2 += 1
                    
            self._sortingList = tmp    
            self._rek(block * 2)

class HeapSort(_Template):
    def drain(self, i, l, r):
        drainNeed = True
        tmp = self._sortingList[i]
        
        while 2*(i-l)+1+l <= r:
            j = 2 * (i - l) + 1 + l
            if j+1 <= r and self._compareByIndex(j, j+1) < 0:
                j += 1
            if self._compareElements(tmp, self._key(self._sortingList[j])) < 0:
                self._sortingList[i] = self._sortingList[j]
                i = j
            else:
                self._sortingList[i] = tmp
                i = r
                drainNeed = False
        
        if drainNeed:
            self._sortingList[i] = tmp
        
    def _do(self):
        for i in range(int((len(self._sortingList)+1)/2))[::-1]:
            self.drain(i, 0, len(self._sortingList)-1)
        for i in range(len(self._sortingList))[::-1]:
            self._exchangeByIndex(0, i)
            self.drain(0, 0, i-1)