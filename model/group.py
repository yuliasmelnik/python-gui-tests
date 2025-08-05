from sys import maxsize

class Group:

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "%s" % (self.name)