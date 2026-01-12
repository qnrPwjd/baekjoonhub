import sys
import math
input = sys.stdin.readline

heap = ['root']
heap_count = 0

def pickLargestOrSmallestDescendantIndex(index, largest):
    global heap, heap_count
    resultIndex, resultValue = index * 2, heap[index * 2]
    candids = [ # Children and grandchildren
        index * 2 + 1, # Right child
        index * 4, # 1st grandchild (Left child of left child)
        index * 4 + 1, # 2nd grandchild (Right child of left cihld)
        index * 4 + 2, # 3rd grandchild (Left child of right child)
        index * 4 + 3 # 4th grandchild (Right child of right child)
    ]

    for candidIndex in candids:
        if candidIndex > heap_count:
            continue # If it's invalid index, continue

        if largest and resultValue < heap[candidIndex]:
            resultValue = heap[candidIndex]
            resultIndex = candidIndex
        elif not largest and resultValue > heap[candidIndex]:
            resultValue = heap[candidIndex]
            resultIndex = candidIndex

    return resultIndex

def pushDown(index):
    if (lambda index : int(math.log2(index)) % 2 == 0)(index) :
        pushDownMin(index)
    else:
        pushDownMax(index)

def pushDownMin(index):
    global heap, heap_count
    if index * 2 <= heap_count: # if has children
        m = pickLargestOrSmallestDescendantIndex(index, False)

        if (m >= index * 4): # if m is a grandchild
            if (heap[m] < heap[index]):
                heap[m], heap[index] = heap[index], heap[m]
                if (heap[m] > heap[m // 2]):
                    heap[m], heap[m // 2] = heap[m // 2], heap[m]
                pushDown(m)
        elif (heap[m] < heap[index]):
            heap[m], heap[index] = heap[index], heap[m] 

def pushDownMax(index):
    global heap, heap_count
    if (index * 2 <= heap_count): # if has children
        m = pickLargestOrSmallestDescendantIndex(index, True)

        if (m >= index * 4): # if m is a grandchild
            if (heap[m] > heap[index]):
                heap[m], heap[index] = heap[index], heap[m]
                if (heap[m] < heap[m // 2]):
                    heap[m], heap[m // 2] = heap[m // 2], heap[m]
                pushDown(m)
        elif (heap[m] > heap[index]):
            heap[m], heap[index] = heap[index], heap[m]

def popMin():
    global heap, heap_count
    if heap_count <= 0:
        return
    # Removes minimum element
    heap[1] = heap[heap_count]
    heap.pop(heap_count)
    heap_count -= 1
    # Push down root element to make the heap valid min-max heap
    pushDown(1)

def popMax():
    global heap, heap_count
    if heap_count <= 0:
        return
    
    index = 0
    if heap_count == 1:
        index = 1
    elif heap_count == 2:
        index = 2
    else :
        index = 2 if heap[2] > heap[3] else 3
    
    # Removes maximum element
    heap[index] = heap[heap_count]
    heap.pop(heap_count)
    heap_count -= 1
    # Push down to root element make the heap valid min-max heap
    pushDown(index)

def pushUpMin(index):
    global heap
    if index >= 4 and heap[index] < heap[index // 4]: # if index >= 4, it must have a grandparent.
            heap[index], heap[index // 4] = heap[index // 4], heap[index]
            pushUpMin(index // 4)

def pushUpMax(index):
    global heap
    if index >= 4 and heap[index] > heap[index // 4]: # if index >= 4, it must have a grandparent.
            heap[index], heap[index // 4] = heap[index // 4], heap[index]
            pushUpMax(index // 4)

def pushUp(index):
    global heap
    if index != 1 :
        if (lambda index : int(math.log2(index)) % 2 == 0)(index) :
            if heap[index] > heap[index // 2] :
                heap[index], heap[index // 2] = heap[index // 2], heap[index]
                pushUpMax(index // 2)
            else :
                pushUpMin(index)
        else :
            if heap[index] < heap[index // 2] :
                heap[index], heap[index // 2] = heap[index // 2], heap[index]
                pushUpMin(index // 2)
            else :
                pushUpMax(index)

def insertHeap(item):
    global heap, heap_count
    heap_count += 1
    heap.append(item)
    pushUp(heap_count)

def seekMin():
    if heap_count == 0:
        return 'EMPTY'
    return heap[1]

def seekMax():
    if heap_count == 0:
        return 'EMPTY'
    elif heap_count == 1:
        return heap[1]
    elif heap_count == 2:
        return heap[2]
    else:
        return max(heap[2], heap[3])
    
T = int(input())

for _ in range(T):
    k = int(input())

    for __ in range(k):
        command, n = input().strip().split()
        n = int(n)
            
        if command == 'I':
            insertHeap(n)
        elif command =='D':
            if n == -1:
                popMin()
            else:
                popMax()

    cur_max, cur_min = seekMax(), seekMin()

    if heap_count == 0:
        print('EMPTY')
    else:
        print(f"{cur_max} {cur_min}")

    heap = ['root']
    heap_count = 0