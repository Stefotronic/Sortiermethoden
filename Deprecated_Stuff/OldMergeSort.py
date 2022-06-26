import sys

class MergeSort():

    def __init__(self, arr):
        self.arr = arr
        sys.setrecursionlimit(2000)

    def sort(self):
        length = len(self.arr)
        sorted = self.mergeSort(0, length - 1)
        dest = self.arrayCopy(sorted, 0, self.arr, 0, length)
        return dest
        
        
    def mergeSort(self, left, right):
        if left == right:
            res = []
            val = self.arr[left]
            res.append(val)
            return res

        mid = left + (right - left) / 2
        leftArr = self.mergeSort(left, mid)
        rightArr = self.mergeSort(mid + 1, right)
        return self.merge(leftArr, rightArr)

    def merge(self, leftArr, rightArr):
        target = []
        leftLen = len(leftArr)
        rightLen = len(rightArr)

        target[leftLen + rightLen]
        targetPos = 0
        leftPos = 0
        rightPos = 0

        while leftPos < leftLen and rightPos < rightLen:
            leftVal = leftArr[leftPos]
            rightVal = rightArr[rightPos]

            if leftVal <= rightVal:
                target[targetPos + 1] = leftVal
                leftPos += 1
            else:
                target[targetPos + 1] = rightVal
                rightPos += 1

        while leftPos < leftLen:
            target[targetPos + 1] = leftArr[leftPos + 1]

        while rightPos < rightLen:
            target[targetPos + 1] = rightArr[rightPos + 1]

        return target
        
    def arrayCopy(self, src, srcPos, dest, destPos, length):
        for i in range(length):
            dest[i + destPos] = src[i + srcPos]
 
                
        
# Hiermit kann diese Klasse gestartet werden
lst = [64, 34, 25, 12, 22, 11, 90]
ms = MergeSort(lst)
res = ms.sort()
print(res)

