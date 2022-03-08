import traceback


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.Size = 0

    def isEmpty(self):
        if self.Size == 0:
            return True
        return False

    def dequeLength(self):
        return self.Size

    def appendleft(self, data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
        else:
            temp.next = self.front
            self.front = temp
        self.Size += 1

    def append(self, data):
        temp = Node(data)
        if self.front == None:
            self.front = temp
            self.Size = self.Size + 1
        else:
            curr = self.front
            while curr.next != None:
                curr = curr.next
            curr.next = temp
            self.Size = self.Size + 1

    def popleft(self):
        try:

            if self.Size == 0:
                raise Exception("Deque is Empty")
            else:
                temp = self.front
                self.front = self.front.next
                self.Size = self.Size - 1
                return temp.data

        except Exception as e:
            print(traceback.format_exc())
            print(str(e))

    def print_list(self):
        print("\n--")
        cur = self.front
        while cur:
            print(cur.data, end="--")
            cur = cur.next

    def remove(self, data):
        try:

            if self.front.data == data:
                self.front = self.front.next
                self.Size -= 1
                return

            cur = self.front.next
            prev = self.front
            while cur is not None:
                if cur.data == data:
                    prev.next = cur.next
                prev = cur
                cur = cur.next



        except Exception as e:
            print(traceback.format_exc())
            print(str(e))


class Cache(object):

    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.size = 0
        self.lookup = {}
        self.queue = Deque()

    def get(self, key):
        """Get the stored query result from the cache.
        Accessing a node updates its position to the front of the LRU list.
        """
        node = self.lookup.get(key)
        if node is not None:
            self.queue.remove(data=key)
            self.queue.append(data=key)
            return node
        else:
            return None

    def update(self, key: int, value: int):
        if self.get(key):
            self.lookup[key] = value
        else:
            raise KeyError("Key Not Found !")

    def put(self, key: int, value: int) -> None:

        if self.lookup.get(key, None):
            self.update(key, value)

        elif self.queue.dequeLength() < self.MAX_SIZE:
            self.queue.append(key)
            self.lookup[key] = value

        else:
            popped = self.queue.popleft()
            self.queue.append(key)
            self.lookup[key] = value
            self.lookup[popped] = None


def main():
    # Your LRUCache object will be instantiated and called as such:
    obj = Cache(4)
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
