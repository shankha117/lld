"""
1. we can have a single neuron
2. we can have a neuron layer
3. a neuron can connect to a neuron
4. a neuron can connect to a layer
4. a layer can connect to a layer
5. a layer can connect to a neuron
"""

from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):

        if self == other:
            return None

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    """Abstract class"""

    def __init__(self, name, layer=None):
        self.name = name
        self.inputs = []
        self.outputs = []
        self.layer = None

    def __iter__(self):
        yield self

    def __str__(self):
        return f"Neuron {self.name} with {len(self.inputs)} inputs and  {len(self.outputs)} outputs"


class Layer(list, Connectable):

    def __init__(self, name):
        super(Layer, self).__init__()
        self.name = name

    def generate_and_add_neurons(self, neuron_count):
        for n in range(neuron_count):
            self.append(Neuron(f'{self.name}-{n}', layer=self.name))

    def add_neurons(self, neurons):
        for n in neurons:
            n.layer = self.name
            self.append(n)

    def __str__(self):
        return f"Layer {self.name} with {len(self)} neurons"


if __name__ == "__main__":
    n1 = Neuron('n1')
    n2 = Neuron('n2')
    n3 = Neuron('n3')
    l1 = Layer('l1')
    l1.generate_and_add_neurons(neuron_count=3)
    l2 = Layer('l2')
    l2.generate_and_add_neurons(neuron_count=4)

    n1.connect_to(l1)

    l1.connect_to(n2)

    n2.connect_to(l2)

    l2.connect_to(n3)

    print(n1)
    print(n2)
    print(n3)
    print(l1)
    print(l2)
