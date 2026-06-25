import unittest
from src.DLMS1.types import cdt, cst, ut
from src.DLMS1.types.implementations import octet_string
from src.DLMS1.cosem_interface_classes import collection, overview
from src.DLMS1.cosem_interface_classes import implementations as impl


class TestType(unittest.TestCase):

    def test_set(self):
        t = collection.get_type(
            c_id=7,
            version=1,
            ln=octet_string.LN.from_obis("1.0.94.7.4.255"),
            func_map=collection.func_maps["KPZ"]
        )
        print(t)
        obj = t(octet_string.LN.from_obis("1.0.94.7.4.255"))
        obj.set_attr(index=2, value=b'\x01\x00')
