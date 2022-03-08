from abc import ABCMeta, abstractmethod
from collections import deque
from enum import Enum


class Rank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2


class CallState(Enum):
    NOT_STARTED = -1
    IN_PROGRESS = 0
    COMPLETE = 1
    QUEUED = 2


class Call(object):

    def __init__(self, call_id, seviority):
        self.state = CallState.NOT_STARTED
        self.id = call_id
        self.handeled_by = None
        self.seviority = seviority


class CallHandler(metaclass=ABCMeta):  # Abstract handler
    """Abstract Handler"""

    def __init__(self, successors, call_center, id, rank):
        self._successors = successors
        self.call_center = call_center
        self.id = id
        self.rank = rank

    def handle(self, call: Call):
        handled = self._handle(call)  # If handled, stop here

        if not handled:
            for s in self._successors:
                if s.handle(call):
                    return True
        else:
            return True

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')


class Operator(CallHandler):  # Inherits from the abstract handler
    """Operator"""
    MAX_SEVIORITY = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _handle(self, call: Call):
        if call.seviority <= self.MAX_SEVIORITY:  # Provide a condition for handling
            print("{} handled in Operator ".format(call.id))
            call.state = CallState.COMPLETE
            return True  # Indicates that the request has been handled


class Supervisor(CallHandler):  # Inherits from the abstract handler
    """Supervisor"""
    MAX_SEVIORITY = 60

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _handle(self, call: Call):
        if call.seviority <= self.MAX_SEVIORITY:  # Provide a condition for handling
            print("{} handled in Supervisor ".format(call.id))
            call.state = CallState.COMPLETE
            return True  # Indicates that the request has been handled


class DefaultHandler(CallHandler):  # Inherits from the abstract handler
    """Supervisor"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _handle(self, call: Call):
        print("Default Handler pushing the file to queue")
        call.state = CallState.QUEUED
        self.call_center.queue.append(call)
        return True


class Call_Center(object):

    def __init__(self, name):
        self.supervisors = []
        self.operators = []
        self.queue = deque()
        self.name = name
        self.total_calls = 0

    def add_supervisors(self, supervisor):
        self.supervisors.append(supervisor)

    def add_operators(self, operator):
        self.operators.append(operator)

    def make_a_call(self, call_seviority):
        self.total_calls += 1
        call = Call(call_id=self.total_calls, seviority=call_seviority)

        # always make a call to operator
        # if len(self.operators) == 0:
        #     raise Exception("No operators Available in call center !")

        for op in self.operators:
            op.handle(call)
            if call.state == CallState.COMPLETE:
                print(f"{call.id} is completed")
            elif call.state == CallState.QUEUED:
                print(f"{call.id} is queued")
            else:
                print(f"{call.id} is Not Handled")
            return


def main():
    c = Call_Center(name="MyCallCenter")
    d = DefaultHandler(call_center=c, id=0, rank=Rank.DIRECTOR, successors=[])
    s1 = Supervisor(call_center=c, id=1, rank=Rank.SUPERVISOR, successors=[d])
    s2 = Supervisor(call_center=c, id=2, rank=Rank.SUPERVISOR, successors=[d])

    c.add_supervisors(s1)
    c.add_supervisors(s2)

    op1 = Operator(call_center=c, id=3, rank=Rank.OPERATOR, successors=[s1, s2])
    op2 = Operator(call_center=c, id=4, rank=Rank.OPERATOR, successors=[s1, s2])

    c.add_operators(op1)
    c.add_operators(op2)

    calls = [34, 52, 67, 45, 35, 66, 22, 56, 77, 23]

    for call in calls:
        c.make_a_call(call)


if __name__ == "__main__":
    main()
