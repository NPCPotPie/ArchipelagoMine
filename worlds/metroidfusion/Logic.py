from copy import copy
from typing import TYPE_CHECKING
import logging

from BaseClasses import CollectionState
from .data.logic.Requirement import Requirement
from .Items import valid_item_names

if TYPE_CHECKING:
    from worlds.metroidfusion import MetroidFusionOptions

class LogicObject:
    requirements: list[list[str]] = []
    energy_tanks: list[int] = []
    calculated_energy_tanks: int = 0
    player: int
    options: "MetroidFusionOptions"

    def __init__(self, player: int, options: "MetroidFusionOptions"):
        self.player = player
        self.options = options

    def logic_rule(self, state: CollectionState) -> bool:
        if len(self.requirements) == 0:
            return True
        expression = None
        for requirement_list, energy_tanks in zip(self.requirements, self.energy_tanks):
            while "Wall Jump Boots" in requirement_list:
                requirement_list.remove("Wall Jump Boots")
            while "Nothing" in requirement_list:
                requirement_list.remove("Nothing")
            while "Point of No Return" in requirement_list:
                requirement_list.remove("Point of No Return")
            if energy_tanks > 0:
                if self.options.ElevatorShuffle.value > self.options.ElevatorShuffle.option_none:
                    energy_tanks = energy_tanks // 2
                else:
                    energy_tanks = energy_tanks
                if self.options.CombatDifficulty >= self.options.CombatDifficulty.option_expert:
                    energy_tanks = energy_tanks // 2
            if expression is None:
                expression = (state.has_all(requirement_list, self.player)
                              and state.has("Energy Tank", self.player, energy_tanks))
            else:
                expression = (expression
                              or state.has_all(requirement_list, self.player)
                              and state.has("Energy Tank", self.player, energy_tanks))
        return expression



def create_logic_rule_for_list(
        requirements: list[Requirement],
        options: "MetroidFusionOptions",
        debug: bool = False) -> tuple[list, list]:
    energy_tanks = []
    requirements_list = []
    for requirement in requirements:
        new_rule, energy_tanks_in_rule = create_logic_rule(requirement, options, debug)
        for requirement2, energy_tanks2 in zip(new_rule, energy_tanks_in_rule):
            requirements_list.append(requirement2)
            energy_tanks.append(energy_tanks2)
        continue
    print("Create logic rule for list...")
    logging.info("Create logic rule for list...")
    for requirement, energy_tanks_amount in zip(requirements_list, energy_tanks):
        print("Logic rule:")
        print(f"Requirements: {requirement}")
        print(f"Energy Tanks: {energy_tanks_amount}")
        print("===\n")
        logging.info("Logic rule:")
        logging.info(f"Requirements: {requirement}")
        logging.info(f"Energy Tanks: {energy_tanks_amount}")
        logging.info("===\n")
    return requirements_list, energy_tanks

def create_logic_rule(
        requirement: Requirement,
        options: "MetroidFusionOptions",
        debug: bool = False) -> tuple[list[str], list[int]]:
    if requirement.check_option_enabled(options):
        requirements_list = []
        energy_tanks_needed = []
        unpack_requirement(
            requirement,
            requirements_list,
            [],
            energy_tanks_needed,
            options,
            0,
            debug)
        if debug:
            print("Create logic rule...")
            print(f"Requirement: {requirement.name}")
            print(f"Requirements List: [")
            for requirement in requirements_list:
                print(f"  {requirement}")
            print(f"]")
            print(f"Energy Tanks Needed: {energy_tanks_needed}")
            logging.info(f"  {requirement}")
            logging.info(f"]")
            logging.info(f"Energy Tanks Needed: {energy_tanks_needed}")
        return requirements_list, energy_tanks_needed
    else:
        print(f"Requirement {requirement.name} disabled due to options.")
        logging.info(f"Requirement {requirement.name} disabled due to options.")
        return [], []

def unpack_requirement(
        requirement: Requirement,
        possibilities: list[list[str]],
        parent_items: list[str],
        energy_tanks: list[int],
        options: "MetroidFusionOptions",
        parent_energy_tanks: int = 0,
        debug = False) -> None:
    logging.info(f"Requirement {requirement.name}. Items needed {requirement.items_needed}. Sub-requirements {requirement.requirements}. Possibilities {possibilities}. Parent items {parent_items}. Energy Tanks {energy_tanks}. Parent Energy Tanks Needed {parent_energy_tanks}.")
    if requirement.check_option_enabled(options):
        for item_needed in requirement.items_needed:
            assert item_needed in valid_item_names, (item_needed, requirement)
        # Has more than one list of sub-requirements?
        if len(requirement.requirements) > 1:
            # Initialize AND gate
            and_possibilities: list[list[str]] = []
            # Requires an index due to arbitrary number of requirement lists
            index = 0
            while index < len(requirement.requirements):
                # First list initializes possibilities
                if not and_possibilities:
                    for nested_requirement in requirement.requirements[index]:
                        current_parent_items = copy(parent_items)
                        parent_items.extend(requirement.items_needed)
                        unpack_requirement(
                            nested_requirement,
                            and_possibilities,
                            parent_items,
                            energy_tanks,
                            options,
                            max(requirement.energy_tanks_needed, parent_energy_tanks),
                            debug
                        )
                        parent_items = copy(current_parent_items)
                # Lists following the first will compound on the possibilities
                else:
                    # Supply new blank list for overwriting the original
                    new_possibilities: list[list[str]] = []
                    for possibility in and_possibilities:
                        for nested_requirement in requirement.requirements[index]:
                            current_parent_items = copy(parent_items)
                            parent_items.extend(requirement.items_needed)
                            unpack_requirement(
                                nested_requirement,
                                new_possibilities,
                                possibility,
                                energy_tanks,
                                options,
                                max(requirement.energy_tanks_needed, parent_energy_tanks),
                                debug
                            )
                            parent_items = copy(current_parent_items)
                    # Once combined, overwrite
                    and_possibilities = new_possibilities
                # After completing last list of requirements, add them to the end of the current possibilities.
                if index == len(requirement.requirements) - 1:
                    possibilities.extend(and_possibilities)
                index += 1
        # This Requirement has only one Sub-List?
        elif len(requirement.requirements) == 1:
            for nested_requirement in requirement.requirements[0]:
                current_parent_items = copy(parent_items)
                parent_items.extend(requirement.items_needed)
                unpack_requirement(
                    nested_requirement,
                    possibilities,
                    parent_items,
                    energy_tanks,
                    options,
                    max(requirement.energy_tanks_needed, parent_energy_tanks),
                    debug
                )
                parent_items = copy(current_parent_items)
        if requirement.items_needed:
            items_needed = copy(requirement.items_needed)
            items_needed.extend(parent_items)
            possibilities.append(items_needed)
            energy_tanks.append(max(requirement.energy_tanks_needed, parent_energy_tanks))
    else:
        print(f"Requirement {requirement.name} disabled due to options.")
        logging.info(f"Requirement {requirement.name} disabled due to options.")