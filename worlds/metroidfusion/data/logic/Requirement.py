import typing
from typing import TYPE_CHECKING, Self
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from ... import MetroidFusionOptions


class RequirementBase(ABC):
    """
    Defines a set of requirements for a Connection or Location.
    \n The parameters are unpacked into a series of logical requirements where all housed in ``items_needed`` and one each of entries in ``requirements1`` and ``requirements2`` must be met for this Requirement to be passed.

    :param name: A String to label this Requirement. Defaults to the class name.
    :param items_needed: A list of items as Strings. Defaults to an empty list.
    :param requirements1: A list of Requirement objects. Defaults to an empty list.
    :param requirements2: A list of Requirement objects. Defaults to an empty list.
    :param energy_tanks_needed: An integer number of energy tanks required. Defaults to 0.
    """
    name: str
    items_needed: list[str]
    requirements1: list[Self]
    requirements2: list[Self]
    energy_tanks_needed: int

    @abstractmethod
    def __init__(self,
                 name: str = None,
                 items_needed: list[str] = None,
                 requirements1: list[Self] = None,
                 requirements2: list[Self] = None,
                 energy_tanks_needed: int = 0):
        if name is None:
            self.name = self.__class__.__name__
        else:
            self.name = name
        if items_needed is None:
            items_needed = []
        self.items_needed = items_needed
        if requirements1 is None:
            requirements1 = []
        self.requirements1 = requirements1
        if requirements2 is None:
            requirements2 = []
        self.requirements2 = requirements2
        self.energy_tanks_needed = energy_tanks_needed

    def __repr__(self):
        return_string = f"{self.name}\n"
        return_string += f"ItemsNeeded: [{', '.join(self.items_needed)}]\n"
        return_string += (f"Requirements1: "
                          f"[{', '.join([requirement.name for requirement in self.requirements1])}]\n")
        return_string += (f"Requirements2: "
                          f"[{', '.join([requirement.name for requirement in self.requirements2])}]\n")
        return_string += f"EnergyTanks: {self.energy_tanks_needed}"
        return return_string

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return True

class Requirement(RequirementBase):
    def __init__(self,
                 name: str = None,
                 items_needed: list[str] = None,
                 requirements1: list[RequirementBase] = None,
                 requirements2: list[RequirementBase] = None,
                 energy_tanks_needed: int = 0):
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class PONRRequirement(Requirement):
    """Defines a set of requirements to be used when Point of No Returns are disabled.
    These should always be more minimal than any surrounding requirements."""

    def __init__(self,
                 name: str = "Point of No Return Requirement",
                 items_needed: list[str] = None,
                 requirements1: list[RequirementBase] = None,
                 requirements2: list[RequirementBase] = None,
                 energy_tanks_needed = 0):
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.PointOfNoReturnsInLogic == True
