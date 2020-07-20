import unittest


class Heap:
    def __init__(self):
        self.data = [0]

    def __str__(self):
        return "{}".format(self.data[1:])

    def insert(self, val):
        self.data.append(val)
        self.sift_up()

    # 添加时使用
    def sift_up(self, curr=None):
        current_index = len(self.data) - 1 if not curr else curr
        parent_index = (len(self.data) - 1) // 2
        while parent_index:
            current, parent = self.data[current_index], self.data[parent_index]
            if current > parent:
                self.data[current_index], self.data[parent_index] = self.data[parent_index], self.data[current_index]
            parent_index, current_index = parent_index // 2, parent_index

    def extract_max(self):
        if len(self.data) == 2:
            return self.data.pop()
        if len(self.data) < 2:
            return None
        heap_max = self.get_max()
        self.data[1] = self.data.pop()
        self.sift_down()
        return heap_max

    def sift_down(self, data=None, curr=None):
        current_index = 1 if not curr else curr
        data = self.data if not data else data
        length = len(data) - 1

        while True:
            left_child_index = current_index * 2
            if left_child_index > length:
                return
            right_child_index = current_index * 2 + 1

            if right_child_index > length:
                if data[current_index] < data[left_child_index]:
                    data[current_index], data[left_child_index] = data[left_child_index], data[
                        current_index]
                return
            if data[left_child_index] > data[right_child_index]:
                if data[current_index] < data[left_child_index]:
                    data[current_index], data[left_child_index] = data[left_child_index], data[
                        current_index]
                    current_index = left_child_index
            else:
                if data[current_index] < data[right_child_index]:
                    data[current_index], data[right_child_index] = data[right_child_index], data[
                        current_index]
                    current_index = right_child_index

    def remove(self, i):
        self.data[i] = float("inf")
        self.sift_up(i)
        self.extract_max()

    # create a heap from an array of elements, needed for heap_sort
    def heapify(self, arr):
        self.data = [0]
        for a in arr:
            self.insert(a)

    def heapify2(self, arr):
        arr.insert(0, 0)
        for i in range(len(arr) // 2, 0, -1):
            self.sift_down(arr, i)
        arr.pop(0)

    def heap_sort(self, arr):
        self.heapify(arr)
        result = []
        while len(self.data) != 1:
            result.append(self.extract_max())
        return result

    # get max without remove
    def get_max(self):
        if len(self.data) < 2:
            return None
        return self.data[1]

    def get_size(self):
        return len(self.data) - 1

    def is_empty(self):
        return self.get_size() == 1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.h = Heap()
        self.h.insert(2)
        self.h.insert(1)
        self.h.insert(5)
        self.h.insert(10)
        self.h.insert(4)
        self.h.insert(7)

    def test_extract_max(self):
        print(self.h)
        print(self.h.extract_max())
        print(self.h)
        print(self.h.extract_max())
        print(self.h)
        print(self.h.extract_max())
        print(self.h)
        print(self.h.extract_max())
        print(self.h)
        print(self.h.extract_max())
        print(self.h)
        print(self.h.extract_max())
        print(self.h)
        print(self.h.extract_max())
        print(self.h)

    def test_remove(self):
        print(self.h)
        self.h.remove(3)
        print(self.h)

    def test_heapify(self):
        print(self.h)
        self.h.heapify([2, 1, 5, 10, 4, 7])
        print(self.h)

    def test_heap_sort(self):
        print(self.h)
        print(self.h.heap_sort([2, 1, 5, 10, 4, 7]))

    def test_heapify2(self):
        arr = [2, 1, 5, 10, 4, 7]
        self.h.heapify2(arr)
        print(arr)

"""
# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra 
"""