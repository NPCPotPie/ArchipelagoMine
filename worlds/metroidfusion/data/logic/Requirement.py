import typing
from typing import TYPE_CHECKING, Self
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from ... import MetroidFusionOptions


class RequirementBase(ABC):
    """
    Defines a set of requirements for a Connection or Location.
    \n The parameters are unpacked into a series of logical requirements where all housed in ``items_needed`` and one each of entries in each list housed in ``requirements`` must be met for this Requirement to be passed.
    \n Requirements logic is: (list1 AND list2 AND list3...) where (list_requirement1 OR list_requirement2 OR list_requirement3...)

    :param name: A String to label this Requirement. Defaults to the class name.
    :param items_needed: A list of items as Strings. Defaults to an empty list.
    :param energy_tanks_needed: An integer number of energy tanks required. Defaults to 0.
    :param requirements: A list of lists of Requirement objects. Defaults to an empty list.
    """
    name: str
    items_needed: list[str]
    energy_tanks_needed: int
    requirements: list[list[Self]]

    @abstractmethod
    def __init__(self,
                 name: str = None,
                 items_needed: list[str] = None,
                 energy_tanks_needed: int = 0,
                 *requirements: list[Self]):
        if name is None:
            self.name = self.__class__.__name__
        else:
            self.name = name
        if items_needed is None:
            items_needed = []
        self.items_needed = items_needed
        reqs: list[list[Self]] = []
        for requirement in requirements:
            if requirement:
                reqs.append(requirement)
        self.requirements = reqs
        self.energy_tanks_needed = energy_tanks_needed

    def __repr__(self):
        return_string = f"Name: {self.name}\n"
        return_string += f"ItemsNeeded: [{', '.join(self.items_needed)}]\n"
        # return_string += (f"Requirements1: "
        #                   f"[{', '.join([requirement.name for requirement in self.requirements1])}]\n")
        # return_string += (f"Requirements2: "
        #                   f"[{', '.join([requirement.name for requirement in self.requirements2])}]\n")
        return_string += f"EnergyTanks: {self.energy_tanks_needed}\n"
        return_string += "Requirements: ["
        if self.requirements:
            for req_list in self.requirements:
                return_string += f"\n\t[{', '.join(req.name for req in req_list)}]"
            return_string += "\n]"
        else:
            return_string += "]"
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
                 energy_tanks_needed: int = 0,
                 *requirements: list[RequirementBase]):
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class PONRRequirement(Requirement):
    """Defines a set of requirements to be used when Point of No Returns are disabled.
    These should always be more minimal than any surrounding requirements."""

    def __init__(self,
                 name: str = "Point of No Return Requirement",
                 items_needed: list[str] = None,
                 energy_tanks_needed = 0,
                 *requirements: list[RequirementBase]):
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.PointOfNoReturnsInLogic == True
