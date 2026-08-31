from . import ver2

class AssociationLN(ver2.AssociationLN):
    def __init__(self):
        raise ValueError(F"version: {__name__[-1]} of {self.__class__.__name__} not support framework")
