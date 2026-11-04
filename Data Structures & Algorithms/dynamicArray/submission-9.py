class DynamicArray:
    
    def __init__(self, capacity: int):
        # set the environments
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity
    
    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        # find the last filled index in the array, 
        # save n to the next, and add 1 to the size.
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1

        return self.arr[self.size]

    def resize(self) -> None:
        # find the capacity of the array
        # double it
        self.capacity *= 2
        # create a new variable for the new arr you created
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        # copy the content of the old array into the new arr
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
