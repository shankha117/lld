"""
 Our given problem is that many different types of processing needs to be done depending on what the request is.
 In our scenario, we receive an integer value and then we use different handlers to find out its range.

 As our solution, we used Abstract Handler that stores a Successor who will handle a request if it is not handled at the current handler.
 then Concrete Handlers check if they can handle the request.

 If they can, they handle it and return a true value indicating that the request was handled.

 Composite is related to the Chain of Responsibility design pattern.

"""


class Handler:  # Abstract handler
    """Abstract Handler"""

    def __init__(self, successor):
        self._successor = successor  # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request)  # If handled, stop here

        # Otherwise, keep going
        if not handled:
            print(f"{self.name} could not handle  {request}, so delegating")
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')


class ConcreteHandler1(Handler):  # Inherits from the abstract handler
    """Concrete handler 1"""

    def __init__(self, *args, **kwargs):
        self.name = "ConcreteHandler1"
        super().__init__(*args, **kwargs)

    def _handle(self, request):
        if 0 < request <= 10:  # Provide a condition for handling
            print("Request {} handled in handler 1".format(request))
            return True  # Indicates that the request has been handled


class ConcreteHandler2(Handler):  # Inherits from the abstract handler
    """Concrete handler 2"""

    def __init__(self, *args, **kwargs):
        self.name = "ConcreteHandler2"
        super().__init__(*args, **kwargs)

    def _handle(self, request):
        if 10 < request <= 30:  # Provide a condition for handling
            print("Request {} handled in handler 2".format(request))
            return True  # Indicates that the request has been handled


class DefaultHandler(Handler):  # Inherits from the abstract handler
    """Default handler"""

    def __init__(self, *args, **kwargs):
        self.name = "DefaultHandler"
        super().__init__(*args, **kwargs)

    def _handle(self, request):
        """If there is no handler available"""
        # No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True  # Indicates that the request has been handled


class Client:  # Using handlers
    def __init__(self):
        self.handler = ConcreteHandler1(
            ConcreteHandler2(DefaultHandler(None)))  # Create handlers and use them in a sequence you want
        # Note that the default handler has no successor

    def delegate(self, requests):  # Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


def main():
    # Create a client
    c = Client()

    # Create requests
    requests = [2, 5, 30, 55]

    # Send the requests
    c.delegate(requests)


if __name__ == "__main__":
    main()
