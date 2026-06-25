from dataclasses import dataclass
from COSEMpdu.data import Array, Structure, Boolean, LongUnsigned, Data
from ..types.implementations import structs, double_long_usingneds, octet_string
from .cosem_interface_class import ICAElement, ICAuto, Classifier
from ..types.type_alias import Attr


@dataclass
class EmergencyProfileType(Structure):
    """emergency_profile"""
    emergency_profile_id: LongUnsigned
    emergency_activation_time: octet_string.DateTime
    emergency_duration: double_long_usingneds.DoubleLongUnsignedSecond


EmergencyProfileGroupIdList = Array[LongUnsigned]
"""emergency_profile_group_id_list"""


@dataclass
class Action(Structure):
    """action"""
    action_over_threshold: structs.ActionItem
    action_under_threshold: structs.ActionItem


class Limiter(ICAuto):
    """4.5.9 Limiter"""
    CLASS_ID = 71
    VERSION = 0
    A_ELEMENTS = (
        ICAElement(2, "monitored_value", structs.ValueDefinition),
        ICAElement(3, "threshold_active", Data, classifier=Classifier.DYNAMIC),
        ICAElement(4, "threshold_normal", Data),
        ICAElement(5, "threshold_emergency", Data),
        ICAElement(6, "min_over_threshold_duration", double_long_usingneds.DoubleLongUnsignedSecond),
        ICAElement(7, "min_under_threshold_duration", double_long_usingneds.DoubleLongUnsignedSecond),
        ICAElement(8, "emergency_profile", EmergencyProfileType),
        ICAElement(9, "emergency_profile_group_id_list", EmergencyProfileGroupIdList),
        ICAElement(10, "emergency_profile_active", Boolean, classifier=Classifier.DYNAMIC),
        ICAElement(11, "actions", Action))
    monitored_value: Attr
    threshold_active: Attr
    threshold_normal: Attr
    threshold_emergency: Attr
    min_over_threshold_duration: Attr
    min_under_threshold_duration: Attr
    emergency_profile: Attr
    emergency_profile_group_id_list: Attr
    emergency_profile_active: Attr
    actions: Attr
