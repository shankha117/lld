import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """
            Clone a registered object and update its attributes
            we also need to have the update method if some attributes are changing
        """

        # print(attr)
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        # print(id(self._objects.get(name)), id(obj))
        # print(obj.__dict__)
        return obj


class Car:
    def __init__(self, name, color, options):
        self.name = name
        self.color = color
        self.options = options

    def __str__(self):
        return '{} | {} | {} | {}'.format(self.name, self.color, self.options, id(self))


def main():
    skyv1 = Car(**{'name': 'Skylark', 'color': 'Red', 'options': 'Ex'})
    prototype = Prototype()
    prototype.register_object('skylark', skyv1)

    c1 = prototype.clone('skylark')

    print(c1)

    c2 = prototype.clone('skylark')

    print(c2)

    skyv2 = Car(**{'name': 'Skylark', 'color': 'black', 'options': 'Ex'})
    prototype.register_object('skylark', skyv2)

    c3 = prototype.clone('skylark')

    print(c3)


if __name__ == "__main__":
    main()
