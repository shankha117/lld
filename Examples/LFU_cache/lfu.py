"""
from
https://leetcode.com/problems/lfu-cache/discuss/1123409/Python-remove-from-head-and-add-to-tail-of-DLL
"""

import collections


class LinkedList:

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

    def __str__(self):
        return "{} {}".format(self.key, self.val)


# Every key in the frequency dict is the frequency
# every value is a linkedList with all the nodes having the same frequency as of the key
class DLL:

    def __init__(self):
        self.head = LinkedList("Head", "H")
        self.tail = LinkedList("Tail", "T")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertAtTail(self, key, val):
        temp = LinkedList(key, val)
        tail = self.tail.prev
        tail.next = temp
        temp.prev = tail
        temp.next = self.tail
        self.tail.prev = temp
        self.size += 1
        return temp

    def removeFromHead(self):
        temp = self.head.next
        self.removeNode(temp)
        return temp

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        # del node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = collections.defaultdict(DLL)
        self.cache = dict()
        self.keyToNodemap = dict()
        self.size = 0
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.updatefreq(key, self.cache[key][1])
        return self.cache[key][1]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key not in self.cache:
            if self.size == self.cap:
                """
                1. capacity is now full so we have to remove LFU.
                2. LFU number we have in min_freq so we have to remove from d[min_freq]
                3. First element from d[min_freq] will be removed.
                """
                # print(f"deleting node with min frequency ", self.min_freq)
                temp = self.d[self.min_freq].removeFromHead()
                # print(f"Node deleted --> {0}".format(temp))
                del self.cache[temp.key]
                del self.keyToNodemap[temp.key]

            # inset a new node at the dll
            # 1: <head> <=> <tmp> <=> <tail>
            temp = self.d[1].insertAtTail(key, value)

            self.keyToNodemap[key] = temp
            self.min_freq = 1
            self.cache[key] = (1, value)

            # increase the size of that DLL
            # {1:DLL(self.size = self.size+1,)}
            self.size += 1

        else:

            # if key is already present in the cache ,
            # we will update the new value for the key and
            # update the frequency
            self.updatefreq(key, value)

        # print("cache -->", self.cache)
        # print("keytode -->", self.keyToNodemap)

    def updatefreq(self, key, value):
        """
        Update Freq works in following way:
            1. Retrieve freq and value of key
            2. From keyToLmap dict get address of linkedlist of key
            3. Remove key value from current freq.
            4. Append key to freq+1 list.
        :param value:
        :param key:
        :return:
        """
        prevFreq, _ = self.cache[key]
        currFreq = prevFreq + 1

        # remove the node(self.keyToNodemap[key]) from DLL of freq = prevFreq
        self.d[prevFreq].removeNode(self.keyToNodemap[key])

        # insert the node at the tail as it is the last used node at that frequency
        self.keyToNodemap[key] = self.d[currFreq].insertAtTail(key, value)

        #
        if self.d[self.min_freq].size == 0:

            self.min_freq += 1

        self.cache[key] = (currFreq, value)


def main():
    # Your LRUCache object will be instantiated and called as such:
    obj = LFUCache(3)
    print(obj.get("s"))
    obj.put("s", 1)
    obj.put("s", 3)
    print(obj.get("s"))
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
