class Base:
    X = 1

    def foo(self):
        return 1

    def bar(self):
        self.x = 1


class Short(Base):
    """Simple class."""

    X = 2

    def __init__(self, z):
        self.z = z

    def add(self, x , y):
        return x + y

    def add_two(self, x):
        return self.add(x, 2)

    def add_etc(self, x):
        return x + ' etc.'
    
