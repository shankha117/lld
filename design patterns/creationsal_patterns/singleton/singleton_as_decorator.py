from functools import wraps


def singleton(func):
    instances = {}
    "stored the class object in the instance"

    @wraps(func)
    def getinstance(*args, **kwargs):
        if func not in instances:
            instances[func] = func(*args, **kwargs)
        return instances[func]

    return getinstance


@singleton
class MyClass():
    pass

def main():
    m1 = MyClass()
    print(f"id of first Myclass object  {id(m1)}")

    m2 = MyClass()
    print(f"id of second Myclass object {id(m2)}")

    print("both are smae , class is instantiated only once")


if __name__ == "__main__":
    main()
