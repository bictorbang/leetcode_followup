# 146. LRU Cache
# Design a data structure that follows the constraints 
# of a Least Recently Used (LRU) cache.
#
#Implement the LRUCache class:
# 
# LRUCache(int capacity) Initialize the LRU cache with 
# positive size capacity.
#
# int get(int key)              Return the value of the key 
#                               if the key exists, otherwise return -1.
# void put(int key, int value)  Update the value of the key if the key 
#                               exists. Otherwise, add the key-value pair 
#                               to the cache. If the number of keys 
#                               exceeds the capacity from this operation, 
#                               evict the least recently used key.
#
# The functions get and put must each run in O(1) average time complexity.

from collections import deque

# Date: 24.01.2025
# Runtime: 3142ms (5%)
# Memory: 78.08MB (74.74%)
#
# Kind of trash, but I didn't want to use linked lists... I'll try better.

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.history = deque()
        return

    def get(self, key: int) -> int:
        if key in self.cache:
            self.history.remove(key)
            self.history.append(key)
        return self.cache.get(key, -1)
    

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)
        if len(self.cache) > self.capacity:
            del self.cache[self.history[0]]
            self.history.popleft()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)