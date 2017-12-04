import six

class _TemplateMetaclass(type):

    pattern = r"""
    %(delim)s(?:
      (?P<escaped>%(delim)s) |  
      (?P<named>%(id)s)      | 
      {(?P<braced>%(id)s)}   | 
      (?P<invalid>)            
    )
    """

    def __init__(cls, name, bases, dct):
        super(_TemplateMetaclass, cls).__init__(name, bases, dct)
        if 'pattern' in dct:
            pattern = cls.pattern
        else:
            pattern = _TemplateMetaclass.pattern % {
                'delim' : _re.escape(cls.delimiter),
                'id'    : cls.idpattern,
                }
        cls.pattern = _re.compile(pattern, _re.IGNORECASE | _re.VERBOSE)

@add_metaclass(_TemplateMetaclass)
class Template(object):

    delimiter = '$'
    idpattern = r'[_a-z][_a-z0-9]*'

    def __init__(self, template):
        self.template = template