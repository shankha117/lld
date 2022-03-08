from functools import wraps
import inspect


class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


def validate_key(func):
    @wraps(func)
    def inner(*args, **kwargs):
        key = dict(zip(inspect.getfullargspec(func)[0], args))['key']
        if type(key) != int:
            raise ValueError("Key must be an Integer")
        return func(*args, **kwargs)

    return inner


# def star(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print(dict(zip(inspect.getfullargspec(func)[0], args)))
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    @validate_key
    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                print(f"{key} set with {value}")
                return
        self.table[hash_index].append(Item(key, value))
        print(f"{key} set with {value}")

    @validate_key
    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    @validate_key
    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Key not found')


# ht = HashTable(5)
#
# ht.set(1, "shankha")
# ht.set(2, "shuvro")
# ht.set(3, "sinha")
# print(ht.get(1))
# print(ht.get(3))
# ht.set(3, "python")
# print(ht.get("3"))
# print(ht.remove(3))
# print(ht.get(3))
