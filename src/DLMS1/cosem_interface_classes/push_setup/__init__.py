from typing import TypeAlias
from . import ver0, ver1, ver2


PushObjectList: TypeAlias = ver0.PushObjectList | ver1.PushObjectList | ver2.PushObjectList
PushObjectDefinition: TypeAlias = ver0.ObjectDefinition | ver1.PushObjectDefinition | ver2.PushObjectDefinition