class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
    # Declaring index position
        self.x = 0
    # Creating empty list with fixed amount as capacity
        self.stored = [None]*capacity

    def append(self, item):
        # declaring item var
        self.stored[self.x] = item
    # add to stored list new item
        self.x += 1
    # removing item if greater than buffer value and resetting index value
        if self.x > self.capacity - 1:
            self.x = 0

# None to account for length of list items stored
# and a None value return will cause error
    def get(self):
        return [item for item in self.stored if item is not None]
