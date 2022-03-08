"""
 An object-oriented way of providing global variables is Singleton.
 Singleton is the pattern you need when you'd like to allow only one object to be instantiated from a class.

"""


class Borg:
    """Borg pattern making the class attributes global"""
    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""

    # This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        super().__init__()
        self._shared_data.update(kwargs)  # Update the attribute dictionary by inserting a new key-value pair

    def __str__(self):
        return str(self._shared_data)  # Returns the attribute dictionary for printing


def main():
    # Let's create a singleton object and add our first acronym
    x = Singleton(HTTP="Hyper Text Transfer Protocol")
    # Print the object
    print(x)

    # Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
    y = Singleton(SNMP="Simple Network Management Protocol")
    # Print the object
    print(y)


if __name__ == "__main__":
    main()
