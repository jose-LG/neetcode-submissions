class MyHashSet:

    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)
        

    def remove(self, key: int) -> None:
        #Removing can also be done in constant time
        #we'll use discard to do it safely, but .remove should be used if we need to guarantee that
        #the key should have existed

        self.hashset.discard(key)
        

    def contains(self, key: int) -> bool:
        #O(1) time lookup for sets but O(n) for arrays

        if key in self.hashset:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)