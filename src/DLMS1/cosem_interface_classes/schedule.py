from dataclasses import dataclass
from COSEMpdu.data import Boolean, LongUnsigned, Structure, BitString, Array
from .cosem_interface_class import ICAuto, ICAElement, ICMElement
from ..types.implementations import octet_string
from ..types.type_alias import Attr


@dataclass
class ScheduleTableEntry(Structure):
    """schedule_table_entry"""
    index: LongUnsigned
    enable: Boolean
    script_logical_name: octet_string.LN
    script_selector: LongUnsigned
    switch_time: octet_string.Time
    validity_window: LongUnsigned
    exec_weekdays: BitString
    exec_specdays: BitString
    begin_date: octet_string.Date
    end_date: octet_string.Date


Entries = Array[ScheduleTableEntry]
"""entries attribute"""


@dataclass
class DataED(Structure):
    """ enable/disable"""
    firstIndexA: LongUnsigned
    lastIndexA: LongUnsigned
    firstIndexB: LongUnsigned
    lastIndexB: LongUnsigned


@dataclass
class DataDelete(Structure):
    """delete"""
    firstIndex: LongUnsigned
    lastIndex: LongUnsigned


class Schedule(ICAuto):
    """4.5.3 Schedule"""
    CLASS_ID = 10
    VERSION = 0
    A_ELEMENTS = ICAElement(2, "entries", Entries),
    M_ELEMENTS = (
        ICMElement(1, "enable_disable", DataED),
        ICMElement(2, "insert", ScheduleTableEntry),
        ICMElement(3, "delete", DataDelete))
    entries: Attr
