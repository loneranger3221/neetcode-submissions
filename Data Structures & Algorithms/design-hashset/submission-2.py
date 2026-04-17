class MyHashSet:
    '''This is the best approach . 
    use the concept of hashing and chaining
    use num%1000 as mapping function '''
    def __init__(self):
        self.size = 10000
        # Create 10,000 empty buckets (lists)
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        # This tells us which bucket index the key goes into
        return key % self.size

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        # Only add it if it's not already in that specific bucket
        if key not in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        # If it's in the bucket, remove it
        if key in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        # Just check that one specific bucket
        return key in self.buckets[bucket_idx]