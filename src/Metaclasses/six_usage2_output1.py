
class myMeta(type):
	pass

class Klass(object, metaclass=MyMeta):
	pass