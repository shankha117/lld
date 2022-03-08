class SingletonMeta(type):
    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            self._instance[self] = super(SingletonMeta, self).__call__(*args, **kwargs)

        return self._instance[self]


# MyClass will be my singleton class
class MyClass(metaclass=SingletonMeta):
    pass


def main():
    m1 = MyClass()
    print(f"id of first Myclass object  {id(m1)}")

    m2 = MyClass()
    print(f"id of second Myclass object {id(m2)}")

    print("both are smae , class is instantiated only once")


if __name__ == "__main__":
    main()
