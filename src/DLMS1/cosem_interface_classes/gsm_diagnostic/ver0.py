from typing import Final
import logging
from ...config_parser import get_message
from dataclasses import dataclass
from COSEMpdu.data import Enum, Array, Structure, VisibleString, DateTime, Unsigned, LongUnsigned
from ...types import cdt
from ..cosem_interface_class import ICAuto, ICAElement, Classifier
from ...types.type_alias import Attr


class Status(Enum):
    """status"""
    NOT_REGISTERED: Final[int] = 0
    REGISTERED_HOME: Final[int] = 1
    NOT_REGISTERED_SEARCHING: Final[int] = 2
    REGISTRATION_DENIED: Final[int] = 3
    UNKNOWN: Final[int] = 4
    REGISTERED_ROAMING: Final[int] = 5


class CSAttachment(Enum):
    """cs_attachment"""
    INACTIVE: Final[int] = 0
    INCOMING_CALL: Final[int] = 1
    ACTIVE: Final[int] = 2


class PSStatus(Enum):
    """ps_status"""
    INACTIVE: Final[int] = 0
    GPRS: Final[int] = 1
    EDGE: Final[int] = 2
    UMTS: Final[int] = 3
    HSPDA: Final[int] = 4


class SignalQuality(Unsigned):
    """signal_quality"""
    _113_DBM_OR_LESS: Final[int] = 0
    _111_DBM: Final[int] = 1
    _109_DBM: Final[int] = 2
    _107_DBM: Final[int] = 3
    _105_DBM: Final[int] = 4
    _103_DBM: Final[int] = 5
    _101_DBM: Final[int] = 6
    _99_DBM: Final[int] = 7
    _97_DBM: Final[int] = 8
    _95_DBM: Final[int] = 9
    _93_DBM: Final[int] = 10
    _91_DBM: Final[int] = 11
    _89_DBM: Final[int] = 12
    _87_DBM: Final[int] = 13
    _85_DBM: Final[int] = 14
    _83_DBM: Final[int] = 15
    _81_DBM: Final[int] = 16
    _79_DBM: Final[int] = 17
    _77_DBM: Final[int] = 18
    _75_DBM: Final[int] = 19
    _73_DBM: Final[int] = 20
    _71_DBM: Final[int] = 21
    _69_DBM: Final[int] = 22
    _67_DBM: Final[int] = 23
    _65_DBM: Final[int] = 24
    _63_DBM: Final[int] = 25
    _61_DBM: Final[int] = 26
    _59_DBM: Final[int] = 27
    _57_DBM: Final[int] = 28
    _55_DBM: Final[int] = 29
    _53_DBM: Final[int] = 30
    _51_OR_GREATER: Final[int] = 31
    NOT_KNOWN_OR_NOT_DETECTABLE: Final[int] = 99

    def get_report(self) -> cdt.Report:
        val = int(self)
        if val == 0:
            return cdt.Report(get_message(F"({val}) –113 dBm $or$ $less$(0)"))
        if val == 1:
            return cdt.Report(F"({val}) –111 dBm")
        if val < 31:
            return cdt.Report(get_message(F"({val}) {-109 + (val - 2) * 2} dBm"))
        if val == 31:
            return cdt.Report(get_message(F"({val}) –51 dBm $or$ $greater$"))
        if val == 99:
            return cdt.Report(get_message(F"({val}) $not_known_or_not_detectable$"))
        return cdt.Report(
            msg=F"({val})",
            log=cdt.Log(logging.WARN, "unknown value"))


@dataclass
class CellInfoType(Structure):
    """cell_info_type"""
    cell_ID: LongUnsigned
    location_ID: LongUnsigned
    signal_quality: SignalQuality
    ber: Unsigned


@dataclass
class AdjacentCellInfo(Structure):
    """adjacent_cell_info"""
    cell_ID: LongUnsigned
    signal_quality: SignalQuality


class GSMDiagnostic(ICAuto):
    """4.7.8 GSM diagnostic"""
    CLASS_ID = 47
    VERSION = 0
    A_ELEMENTS = (
        ICAElement(2, "operator", VisibleString, classifier=Classifier.DYNAMIC),
        ICAElement(3, "status", Status, 0, 255, 0, classifier=Classifier.DYNAMIC),
        ICAElement(4, "cs_attachment", CSAttachment, 0, 255, 0, classifier=Classifier.DYNAMIC),
        ICAElement(5, "ps_status", PSStatus, 0, 255, 0, classifier=Classifier.DYNAMIC),
        ICAElement(6, "cell_info", CellInfoType, classifier=Classifier.DYNAMIC),
        ICAElement(7, "adjacent_cell", Array[AdjacentCellInfo], classifier=Classifier.DYNAMIC),
        ICAElement(8, "capture_time", DateTime, classifier=Classifier.DYNAMIC))
    operator: Attr
    status: Attr
    cs_attachment: Attr
    ps_status: Attr
    cell_info: Attr
    adjacent_cell: Attr
    capture_time: Attr
