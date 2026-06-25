from dataclasses import dataclass
from COSEMpdu.axdr import ImplicitTaggedType
from .cosem_interface_classes.parameter import Parameter
from typing import Iterator

@dataclass(frozen=True)
class ParValues[T]:
    par:  Parameter
    data: T

    def __iter__(self) -> Iterator[Parameter | T]:
        yield self.par
        yield self.data

    def __str__(self):
        return F"{self.par} - {self.data}"


@dataclass(frozen=True)
class ParData(ParValues[ImplicitTaggedType]):
    data: ImplicitTaggedType
