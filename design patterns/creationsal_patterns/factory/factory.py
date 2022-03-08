" Imagine you have a pet shop and now you need to sell dogs too "
" The system needs to be able to handle cats as well as dogs"
" The system suppose to show how each of the pets speak"


class Dog:
    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:
    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """The factory method"""

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]


def main():
    # client is the user is the get_pet method

    d = get_pet("dog")

    print(d.speak())

    c = get_pet("cat")

    print(c.speak())


if __name__ == "__main__":
    main()
