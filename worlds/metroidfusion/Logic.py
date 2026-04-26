from itertools import product as itertools_product
from typing import TYPE_CHECKING
import logging

from BaseClasses import CollectionState
from .data.logic.Requirement import Requirement
from .Items import valid_item_names, placeholder_names

if TYPE_CHECKING:
    from worlds.metroidfusion import MetroidFusionOptions

class LogicObject:
    requirements: list[set[str]] = []
    energy_tanks: list[int] = []
    missile_ammo: list[int] = []
    power_bomb_ammo: list[int] = []
    calculated_energy_tanks: int = 0
    player: int
    options: "MetroidFusionOptions"

    def __init__(self, player: int, options: "MetroidFusionOptions"):
        self.player = player
        self.options = options

    def logic_rule(self, state: CollectionState) -> bool:
        if not self.requirements:
            return True
        expression = None
        for (requirement_list,
             energy_tanks_value,
             missile_ammo_value,
             power_bomb_ammo_value) in zip(self.requirements,
                                           self.energy_tanks,
                                           self.missile_ammo,
                                           self.power_bomb_ammo):
            # Remove placeholder values in item list and re-validate
            requirement_list -= placeholder_names
            assert all([item in valid_item_names for item in requirement_list]), \
                f"Invalid item name in: {requirement_list}"
            if energy_tanks_value > 0:
                if self.options.ElevatorShuffle.value > self.options.ElevatorShuffle.option_none:
                    energy_tanks_value = energy_tanks_value // 2
                if self.options.CombatDifficulty >= self.options.CombatDifficulty.option_expert:
                    energy_tanks_value = energy_tanks_value // 2
            if missile_ammo_value > 0:
                match self.options.CombatDifficulty.value:
                    case self.options.CombatDifficulty.option_beginner:
                        missile_ammo_value = -int(-(missile_ammo_value * 1.25) // 1)
                    case self.options.CombatDifficulty.option_advanced:
                        missile_ammo_value = -int(-(missile_ammo_value * 1.1) // 1)
                missile_ammo_value -= self.options.MissileDataAmmo.value
                if self.options.MissileTankAmmo.value > 0:
                    missile_ammo_value = -int(-(missile_ammo_value / self.options.MissileTankAmmo.value) // 1)
            if power_bomb_ammo_value > 0:
                power_bomb_ammo_value -= self.options.PowerBombDataAmmo.value
                if self.options.PowerBombTankAmmo.value > 0:
                    power_bomb_ammo_value = -int(-(power_bomb_ammo_value / self.options.PowerBombTankAmmo.value) // 1)
            if expression is None:
                expression = (state.has_all(requirement_list, self.player)
                              and state.has("Energy Tank", self.player, energy_tanks_value)
                              and state.has("Missile Tank", self.player, missile_ammo_value)
                              and state.has("Power Bomb Tank", self.player, power_bomb_ammo_value))
            else:
                expression = (expression
                              or state.has_all(requirement_list, self.player)
                              and state.has("Energy Tank", self.player, energy_tanks_value)
                              and state.has("Missile Tank", self.player, missile_ammo_value)
                              and state.has("Power Bomb Tank", self.player, power_bomb_ammo_value))
        return expression



def create_logic_rule_for_list(
        requirements: list[Requirement],
        options: "MetroidFusionOptions",
        debug: bool = False) -> tuple[list[set[str]], list[int], list[int], list[int]]:
    if debug:
        print("Create logic rule for list...")
        logging.info("Create logic rule for list...")
    r_e_m_p: tuple[list[set[str]], list[int], list[int], list[int]] = ([], [], [], [])
    for requirement in requirements:
        for (new_rule,
             energy_tanks_in_rule,
             missile_ammo_in_rule,
             power_bomb_ammo_in_rule) in create_logic_rule(requirement, options, debug):
            r_e_m_p[0].append(new_rule)
            r_e_m_p[1].append(energy_tanks_in_rule)
            r_e_m_p[2].append(missile_ammo_in_rule)
            r_e_m_p[3].append(power_bomb_ammo_in_rule)
    if debug:
        for (requirement,
             energy_tanks,
             missiles,
             power_bombs) in zip(*r_e_m_p):
            debug_string = ("Logic rule:"
                            f"\nRequirements: {requirement}"
                            f"\nEnergy Tanks: {energy_tanks}"
                            f"\nMissiles: {missiles}"
                            f"\nPower Bombs: {power_bombs}"
                            "\n===\n")
            print(debug_string)
            logging.info(debug_string)
    return r_e_m_p

def create_logic_rule(
        requirement: Requirement,
        options: "MetroidFusionOptions",
        debug: bool = False) -> list[tuple[set[str], int, int, int]]:
    if requirement.check_option_enabled(options):
        possibilities: list[tuple[set[str], int, int, int]] = []
        hard_items: set[str] = set()
        unpack_requirement(
            requirement,
            possibilities,
            set(),
            options,
            hard_items,
            0,
            0,
            0,
            debug)
        if debug:
            sub_requirements_debug_string = [
                (f"\t({requirements_list},\n"
                 f"\t\tEnergy Tanks: {energy_tanks},\n"
                 f"\t\tMissiles: {missiles},\n"
                 f"\t\tPower Bombs: {power_bombs})")
                for requirements_list, energy_tanks, missiles, power_bombs in possibilities
            ]
            debug_string = ("Create logic rule...\n"
                            f"Requirement: {requirement.name}\n"
                            f"Item Possibilities: [\n{",\n".join(sub_requirements_debug_string)}\n]\n"
                            f"Hard Requirements: {{{", ".join(hard_items)}}}")
            print(debug_string)
            logging.info(debug_string)
        return possibilities
    elif debug:
        print(f"Requirement {requirement.name} disabled due to options.")
        logging.info(f"Requirement {requirement.name} disabled due to options.")
    return []

def unpack_requirement(
        requirement: Requirement,
        possibilities: list[tuple[set[str], int, int, int]],
        parent_items: set[str],
        options: "MetroidFusionOptions",
        parent_hard_items: set[str],
        parent_energy_tanks: int = 0,
        parent_missile_ammo: int = 0,
        parent_power_bomb_ammo: int = 0,
        debug = False) -> list[tuple[set[str], int, int, int]]:
    """Unpacks a requirement into a list of possible item sets each paired with an integer of energy tanks"""
    if debug:
        logging.info(f"Requirement {requirement.name}. "
                     f"Items needed {requirement.items_needed}. "
                     f"Sub-requirements {requirement.requirements}. "
                     f"Hard requirements {requirement.hard_items_needed}. "
                     f"Possibilities {possibilities}. "
                     f"Parent items {parent_items}. "
                     f"Parent hard requirements {parent_hard_items}. "
                     f"Parent Energy Tanks Needed {parent_energy_tanks}. "
                     f"Parent Missile Ammo {parent_missile_ammo}. "
                     f"Parent Power Bomb Ammo {parent_power_bomb_ammo}.")
    # Is the Requirement's YAML option enabled?
    if requirement.check_option_enabled(options):
        # Validate item names
        assert all([item_needed in valid_item_names
                    for item_needed in requirement.items_needed]), requirement
        assert all([hard_item_needed in valid_item_names
                    for hard_item_needed in requirement.hard_items_needed]), requirement
        # Has sub-requirements?
        if requirement.requirements:
            # Permute the requirements lists
            requirements_product: list[list[Requirement]] = list(itertools_product(*requirement.requirements))
            for requirements_permutation in requirements_product:
                # Check if all requirements in permutation have enabled options
                if not all([nested_requirement.check_option_enabled(options)
                        for nested_requirement in requirements_permutation]):
                    if debug:
                        print(f"Permutation disabled due to options: ["
                              f"{", ".join(nested_requirement.name 
                                           for nested_requirement in requirements_permutation)}]")
                        logging.info(f"Permutation disabled due to options: ["
                                     f"{", ".join(nested_requirement.name 
                                                  for nested_requirement in requirements_permutation)}]")
                    continue
                # Save state of parent's hard_items_needed
                current_hard_items = parent_hard_items.copy()
                current_parent_items = parent_items.copy()
                parent_hard_items |= requirement.hard_items_needed
                parent_items |= requirement.items_needed
                new_possibilities: list[tuple[set[str], int, int, int]] = []
                for nested_requirement in requirements_permutation:
                    and_possibilities = unpack_requirement(
                        nested_requirement,
                        [],
                        parent_items,
                        options,
                        parent_hard_items,
                        max(parent_energy_tanks, requirement.energy_tanks_needed),
                        parent_missile_ammo + requirement.missile_ammo_needed,
                        parent_power_bomb_ammo + requirement.power_bomb_ammo_needed,
                        debug
                    )
                    if new_possibilities:
                        current_new_possibilities = new_possibilities.copy()
                        new_possibilities = [(p[0][0] | p[1][0],
                                              max(p[0][1], p[1][1]),
                                              p[0][2] + p[1][2],
                                              p[0][3] + p[1][3])
                                             for p in itertools_product(current_new_possibilities, and_possibilities)]
                    elif not new_possibilities:
                        new_possibilities.extend(and_possibilities)
                for (n_r_items, n_r_energy, n_r_missiles, n_r_pbs) in new_possibilities:
                    combined_items = n_r_items | requirement.items_needed
                    calculated_energy = max(n_r_energy, requirement.energy_tanks_needed)
                    hard_test: bool = parent_hard_items.issubset(combined_items)
                    possibility_exists_test: bool = \
                        (combined_items, calculated_energy, n_r_missiles, n_r_pbs) in possibilities
                    if hard_test and not possibility_exists_test:
                        possibilities.append( (combined_items, calculated_energy, n_r_missiles, n_r_pbs) )
                    elif debug:
                        print(f"Skipping Possibility: {combined_items}")
                        logging.info(f"Skipping Possibility: {combined_items}")
                        if not hard_test:
                            print(f"\tDoes not contain all of: {parent_hard_items}")
                            logging.info(f"\tDoes not contain all of: {parent_hard_items}")
                        elif possibility_exists_test:
                            print(f"\tPossibility already existed when attempting to add to list")
                            logging.info(f"\tPossibility already existed when attempting to add to list")
                parent_hard_items = current_hard_items.copy()
                parent_items = current_parent_items.copy()
        elif requirement.items_needed:
            parent_hard_items |= requirement.hard_items_needed
            possibilities.append(( parent_items | requirement.items_needed,
                                   max(parent_energy_tanks, requirement.energy_tanks_needed),
                                   parent_missile_ammo + requirement.missile_ammo_needed,
                                   parent_power_bomb_ammo + requirement.power_bomb_ammo_needed ))
    else:
        print(f"Requirement {requirement.name} disabled due to options.")
        logging.info(f"Requirement {requirement.name} disabled due to options.")
        return []
    return possibilities