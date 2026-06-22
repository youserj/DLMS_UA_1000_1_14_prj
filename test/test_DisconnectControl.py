import unittest
from src.DLMS1.types import cdt, cst, ut
from src.DLMS1.cosem_interface_classes import collection, overview
from src.DLMS1 import cosem_interface_classes
from src.DLMS1.exceptions import NeedUpdate, NoObject


class TestType(unittest.TestCase):

    def test_OutputState(self):
        from src.DLMS1.cosem_interface_classes.disconnect_control import OutputState
        value = OutputState(0)
        print(value)
