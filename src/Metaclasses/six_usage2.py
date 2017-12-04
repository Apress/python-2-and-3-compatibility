
class MyMeta(type):
	pass

@add_metaclass(MyMeta)
class Klass(object):
	pass