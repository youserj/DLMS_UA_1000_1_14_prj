import unittest
from src.DLMS1.types import cdt, cst, ut
from src.DLMS1.cosem_interface_classes import collection, overview


class TestType(unittest.TestCase):

    def test_Data(self):
        obj = collection.impl.profile_generic.SPODES3DisplayReadout("0.0.21.0.1.255")
        print(obj)