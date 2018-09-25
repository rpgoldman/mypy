from typing import Any

class SuperClass:
    def example_method(self, *args: Any, **kwargs: Any) -> float: ...
    # in the *real* code, this is used to delegate any call to
    # example_method that is *not* handled by a subclass to another
    # method:
    # def example_method(self, *args, **kwargs):
    #     return self.backstop(*args, **kwargs)
    def backstop(self, *args: Any, **kwargs: Any) -> float: ...

class SubClass(SuperClass):
    def example_method(self, x) -> float: ...
