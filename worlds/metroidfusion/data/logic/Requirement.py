import typing
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from ... import MetroidFusionOptions


class Requirement:
    """
    Defines a set of requirements for a Connection or Location.
    \n The parameters are unpacked into a series of logical requirements where all ``items_needed`` and entries in ``requirements1`` and ``requirements2`` must be met for this Requirement to be passed.
    \n If either ``requirements1`` or ``requirements2`` are not empty, at least one Requirement object must be fulfilled.
    \n If both ``requirements1`` and ``requirements2`` are not empty, at least one Requirement object from each list must be fulfilled.

    Attribute "name": The String name of the requirement. When not given, the class name will be used in its place.

    :param items_needed: A list of items named by Strings that are all required to be had. When not given, defaults to an empty list.
    :param requirements1: A list of Requirement objects. When not given, defaults to an empty list.
    :param requirements2: A list of Requirement objects. When not given, defaults to an empty list.
    :param energy_tanks_needed: The number of energy tanks required. When not given, defaults to 0.
    """
    items_needed: list[str] = []
    requirements1: list[Self] = []
    requirements2: list[Self] = []
    energy_tanks_needed: int = 0
    name: str = __name__

    def __init__(self, items_needed: list[str] = None, requirements1 = None, requirements2 = None, energy_tanks_needed = 0):
        if items_needed is None:
            items_needed = []
        if requirements1 is None:
            requirements1 = []
        if requirements2 is None:
            requirements2 = []

        self.items_needed = items_needed
        self.requirements1 = requirements1
        self.requirements2 = requirements2
        self.energy_tanks_needed = energy_tanks_needed
        self.name: str = self.__class__.__name__

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

class PONRRequirement(Requirement):
    """Defines a set of requirements to be used when Point of No Returns are disabled.
    These should always be more minimal than any surrounding requirements."""
    additional_requirements: tuple[list[str], typing.Literal["and", "or"]]

    def __init__(self, items_needed: list[str] = None, requirements1 = None, requirements2 = None, energy_tanks_needed = 0, additional_requirements = ([], "or")):
        if items_needed is None:
            items_needed = []
        if requirements1 is None:
            requirements1 = []
        if requirements2 is None:
            requirements2 = []
        super().__init__(items_needed, requirements1, requirements2, energy_tanks_needed)
        self.additional_requirements = additional_requirements

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.PointOfNoReturnsInLogic == True
