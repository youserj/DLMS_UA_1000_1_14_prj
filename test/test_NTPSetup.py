import unittest
from src.DLMS1.types import cdt, cst, ut
from src.DLMS1.cosem_interface_classes import collection
from src.DLMS1 import exceptions as exc


class TestType(unittest.TestCase):

    def test_NTPSetup(self):
        obj = collection.NTPSetup("0.0.25.10.0.255")
        obj.set_attr(2, False)
        obj.set_attr(3, bytearray(b'1234'))
        obj.set_attr(5, 0)
        obj.set_attr(6, [(1, bytearray(b'123'))])
        # obj.set_attr(7, False)
        print(obj)
