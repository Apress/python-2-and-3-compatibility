class myMeta(type):
	pass

class Klass(object):
	__metaclass__=  MyMeta
	pass