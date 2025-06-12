Today's Problem is-

Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:

PUT x y: sets the value of the key x with value y
GET x: gets the value of key x if present else returns -1.
The LRUCache class has two methods get() and put() which are defined as follows.

get(key): returns the value of the key if it already exists in the cache otherwise returns -1.
put(key, value): if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should remove the least recently used item before inserting the new item.
In the constructor of the class the capacity of the cache should be initialized.
Examples:

Input: cap = 2, Q = 2, Queries = [["PUT", 1, 2], ["GET", 1]]
Output: [2]
Explanation: Cache Size = 2
["PUT", 1, 2] will insert the key-value pair (1, 2) in the cache,
["GET", 1] will print the value corresponding to Key 1, ie 2.
Input: cap = 2, Q = 8, Queries = [["PUT", 1, 2], ["PUT", 2, 3], ["PUT", 1, 5], ["PUT", 4, 5], ["PUT", 6, 7], ["GET", 4], ["PUT", 1, 2], ["GET", 3]]
Output: [5, -1]
Explanation: Cache Size = 2
["PUT", 1, 2] will insert the pair (1,2) in the cache.
["PUT", 2, 3] will insert the pair (2,3) in the cache: 1->2, 2->3(the most recently used one is kept at the rightmost position) 
["PUT", 1, 5] will replace the value of 1 from 2 to 5 : 2 -> 3, 1 -> 5
["PUT", 4, 5] : 1 -> 5, 4 -> 5 (Cache size is 2, hence we delete the least recently used key-value pair)
["PUT", 6, 7] : 4 -> 5, 6 -> 7 
["GET", 4] : Prints 5 (The cache now looks like 6 -> 7, 4->5)
["PUT", 1, 2] : 4 -> 5, 1 -> 2  (Cache size is 2, hence we delete the least recently used key-value pair)
["GET", 3] : No key value pair having key = 3. Hence, -1 is printed.
Constraints:
1 <= cap <= 103
1 <= Q <= 105
1 <= x, y <= 104

Solution

Code-
# design the class in the most optimal way
class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev =  None
            self.next = None
    def __init__(self, cap):
        self.capacity = cap
        self.cache = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    def _add(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            del self.cache[key]
        if len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            del self.cache[lru_node.key]
            self._remove(lru_node)
        newNode = self.Node(key, value)
        self._add(newNode)
        self.cache[key] = newNode
