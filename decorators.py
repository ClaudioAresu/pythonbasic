def func(f):
    def wrapper(*args, **kwargs):
        print("started")
        rv = f(*args, **kwargs)
        print("ended")
        return rv
    
    return wrapper

def func2():
    print("I am func2")


@func
def func3(x, y):
    print(x, y)

x = func3(5, 6)
print(x)