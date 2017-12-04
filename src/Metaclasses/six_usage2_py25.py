
class MyMeta(type):
    pass

class MyKlass(object):
    pass
    
MyKlass = add_metaclass(MyMeta)(MyKlass)