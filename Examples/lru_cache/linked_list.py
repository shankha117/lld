class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val

        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity

        self.cache = {}

        # left -> # LRU , Right -> #MRU
        self.left, self.right = Node(0, 0), Node(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:

        if key in self.cache:
            # remove from the list
            self.remove(self.cache[key])

            # insert at the right of the list
            self.insert(self.cache[key])

            # update most recent
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        # add a new node into the cache
        self.cache[key] = Node(key, value)

        # insert the new node into the list
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove the LRU Node
            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]

    # insert at right
    def insert(self, node):

        prev, nxt = self.right.prev, self.right

        prev.next = nxt.prev = node

        node.prev, node.next = prev, nxt

    # remove from the list
    def remove(self, node):

        prev, nxt = node.prev, node.next

        prev.next, nxt.prev = nxt, prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(4)
    print(obj.get("s"))
    obj.put("s", 1)
    obj.put("s", 2)
    print(obj.get("s"))
    obj.put("m", 5)
    obj.put("n", 7)
    obj.put("q", 9)
    obj.put("j", 9)
    print(obj.get("m"))
    print(obj.get("n"))
    print(obj.get("s"))


if __name__ == "__main__":
    main()
