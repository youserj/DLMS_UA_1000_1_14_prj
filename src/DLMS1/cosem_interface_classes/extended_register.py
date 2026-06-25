from COSEMpdu.axdr import ChoiceType
from COSEMpdu.data import NullData, BitString, DoubleLongUnsigned, OctetString, VisibleString, Utf8String, Unsigned, LongUnsigned, Long64Unsigned
from . import register
from ..types.type_alias import Attr
from ..types.implementations import octet_string
from .cosem_interface_class import ICAElement, Classifier, update_collection


class StatusData(ChoiceType):
    """value"""
    value: NullData | BitString | DoubleLongUnsigned | OctetString | VisibleString | Utf8String | Unsigned | LongUnsigned | Long64Unsigned


class ExtendedRegister(register.Register):
    """4.3.3 Extended register"""
    CLASS_ID = 4
    VERSION = 0
    A_ELEMENTS = update_collection(
        register.Register.A_ELEMENTS,
        ICAElement(4, "status", StatusData, classifier=Classifier.DYNAMIC),
        ICAElement(5, "capture_time", octet_string.DateTime, classifier=Classifier.DYNAMIC))
    M_ELEMENTS = register.Register.getMElement(1),
    status: Attr
    capture_time: Attr
