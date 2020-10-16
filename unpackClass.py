

class Person(dict):
    __personid = ''
    __personname = ''

    def __init__(self):
        self.__class_name = self.__class__.__name__
    @property
    def personid(self):
        return self.__personid

    @personid.setter
    def personid(self, v):
        self.__personid = v

    def keys(self):
        return [k for k, v in globals()[self.__class_name].__dict__.items() 
            if isinstance(v, property)]

    def values(self):
        return [self.__getitem__(k) for k in self.keys()]

    def items(self):
        return [(k, self.__getitem__(k)) for k in self.keys()]

    def __getitem__(self, key):
        return getattr(self, key)

    def __contains__(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            return False
        except Exception as err:
            raise Exception(err)

def foo(**k):
    print k


a = Person()
a.personid = 'name'
print a.values()
print a.items()
print 'personid' in a
print a