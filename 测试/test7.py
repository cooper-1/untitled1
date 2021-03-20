name='sffjsdijfksdhf'
class TestCall(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("self.name: %s. " % self.name, end='   ')
        print("name: %s. " % name, end='   ')
        print('__call__()  is  running ')


if __name__ == '__main__':
    call = TestCall(name='xiaoming')
    call()  # call.__call__()

    call.__call__()


