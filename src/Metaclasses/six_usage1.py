
from six import with_metaclass

class MyMeta(type):
    pass

class MyBase(object):
    pass

class MyClass(with_metaclass(MyMeta, MyBase)):
    pass