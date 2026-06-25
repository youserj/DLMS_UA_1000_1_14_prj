"""DLMS UA 1000-1 Ed. 14"""
from dataclasses import dataclass
from COSEMpdu.axdr import ChoiceType
from COSEMpdu.data import (
    Array, DoubleLongUnsigned, Integer, Structure, LongUnsigned, CompactArray, 
    DoubleLong, OctetString, Unsigned, VisibleString, Long, Long64Unsigned, Float32, Float64,
    Utf8String, DateTime, Date, Time
)
from COSEMpdu import apdu
from ...types.type_alias import Attr
from . import ver0
from typing import Any
from ...types.implementations import structs
from ..cosem_interface_class import ICAElement, Classifier, update_collection


CaptureObjects = Array[structs.CaptureObjectDefinition]


@dataclass
class EntryDescriptor(Structure):
    """entry_descriptor"""
    from_entry: DoubleLongUnsigned
    to_entry: DoubleLongUnsigned
    from_selected_value: LongUnsigned
    to_selected_value: LongUnsigned


class RangeValue(ChoiceType):
    value: DoubleLong | DoubleLongUnsigned | OctetString | VisibleString | Utf8String | \
            Integer | Unsigned | LongUnsigned | Long | Long64Unsigned | Float32 | Float64 | DateTime | Date | Time


@dataclass
class RangeDescriptor(Structure):
    """range_descriptor"""
    restricting_object: structs.CaptureObjectDefinition
    from_value: RangeValue
    to_value: RangeValue
    selected_values: CaptureObjects


class Buffer(ChoiceType):
    value: Array[Any] | CompactArray


class ParametersType(ChoiceType):
    value: EntryDescriptor | RangeDescriptor


class SelectiveAccessDescriptor(apdu.SelectiveAccessDescriptor): ...


class ProfileGeneric(ver0.ProfileGeneric):
    """4.3.6 Profile generic"""
    VERSION = 1
    A_ELEMENTS = update_collection(
        ver0.ProfileGeneric.A_ELEMENTS,
        ICAElement(2, "buffer", Buffer, classifier=Classifier.DYNAMIC, selective_access=SelectiveAccessDescriptor),
        ICAElement(3, "capture_objects", CaptureObjects),
        ICAElement(6, "sort_object", structs.CaptureObjectDefinition),
        ICAElement(7, "entries_in_use", DoubleLongUnsigned, 0, default=0, classifier=Classifier.DYNAMIC),
        ICAElement(8, "profile_entries", DoubleLongUnsigned, 1, default=1)
    )
    M_ELEMENTS = (
        ver0.ProfileGeneric.getMElement(1),
        ver0.ProfileGeneric.getMElement(2))
    buffer: Attr
    capture_objects: Attr
    sort_method: Attr
    sort_object: Attr
