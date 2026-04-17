class MyHashSet:
    def __init__(self):
        # Create an array of 1,000,001 elements, all set to False
        self.set = [False] * 1000001

    def add(self, key: int) -> None:
        # Just flip the boolean at that exact index to True
        self.set[key] = True

    def remove(self, key: int) -> None:
        # Flip it back to False
        self.set[key] = False

    def contains(self, key: int) -> bool:
        # Check the boolean at that index
        return self.set[key]