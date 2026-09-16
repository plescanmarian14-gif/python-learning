from contextlib import contextmanager
@contextmanager
def usa():
    print("Deschide usa!")
    yield
    print("Inchide usa!")

with(usa()):
    print("Sunt aici!")