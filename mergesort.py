
import random

def merge (arrayList, left, right):
    i = j = k = 0
    while i < len (left) and j < len (right): 
        if left[i] < right[j]: 
            arrayList[k] = left[i] 
            i+=1
        else: 
            arrayList[k] = right[j] 
            j+=1
        k+=1
          
    while i < len (left): 
        arrayList[k] = left[i] 
        i+=1
        k+=1
        
    while j < len (right): 
        arrayList[k] = right[j] 
        j+=1
        k+=1

def mergeSort (arrayList):
    if len( arrayList) > 1:
        middle = len (arrayList) // 2
        left = arrayList[:middle]
        right = arrayList[middle:]

        mergeSort (left)
        mergeSort (right)
        merge (arrayList, left, right)
  
if __name__ == '__main__': 
    rand = random.randint(0,100)
    print ("Number of elements to sort:", rand)
    matrix = []

    for r in range(rand):
        newRand = random.randint(0,100)
        matrix.append(newRand)
 
    print ("Given array is:", end="\n")  
    print (matrix) 
    mergeSort (matrix) 
    print("Sorted array is:", end="\n") 
    print (matrix)