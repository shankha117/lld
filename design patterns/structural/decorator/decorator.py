import functools

# Try the various combinations below!
user = {'username': 'joe123', 'access_level': 'admin'}
# user = {'username': 'bob', 'access_level': 'admin'}
# user = {'username': 'joe123', 'access_level': 'user'}
# user = {'username': 'bob', 'access_level': 'user'}


def user_name_starts_with_j(func):
    """
    This decorator only runs the function passed if the user's username starts with a j.
    """

    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('username').startswith('j'):
            return func(*args, **kwargs)
        else:
            print("User's username did not start with 'j'.")

    return secure_func


def user_has_permission(func):
    """
    This decorator only runs the function passed if the user's access_level is admin.
    """

    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
        else:
            print("User's access_level was not 'admin'.")

    return secure_func


@user_has_permission
@user_name_starts_with_j
def double_decorator():
    return 'I ran.'


"""
When `double_decorator()` runs, this chain of "functions" runs:

#### user_has_permission -> user_name_starts_with_j -> double_decorator

That is because `user_name_starts_with_j` is the first decorator to be applied. It replaces `double_decorator` by the function it returns.
Then, `user_has_permission` is applied—and it replaces the function the other decorator returned by the function it returns.
"""


def main():
    print(double_decorator())


if __name__ == "__main__":
    main()
