
class MyBase (object):
	pass

class MyMeta (type):
	pass

class MyClass (MyBase):
	__metaclass__ =  MyMeta
	pass