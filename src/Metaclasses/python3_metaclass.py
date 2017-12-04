
class MyBase (object):
	pass

class MyMeta (type):
	pass

class MyClass (MyBase, metaclass=MyMeta):
	pass