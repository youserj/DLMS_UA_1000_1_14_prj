from typing import Final
from dataclasses import dataclass
from COSEMpdu.data import OctetString, Array, Unsigned, LongUnsigned, Enum, Structure
from ..cosem_interface_class import ICAuto, ICAElement, Classifier
from ...types.type_alias import Attr
from ...types.implementations import octet_string


class Mode(Enum):
    """mode attribute"""
    NO_AUTO_DIALING: Final = 0
    AUTO_DIALING_ALLOWED_ANYTIME: Final = 1
    AUTO_DIALING_ALLOWED_WITHIN_CALLING_WINDOW: Final = 2
    REGULAR_AUTO_DIALING_ALLOWED_WITHIN_CALLING_WINDOW_ALARM_INITIATED_AUTO_DIALING_ALLOWED_ANYTIME: Final = 3


@dataclass
class WindowElement(Structure):
    """window_element"""
    start_time: octet_string.DateTime
    end_time: octet_string.DateTime


class PhoneNumber(OctetString):
    """phone_number"""


class PSTNAutoDial(ICAuto):
    """5.7.6 PSTN auto dial"""
    CLASS_ID = 29
    VERSION = 0
    A_ELEMENTS = (
        ICAElement(2, "mode", Mode, classifier=Classifier.STATIC),
        ICAElement(3, "repetitions", Unsigned, classifier=Classifier.STATIC),
        ICAElement(4, "repetition_delay", LongUnsigned, classifier=Classifier.STATIC),
        ICAElement(5, "calling_window", Array[WindowElement], classifier=Classifier.STATIC),
        ICAElement(6, "phone_list", Array[PhoneNumber], classifier=Classifier.STATIC)
    )
    mode: Attr
    repetitions: Attr
    repetition_delay: Attr
    calling_window: Attr
    phone_list: Attr
