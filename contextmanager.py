import contextlib



@contextlib.contextmanager
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()
    print("exit")

with file("oro.txt", "w") as dale:
    print("middle")
    dale.write("hello")