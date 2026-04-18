from .data.logic.Requirement import Requirement, PONRRequirement
from .data.logic.Requirements import *

from .Logic import create_logic_rule_for_list, create_logic_rule
from test.bases import WorldTestBase
from .MFOptions import MetroidFusionOptions

class FusionLogicTest(WorldTestBase):
    game = "Metroid Fusion"
    options = {
        # Game Options
        "progression_balancing": "normal",
        "accessibility": "full",
        "death_link": False,
        # Item & Location Options
        "local_items": "",
        "non_local_items": "",
        "start_inventory": "",
        "start_inventory_from_pool": "",
        "start_hints": "",
        "start_location_hints": "",
        "exclude_locations": "",
        "priority_locations": "",
        "item_links": "",
        "plando_items": "",
        # Main Options
        "GameMode": 2,
        "InfantMetroidsInPool": 5,
        "InfantMetroidsRequired": 5,
        "InfantMetroidLocations": 0,
        # Logic Options
        "EarlyProgression": 2,
        "SectorTubeShuffle": True,
        "ElevatorShuffle": "all",
        "PointOfNoReturnsInLogic": True,
        # Trick Options
        "WallJumpTrickDifficulty": 2,
        "ShinesparkTrickDifficulty": 1,
        "CombatDifficulty": 1,
        # Custom Game Mode Options
        "StartingLocation": 0,
        "StartingMajorUpgrades": "random-range-low-1-3",
        "StartingEnergyTanks": 0,
        "FillerItems": ["Missile Tank", "Power Bomb Tank"],
        "OpenSectorElevators": False,
        "SectorNavigationRoomHintLocks": False,
        # Minor Options
        "PaletteRandomization": False,
        "EnableHints": True,
        "NerfGeronWeaknesses": True,
        "RevealHiddenBlocks": False,
        "FastDoorTransitions": True,
        "MissileDataAmmo": 10,
        "MissileTankAmmo": "random-range-1-10",
        "PowerBombDataAmmo": 5,
        "PowerBombTankAmmo": "random-range-0-2",
        "TrickyShinesparksInRegionLogic": False,
        "SimpleWallJumpsInRegionLogic": False,
    }

    def individual_logic_test(self) -> None:
        test_label: str = "Hard Requirements"
        print(f"Logic Test: {test_label}")
        reqs: list[Requirement] = [
            # Copy or write a Requirement in this area to test

        ]
        expected_requirements: list[tuple[set[str], int, int, int]] = [
            # Type out expected sets of item combinations to be produced here.
            # Requirements Set, Energy Tanks, Missile Ammo, PB Ammo
            # All sets in this list will attempt to be asserted and print an error to console if it doesn't exist.

        ]
        (rules,
         energy_tanks,
         missiles,
         power_bombs) = create_logic_rule_for_list(reqs, MetroidFusionOptions(**self.options), True)
        for (expected_requirement,
             expected_energy,
             expected_missiles,
             expected_power_bombs) in expected_requirements:
            try:
                assert expected_requirement in rules
            except AssertionError:
                print(f"{expected_requirement} is not here!")
        print("===\nEnd of Test\n===")

def main():
    test = FusionLogicTest()
    test.individual_logic_test()

if __name__ == "__main__":
    # Ensure this file is run as a MODULE and not a script 
    main()