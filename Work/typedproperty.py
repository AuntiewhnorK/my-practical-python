"""
Practical Python 7.7 - Closures to Avoid Repetition

Auntiewhnor Kpolie
6/20/2022
"""


def typedproperty(name, expected_type):
    private_name = "_" + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type}")
        setattr(self, private_name, value)

    return prop


# definitions for checking str, int, float types
# orignally was x = lambda name: typedproperty(name, str)
def String(name):
    return typedproperty(name, str)


def Integer(name):
    return typedproperty(name, int)


def Float(name):
    return typedproperty(name, float)
