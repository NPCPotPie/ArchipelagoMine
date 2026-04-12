from itertools import product as itertools_product
from typing import TYPE_CHECKING
import logging

from BaseClasses import CollectionState
from .data.logic.Requirement import Requirement
from .Items import valid_item_names

if TYPE_CHECKING:
    from worlds.metroidfusion import MetroidFusionOptions

class LogicObject:
    requirements: list[set[str]] = []
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
        debug: bool = False) -> tuple[list[set[str]], list[int]]:
    requirements_list, energy_tanks_list = [], []
    for requirement in requirements:
        for new_rule, energy_tanks_in_rule in create_logic_rule(requirement, options, debug):
            requirements_list.append(new_rule)
            energy_tanks_list.append(energy_tanks_in_rule)
    print("Create logic rule for list...")
    logging.info("Create logic rule for list...")
    for requirement, energy_tanks in zip(requirements_list, energy_tanks_list):
        print("Logic rule:")
        print(f"Requirements: {requirement}")
        print(f"Energy Tanks: {energy_tanks}")
        print("===\n")
        logging.info("Logic rule:")
        logging.info(f"Requirements: {requirement}")
        logging.info(f"Energy Tanks: {energy_tanks}")
        logging.info("===\n")
    return requirements_list, energy_tanks_list

def create_logic_rule(
        requirement: Requirement,
        options: "MetroidFusionOptions",
        debug: bool = False) -> list[tuple[set[str], int]]:
    if requirement.check_option_enabled(options):
        possibilities: list[tuple[set[str], int]] = []
        hard_items: set[str] = set()
        unpack_requirement(
            requirement,
            possibilities,
            set(),
            options,
            hard_items,
            0,
            debug)
        if debug:
            print("Create logic rule...")
            print(f"Requirement: {requirement.name}")
            print("Requirements List: [")
            for requirements_list, energy in possibilities:
                print(f"\t{requirements_list}, \n\t\tEnergy Tanks: {energy}")
            print("]")
            print(f"Hard Requirements: {hard_items}")
            # print("Removed Requirements: [")
            # for rem_poss in removed_possibilities:
            #     print(f"\t[{rem_poss}]")
            # print("]")
            logging.info(f"  {requirement}")
            logging.info("]")
        return possibilities
    else:
        print(f"Requirement {requirement.name} disabled due to options.")
        logging.info(f"Requirement {requirement.name} disabled due to options.")
        return []

def unpack_requirement(
        requirement: Requirement,
        possibilities: list[tuple[set[str], int]],
        parent_items: set[str],
        options: "MetroidFusionOptions",
        parent_hard_items: set[str],
        parent_energy_tanks: int = 0,
        debug = False) -> list[tuple[set[str], int]]:
    """Unpacks a requirement into a list of possible item sets each paired with an integer of energy tanks"""
    logging.info(f"Requirement {requirement.name}. Items needed {requirement.items_needed}. Sub-requirements {requirement.requirements}. Hard requirements {requirement.hard_items_needed}. Possibilities {possibilities}. Parent items {parent_items}. Parent hard requirements {parent_hard_items}. Parent Energy Tanks Needed {parent_energy_tanks}.")
    # Is the Requirement's YAML option enabled?
    if requirement.check_option_enabled(options):
        # Validate item names
        for item_needed in requirement.items_needed:
            assert item_needed in valid_item_names, (item_needed, requirement)
        for hard_item_needed in requirement.hard_items_needed:
            assert hard_item_needed in valid_item_names, (hard_item_needed, requirement)
        # Has sub-requirements?
        if requirement.requirements:
            # Permute the requirements lists
            requirements_product: list[list[Requirement]] = list(itertools_product(*requirement.requirements))
            for requirements_permutation in requirements_product:
                # Check if all requirements in permutation have enabled options
                cont_permute: bool = False
                for nested_requirement in requirements_permutation:
                    if not nested_requirement.check_option_enabled(options):
                        print(f"Skipping permutation: {requirements_permutation}")
                        print(f"Requirement: '{nested_requirement.name}' disabled due to options.")
                        cont_permute = True
                # If ANY requirement in this permutation is disabled, skip providing its possibilities
                if cont_permute:
                    continue
                # Save state of parent's hard_items_needed
                current_hard_items = parent_hard_items.copy()
                parent_hard_items = parent_hard_items | requirement.hard_items_needed
                new_possibilities: list[tuple[set[str], int]] = []
                for nested_requirement in requirements_permutation:
                    and_possibilities = unpack_requirement(
                        nested_requirement,
                        [],
                        parent_items | requirement.items_needed,
                        options,
                        parent_hard_items,
                        max(parent_energy_tanks, requirement.energy_tanks_needed),
                        debug
                    )
                    if new_possibilities:
                        current_new_possibilities = new_possibilities.copy()
                        new_possibilities = []
                        while 0 < len(current_new_possibilities):
                            nested_possibility_items, nested_possibility_energy = current_new_possibilities.pop(0)
                            for and_possibility_items, and_possibility_energy in and_possibilities:
                                new_possibilities.append((nested_possibility_items | and_possibility_items,
                                                          max(nested_possibility_energy, and_possibility_energy)))
                    elif not new_possibilities:
                        new_possibilities.extend(and_possibilities)
                for nested_requirement_items, nested_requirement_energy in new_possibilities:
                    combined_items = nested_requirement_items | requirement.items_needed
                    calculated_energy = max(nested_requirement_energy, requirement.energy_tanks_needed)
                    hard_test: bool = (parent_hard_items.issubset(combined_items))
                    possibility_exists_test: bool = ((combined_items, calculated_energy) in possibilities)
                    if hard_test and not possibility_exists_test:
                        possibilities.append((combined_items, calculated_energy))
                    elif debug:
                        print(f"Skipping Possibility: {combined_items}")
                        if not hard_test:
                            print(f"Does not contain all of: {parent_hard_items}")
                        elif possibility_exists_test:
                            print(f"Possibility already existed when attempting to add to list")
                parent_hard_items = current_hard_items.copy()
        elif requirement.items_needed:
            parent_hard_items.update(requirement.hard_items_needed)
            possibilities.append((parent_items | requirement.items_needed,
                                  max(parent_energy_tanks, requirement.energy_tanks_needed)))
    else:
        print(f"Requirement {requirement.name} disabled due to options.")
        logging.info(f"Requirement {requirement.name} disabled due to options.")
        return []
    return possibilities