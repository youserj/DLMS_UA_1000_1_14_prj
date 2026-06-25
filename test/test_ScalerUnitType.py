import unittest
from COSEMpdu.byte_buffer import ByteBuffer
from src.DLMS1.cosem_interface_classes.register import ScalUnitType, Integer, Unit


class TestType(unittest.TestCase):

    def test_ScalerUnitType(self) -> None:
        su = ScalUnitType(Integer(0), Unit(27))
        buf = ByteBuffer.allocate(10)
        res = su.put(buf)
        print(su)
