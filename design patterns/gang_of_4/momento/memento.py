"""
 In the case of database applications, rollback is an essential option because irreversible changes can do humongous damage to both your tasks at hand, and future objectives.
 If you're looking for a design solution, to this type of programming need, memento is a perfect behavioral design pattern for you.
 This pattern allows you to capture the internal state of an object at a certain point in time, and to restore that same state later in the future if necessary


"""

import pickle


class Originator:

    def __init__(self):
        self._state = None

    def create_memento(self):
        return pickle.dumps(vars(self))

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear
        vars(self).update(previous_state)


def main():
    originator = Originator()

    print(vars(originator))

    memento = originator.create_memento()

    originator._state = True

    print(vars(originator))

    originator.set_memento(memento)

    print(vars(originator))


if __name__ == "__main__":
    main()
