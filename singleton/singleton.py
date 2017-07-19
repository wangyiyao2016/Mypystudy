import threading


class Singleton(object):
    """
    A class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated
        self.lock = threading.Lock()

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self.lock.acquire()
            try:
                return self._instance
            except AttributeError:
                self._instance = self._decorated()
                return self._instance
            finally:
                self.lock.release()

    def __call__(self):
        print('Singletons should be accessed through `Instance()`.')
        return MySingletonClass.Instance()

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class MySingletonClass(object):
    pass


s0 = MySingletonClass()

s1 = MySingletonClass.Instance()
s2 = MySingletonClass.Instance()

print(s0 is s1)
print(s0 is s2)
print(s1 is s2)
print(isinstance(s0, MySingletonClass))
