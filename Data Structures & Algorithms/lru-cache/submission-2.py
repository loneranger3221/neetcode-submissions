from collections import OrderedDict
'''Python's built-in collections.OrderedDict keeps track of the order
keys are inserted or modified, making a true LRU cache
incredibly easy to build:'''

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to mark it as Most Recently Used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and mark as recently used
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                ''' popitem(last=False) removes 
                the first (Least Recently Used) item in O(1)'''
                self.cache.popitem(last=False)
                
            self.cache[key] = value
