from collections import deque, defaultdict


class LRUCache:

    def __init__(self, capacity: int):

        self.MX_SIZE = capacity
        self.CUR_SIZE = 0
        self.cache = defaultdict(lambda: None)
        self.queue = deque()

    def get(self, key: int) -> int:

        if self.cache[key] != None:

            self.queue.remove(key)
            self.queue.append(key)
            return f"returning {self.cache[key]}"
        else:
            return f"returning -1"

    def update(self, key: int, value: int):
        self.get(key)
        self.cache[key] = value

    def put(self, key: int, value: int) -> None:

        if self.cache[key] != None:
            self.update(key, value)

        elif self.CUR_SIZE < self.MX_SIZE:
            self.queue.append(key)
            self.CUR_SIZE += 1
            self.cache[key] = value

        else:
            popped = self.queue.popleft()
            self.queue.append(key)
            self.cache[key] = value
            self.cache[popped] = None


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
