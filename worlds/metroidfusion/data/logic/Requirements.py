from typing import TYPE_CHECKING

from .Requirement import Requirement
if TYPE_CHECKING:
    from ... import MetroidFusionOptions

level_1_e_tanks = 3
level_2_e_tanks = 5
level_3_e_tanks = 7
level_4_e_tanks = 10

#region Individual Item Requirements
#Morph Ball Items
class HasMorph(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Morph Ball"
        if items_needed is None:
            items_needed = ["Morph Ball"]
        elif items_needed:
            items_needed.append("Morph Ball")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasBombData(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Bomb Data"
        if items_needed is None:
            items_needed = ["Bomb Data"]
        elif items_needed:
            items_needed.append("Bomb Data")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasPowerBombData(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Power Bomb Data"
        if items_needed is None:
            items_needed = ["Power Bomb Data"]
        elif items_needed:
            items_needed.append("Power Bomb Data")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

#Suit Items
class HasVaria(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Varia Suit"
        if items_needed is None:
            items_needed = ["Varia Suit"]
        elif items_needed:
            items_needed.append("Varia Suit")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasGravity(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Gravity Suit"
        if items_needed is None:
            items_needed = ["Gravity Suit"]
        elif items_needed:
            items_needed.append("Gravity Suit")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

#Mobility Items
# Reserved for when Wall Jump Boots enter the fray
class HasWallJump(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Wall Jump"
        if items_needed is None:
            items_needed = ["Wall Jump Boots"]
        elif items_needed:
            items_needed.append("Wall Jump Boots")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasHiJump(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Hi-Jump"
        if items_needed is None:
            items_needed = ["Hi-Jump"]
        elif items_needed:
            items_needed.append("Hi-Jump")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasSpaceJump(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Space Jump"
        if items_needed is None:
            items_needed = ["Space Jump"]
        elif items_needed:
            items_needed.append("Space Jump")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasSpeedBooster(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Speed Booster"
        if items_needed is None:
            items_needed = ["Speed Booster"]
        elif items_needed:
            items_needed.append("Speed Booster")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasScrewAttack(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Screw Attack"
        if items_needed is None:
            items_needed = ["Screw Attack"]
        elif items_needed:
            items_needed.append("Screw Attack")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

#Missile Items
class HasMissile(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Missile Data"
        if items_needed is None:
            items_needed = ["Missile Data"]
        elif items_needed:
            items_needed.append("Missile Data")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasSuperMissile(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Super Missile"
        if items_needed is None:
            items_needed = ["Super Missile"]
        elif items_needed:
            items_needed.append("Super Missile")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasIceMissile(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Ice Missile"
        if items_needed is None:
            items_needed = ["Ice Missile"]
        elif items_needed:
            items_needed.append("Ice Missile")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasDiffusionMissile(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Diffusion Missile"
        if items_needed is None:
            items_needed = ["Diffusion Missile"]
        elif items_needed:
            items_needed.append("Diffusion Missile")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

#Beam Items
class HasChargeBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Charge Beam"
        if items_needed is None:
            items_needed = ["Charge Beam"]
        elif items_needed:
            items_needed.append("Charge Beam")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasWideBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Wide Beam"
        if items_needed is None:
            items_needed = ["Wide Beam"]
        elif items_needed:
            items_needed.append("Wide Beam")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasPlasmaBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Plasma Beam"
        if items_needed is None:
            items_needed = ["Plasma Beam"]
        elif items_needed:
            items_needed.append("Plasma Beam")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasWaveBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Wave Beam"
        if items_needed is None:
            items_needed = ["Wave Beam"]
        elif items_needed:
            items_needed.append("Wave Beam")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasIceBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Ice Beam"
        if items_needed is None:
            items_needed = ["Ice Beam"]
        elif items_needed:
            items_needed.append("Ice Beam")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

#Keycard Items
class HasKeycard1(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Level 1 Keycard"
        if items_needed is None:
            items_needed = ["Level 1 Keycard"]
        elif items_needed:
            items_needed.append("Level 1 Keycard")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasKeycard2(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Level 2 Keycard"
        if items_needed is None:
            items_needed = ["Level 2 Keycard"]
        elif items_needed:
            items_needed.append("Level 2 Keycard")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasKeycard3(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Level 3 Keycard"
        if items_needed is None:
            items_needed = ["Level 3 Keycard"]
        elif items_needed:
            items_needed.append("Level 3 Keycard")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class HasKeycard4(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Has Level 4 Keycard"
        if items_needed is None:
            items_needed = ["Level 4 Keycard"]
        elif items_needed:
            items_needed.append("Level 4 Keycard")
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)
#endregion

#region Combined Item Requirements
class CanBomb(HasMorph, HasBombData):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Bomb"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanPowerBomb(HasMorph, HasPowerBombData):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Power Bomb"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanBallJump(HasMorph):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [HasBombData(), HasHiJump()]
        if name is None:
            name = "Can Ball Jump"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanJumpHigh(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [HasHiJump(), HasSpaceJump()]
        if name is None:
            name = "Can Jump High"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanLavaDive(HasVaria, HasGravity):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Lava Dive"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanJumpHighUnderwater(HasGravity):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [CanJumpHigh()]
        if name is None:
            name = "Can Jump High Underwater"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanSpeedBoosterUnderwater(HasGravity, HasSpeedBooster):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Speed Booster Underwater"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanScrewAttackUnderwater(HasGravity, HasScrewAttack):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Screw Attack Underwater"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanUseSuperMissile(HasMissile, HasSuperMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Use Super Missile"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanUseIceMissile(HasMissile, HasIceMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Use Ice Missile"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanUseDiffusionMissile(HasMissile, HasDiffusionMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Use Diffusion Missile"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanUseOneMissileUpgrade(HasMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [CanUseSuperMissile(), CanUseIceMissile(), CanUseDiffusionMissile()]
        if name is None:
            name = "Can Use One Missile Upgrade"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)


class CanUseTwoMissileUpgrades(HasMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [
            Requirement("Can Use Super Missile and Ice Missile",
                        ["Super Missile", "Ice Missile"]
            ),
            Requirement("Can Use Ice Missile and Diffusion Missile",
                        ["Ice Missile", "Diffusion Missile"]
            ),
            Requirement("Can Use Super Missile and Diffusion Missile",
                        ["Super Missile", "Diffusion Missile"]
            )
        ]
        if name is None:
            name = "Can Use Two Missile Upgrades"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanUseAllMissileUpgrades(HasMissile, HasSuperMissile, HasIceMissile, HasDiffusionMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Use All Missiles"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanFreezeEnemies(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [HasIceBeam(), CanUseIceMissile(), CanUseDiffusionMissile()]
        if name is None:
            name = "Can Freeze Enemies"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanActivatePillar(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [CanBomb(), CanPowerBomb(), HasWaveBeam()]
        if name is None:
            name = "Can Activate Pillar"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanDestroyBombBlocks(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [CanBomb(), CanPowerBomb(), HasScrewAttack()]
        if name is None:
            name = "Can Destroy Bomb Blocks"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanDestroyBombBlocksUnderwater(HasGravity, CanDestroyBombBlocks):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Destroy Bomb Blocks Underwater"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanChargedWaveShot(HasChargeBeam, HasWaveBeam):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Shoot Charged Wave Beam"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

#endregion

#region Enemy Requirements
class CanDamageSmallGeron(HasMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Damage Small Geron"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanDamageMediumGeron(CanUseSuperMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Damage Medium Geron"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanDamageLargeGeron(CanPowerBomb):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Damage Large Geron"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanDamageStabilizer(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [HasMissile(), HasChargeBeam()]
        if name is None:
            name = "Can Damage Stabilizer"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanDamageAnyGeron(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [CanPowerBomb(), HasScrewAttack()]
        if name is None:
            name = "Can Damage Any Geron"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        return not options.NerfGeronWeaknesses

class CanDamageToughEnemy(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [HasMissile(), HasChargeBeam()]
        if name is None:
            name = "Can Damage Tough Enemy"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None, [], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanDamageToughEnemyThroughWalls(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        this_req: list[Requirement] = [CanChargedWaveShot(), CanPowerBomb()]
        if name is None:
            name = "Can Damage Tough Enemy Through Walls"
        if requirements1 is None:
            requirements1 = this_req
        elif (requirements2 is None and requirements1) or (not requirements2 and requirements1):
            requirements2 = requirements1
            requirements1 = this_req
        elif requirements1 and requirements2:
            sub_requirements = [Requirement(None,[], requirements1, requirements2)]
            requirements1 = this_req
            requirements2 = sub_requirements
        else:
            requirements1 = this_req
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

#endregion

#region Boss Requirements
class CanDamageCoreX(HasMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Damage Core X"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

class CanFightEarlyGameBoss(CanDamageCoreX):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Fight Early Game Boss"
        super().__init__(name, items_needed, requirements1, requirements2, max(energy_tanks_needed, level_1_e_tanks))

class CanFightMidGameBoss(CanDamageCoreX, CanUseSuperMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Fight Mid Game Boss"
        super().__init__(name, items_needed, requirements1, requirements2, max(energy_tanks_needed, level_2_e_tanks))

class CanFightLateGameBoss(CanDamageCoreX, CanUseSuperMissile, HasPlasmaBeam, HasSpaceJump):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Fight Late Game Boss"
        super().__init__(name, items_needed, requirements1, requirements2, max(energy_tanks_needed, level_3_e_tanks))

#endregion

#region Trick Options Requirements

class CanDoBeginnerShinespark(HasSpeedBooster):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Do Beginner Shinespark"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.ShinesparkTrickDifficulty.value >= options.ShinesparkTrickDifficulty.option_beginner

class CanDoAdvancedShinespark(HasSpeedBooster):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Do Advanced Shinespark"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.ShinesparkTrickDifficulty >= options.ShinesparkTrickDifficulty.option_advanced

class CanDoSimpleWallJump(HasWallJump):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Do Simple Wall Jump"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_beginner

class CanDoAdvancedWallJump(HasWallJump):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Do Advanced Wall Jump"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_advanced

class CanDoAdvancedCombat(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Do Advanced Combat"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanDoExpertCombat(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Do Expert Combat"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_expert

class CanFightMidGameBossOnAdvanced(CanDamageCoreX, HasChargeBeam):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Fight Mid Game Boss On Advanced"
        super().__init__(name, items_needed, requirements1, requirements2, max(energy_tanks_needed, level_1_e_tanks))

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanFightLateGameBossOnAdvanced(CanDamageCoreX, HasChargeBeam, CanUseSuperMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Fight Late Game Boss on Advanced"
        super().__init__(name, items_needed, requirements1, requirements2, max(energy_tanks_needed, level_2_e_tanks))

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanFightBossOnExpert(CanDamageCoreX, HasChargeBeam):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Can Fight Boss on Expert"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)
    name = "Can Fight Boss on Expert"
    items_needed = ["Missile Data", "Charge Beam"]

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_expert

class SectorHubLevel1KeycardRequirement(HasKeycard1):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Sector Hub Level 1 Keycard Requirement"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        if options.GameMode == options.GameMode.option_custom:
            return not options.OpenSectorElevators
        else:
            return options.GameMode == options.GameMode.option_vanilla


class SectorHubLevel1And2KeycardRequirement(HasKeycard1, HasKeycard2):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 requirements1 = None,
                 requirements2 = None,
                 energy_tanks_needed = 0):
        if name is None:
            name = "Sector Hub Level 1 and 2 Keycard Requirement"
        super().__init__(name, items_needed, requirements1, requirements2, energy_tanks_needed)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        if options.GameMode == options.GameMode.option_custom:
            return not options.OpenSectorElevators
        else:
            return options.GameMode == options.GameMode.option_vanilla


# endregion