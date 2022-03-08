"""
Builder is a solution to an Anti-Pattern called Telescoping Constructor.
An Anti-Pattern is the opposite of the best practice.
The Telescoping Constructor Anti-Pattern occurs when a software developer attempts to build a complex object using an excessive number of constructors.
The Builder pattern is trying to solve this problem. Think of a scenario, in which you're trying to build a car.
This requires various car parts to be first constructed individually and then assembled.
The Builder pattern brings an order to this chaotic process to remove this unnecessary complexity in building a complex object.

"""


class Director():
    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        for parts in self._builder.parts_to_add():
            # getattr(self._builder, parts)()
            parts()

    def get_car(self):
        return self._builder.car


class Builder():
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class TeslaBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """

    def parts_to_add(self):
        # return ["add_tires", "add_screen", "add_model", "add_tires"]

        return [self.add_model, self.add_screen, self.add_tires, self.add_engine]

    def add_screen(self):
        self.car.screen = "Oled"

    def add_model(self):
        self.car.model = "Tesla"

    def add_tires(self):
        self.car.tires = "Automatic tires"

    def add_engine(self):
        self.car.engine = "Efficient engine"


class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """

    def parts_to_add(self):
        # return ["add_tires", "add_model", "add_tires"]
        return [self.add_model, self.add_tires, self.add_engine]

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


from json import dumps


class Car():
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return dumps(self.__dict__)


def main():
    # builder = SkyLarkBuilder()
    # the client will use the Director and pass the Concrete implementation of the CarBuilder

    director = Director(SkyLarkBuilder())
    director.construct_car()
    car = director.get_car()
    print(car)

    director = Director(TeslaBuilder())
    director.construct_car()
    car = director.get_car()
    print(car)


if __name__ == "__main__":
    main()

"""
 This is helpful especially because it makes the process of creating similar objects much, much easier and cleaner. 
 All you have to do is simply add another Concrete Builder. EX: TeslaBuilder()
 For example, we could add another type of car.

"""
