from functools import wraps


class MyClassDecorator:
    def __init__(self, *a, **kw):
        self.conf_args = a
        self.conf_kw = kw
        # self.func  = None

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('preprocessing')
            print('preprocessing configuration', self.conf_args, self.conf_kw)
            if args:
                if isinstance(args[0], int):
                    a = list(args)
                    a[0] += 5
                    args = tuple(a)
                    print('preprocess OK', args)
            r = func(*args, **kwargs)
            print('postprocessing', r)
            r += 7
            return r

        return wrapper


@MyClassDecorator(1001, a='some configuration')
def my_function(*args, **kwargs):
    print('call my_function', args, kwargs)
    return 3


def main():
    print(my_function())


if __name__ == "__main__":
    main()