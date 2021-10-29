
"""
class Foo:
    def show(self):
        print("hi")

def add_attribute(self):
    self.z = 9

Test = type('Test', (Foo,), {"x":5, "add_attribute":add_attribute})
t = Test()
#t.wy = "hello"
#print(t.wy)
t.add_attribute()
print(t.z)
"""


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = attrs[name]
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")

d = Dog()
print(d.X)