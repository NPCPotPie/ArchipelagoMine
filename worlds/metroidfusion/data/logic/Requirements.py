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
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Morph Ball"
        if items_needed is None:
            items_needed = ["Morph Ball"]
        elif items_needed:
            items_needed.append("Morph Ball")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasBombData(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Bomb Data"
        if items_needed is None:
            items_needed = ["Bomb Data"]
        elif items_needed:
            items_needed.append("Bomb Data")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasPowerBombData(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Power Bomb Data"
        if items_needed is None:
            items_needed = ["Power Bomb Data"]
        elif items_needed:
            items_needed.append("Power Bomb Data")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

#Suit Items
class HasVaria(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Varia Suit"
        if items_needed is None:
            items_needed = ["Varia Suit"]
        elif items_needed:
            items_needed.append("Varia Suit")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasGravity(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Gravity Suit"
        if items_needed is None:
            items_needed = ["Gravity Suit"]
        elif items_needed:
            items_needed.append("Gravity Suit")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

#Mobility Items
# Reserved for when Wall Jump Boots enter the fray
class HasWallJump(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Wall Jump"
        if items_needed is None:
            items_needed = ["Wall Jump Boots"]
        elif items_needed:
            items_needed.append("Wall Jump Boots")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasHiJump(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Hi-Jump"
        if items_needed is None:
            items_needed = ["Hi-Jump"]
        elif items_needed:
            items_needed.append("Hi-Jump")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasSpaceJump(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Space Jump"
        if items_needed is None:
            items_needed = ["Space Jump"]
        elif items_needed:
            items_needed.append("Space Jump")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasSpeedBooster(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Speed Booster"
        if items_needed is None:
            items_needed = ["Speed Booster"]
        elif items_needed:
            items_needed.append("Speed Booster")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasScrewAttack(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Screw Attack"
        if items_needed is None:
            items_needed = ["Screw Attack"]
        elif items_needed:
            items_needed.append("Screw Attack")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

#Missile Items
class HasMissile(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Missile Data"
        if items_needed is None:
            items_needed = ["Missile Data"]
        elif items_needed:
            items_needed.append("Missile Data")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasSuperMissile(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Super Missile"
        if items_needed is None:
            items_needed = ["Super Missile"]
        elif items_needed:
            items_needed.append("Super Missile")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasIceMissile(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Ice Missile"
        if items_needed is None:
            items_needed = ["Ice Missile"]
        elif items_needed:
            items_needed.append("Ice Missile")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasDiffusionMissile(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Diffusion Missile"
        if items_needed is None:
            items_needed = ["Diffusion Missile"]
        elif items_needed:
            items_needed.append("Diffusion Missile")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

#Beam Items
class HasChargeBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Charge Beam"
        if items_needed is None:
            items_needed = ["Charge Beam"]
        elif items_needed:
            items_needed.append("Charge Beam")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasWideBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Wide Beam"
        if items_needed is None:
            items_needed = ["Wide Beam"]
        elif items_needed:
            items_needed.append("Wide Beam")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasPlasmaBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Plasma Beam"
        if items_needed is None:
            items_needed = ["Plasma Beam"]
        elif items_needed:
            items_needed.append("Plasma Beam")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasWaveBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Wave Beam"
        if items_needed is None:
            items_needed = ["Wave Beam"]
        elif items_needed:
            items_needed.append("Wave Beam")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasIceBeam(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Ice Beam"
        if items_needed is None:
            items_needed = ["Ice Beam"]
        elif items_needed:
            items_needed.append("Ice Beam")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

#Keycard Items
class HasKeycard1(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Level 1 Keycard"
        if items_needed is None:
            items_needed = ["Level 1 Keycard"]
        elif items_needed:
            items_needed.append("Level 1 Keycard")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasKeycard2(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Level 2 Keycard"
        if items_needed is None:
            items_needed = ["Level 2 Keycard"]
        elif items_needed:
            items_needed.append("Level 2 Keycard")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasKeycard3(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Level 3 Keycard"
        if items_needed is None:
            items_needed = ["Level 3 Keycard"]
        elif items_needed:
            items_needed.append("Level 3 Keycard")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class HasKeycard4(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Has Level 4 Keycard"
        if items_needed is None:
            items_needed = ["Level 4 Keycard"]
        elif items_needed:
            items_needed.append("Level 4 Keycard")
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)
#endregion

#region Combined Item Requirements
class CanBomb(HasMorph, HasBombData):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Bomb"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanPowerBomb(HasMorph, HasPowerBombData):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Power Bomb"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanBallJump(HasMorph):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([HasBombData(), HasHiJump()],)
        if name is None:
            name = "Can Ball Jump"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanJumpHigh(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements +=  ([HasHiJump(), HasSpaceJump()],)
        if name is None:
            name = "Can Jump High"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanLavaDive(HasVaria, HasGravity):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Lava Dive"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanJumpHighUnderwater(HasGravity):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements +=  ([CanJumpHigh()],)
        if name is None:
            name = "Can Jump High Underwater"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanSpeedBoosterUnderwater(HasGravity, HasSpeedBooster):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Speed Booster Underwater"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanScrewAttackUnderwater(HasGravity, HasScrewAttack):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Screw Attack Underwater"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseSuperMissile(HasMissile, HasSuperMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Use Super Missile"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseIceMissile(HasMissile, HasIceMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Use Ice Missile"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseDiffusionMissile(HasMissile, HasDiffusionMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Use Diffusion Missile"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseOneMissileUpgrade(HasMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements +=  ([CanUseSuperMissile(), CanUseIceMissile(), CanUseDiffusionMissile()],)
        if name is None:
            name = "Can Use One Missile Upgrade"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)


class CanUseTwoMissileUpgrades(HasMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([
            Requirement("Can Use Super Missile and Ice Missile",
                        ["Super Missile", "Ice Missile"]
            ),
            Requirement("Can Use Ice Missile and Diffusion Missile",
                        ["Ice Missile", "Diffusion Missile"]
            ),
            Requirement("Can Use Super Missile and Diffusion Missile",
                        ["Super Missile", "Diffusion Missile"]
            )
        ],)
        if name is None:
            name = "Can Use Two Missile Upgrades"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseAllMissileUpgrades(HasMissile, HasSuperMissile, HasIceMissile, HasDiffusionMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Use All Missiles"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanFreezeEnemies(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([HasIceBeam(), CanUseIceMissile(), CanUseDiffusionMissile()],)
        if name is None:
            name = "Can Freeze Enemies"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanActivatePillar(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += [CanBomb(), CanPowerBomb(), HasWaveBeam()]
        if name is None:
            name = "Can Activate Pillar"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanDestroyBombBlocks(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += [CanBomb(), CanPowerBomb(), HasScrewAttack()]
        if name is None:
            name = "Can Destroy Bomb Blocks"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanDestroyBombBlocksUnderwater(HasGravity, CanDestroyBombBlocks):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Destroy Bomb Blocks Underwater"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanChargedWaveShot(HasChargeBeam, HasWaveBeam):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Shoot Charged Wave Beam"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseOneBeamUpgrade(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([
            HasChargeBeam(),
            HasWideBeam(),
            HasPlasmaBeam(),
            HasWaveBeam(),
            HasIceBeam()
        ],)
        if name is None:
            name = "Can Use One Beam Upgrade"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseTwoBeamUpgrades(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([
            Requirement("Charge Wide", ["Charge Beam", "Wide Beam"]),
            Requirement("Charge Plasma", ["Charge Beam", "Plasma Beam"]),
            Requirement("Charge Wave", ["Charge Beam", "Wave Beam"]),
            Requirement("Charge Ice", ["Charge Beam", "Ice Beam"]),
            Requirement("Wide Plasma", ["Wide Beam", "Plasma Beam"]),
            Requirement("Wide Wave", ["Wide Beam", "Wave Beam"]),
            Requirement("Wide Ice", ["Wide Beam", "Ice Beam"]),
            Requirement("Plasma Wave", ["Plasma Beam", "Wave Beam"]),
            Requirement("Plasma Ice", ["Plasma Beam", "Ice Beam"]),
            Requirement("Wave Ice", ["Wave Beam", "Ice Beam"])
        ],)
        if name is None:
            name = "Can Use Two Beam Upgrades"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseThreeBeamUpgrades(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([
            Requirement("Charge Wide Plasma", ["Charge Beam", "Wide Beam", "Plasma Beam"]),
            Requirement("Charge Wide Wave", ["Charge Beam", "Wide Beam", "Wave Beam"]),
            Requirement("Charge Wide Ice", ["Charge Beam", "Wide Beam", "Ice Beam"]),
            Requirement("Charge Plasma Wave", ["Charge Beam", "Plasma Beam", "Wave Beam"]),
            Requirement("Charge Plasma Ice", ["Charge Beam", "Plasma Beam", "Ice Beam"]),
            Requirement("Charge Wave Ice", ["Charge Beam", "Wave Beam", "Ice Beam"]),
            Requirement("Wide Plasma Wave", ["Wide Beam", "Plasma Beam", "Wave Beam"]),
            Requirement("Wide Plasma Ice", ["Wide Beam", "Plasma Beam", "Ice Beam"]),
            Requirement("Wide Wave Ice", ["Wide Beam", "Wave Beam", "Ice Beam"]),
            Requirement("Plasma Wave Ice", ["Plasma Beam", "Wave Beam", "Ice Beam"])
        ],)
        if name is None:
            name = "Can Use Three Beam Upgrades"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseFourBeamUpgrades(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([
            Requirement("Charge Wide Plasma Wave",
                        ["Charge Beam", "Wide Beam", "Plasma Beam", "Wave Beam"]),
            Requirement("Charge Wide Plasma Ice",
                        ["Charge Beam", "Wide Beam", "Plasma Beam", "Ice Beam"]),
            Requirement("Charge Wide Wave Ice",
                        ["Charge Beam", "Wide Beam", "Wave Beam", "Ice Beam"]),
            Requirement("Charge Plasma Wave Ice",
                        ["Charge Beam", "Plasma Beam", "Wave Beam", "Ice Beam"]),
            Requirement("Wide Plasma Wave Ice",
                        ["Wide Beam", "Plasma Beam", "Wave Beam", "Ice Beam"]),
        ],)
        if name is None:
            name = "Can Use Four Beam Upgrades"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanUseAllBeamUpgrades(HasChargeBeam, HasWideBeam, HasPlasmaBeam, HasWaveBeam, HasIceBeam):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Use All Beam Upgrades"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

#endregion

#region Enemy Requirements
class CanDamageSmallGeron(HasMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Damage Small Geron"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanDamageMediumGeron(CanUseSuperMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Damage Medium Geron"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanDamageLargeGeron(CanPowerBomb):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Damage Large Geron"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanDamageStabilizer(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([HasMissile(), HasChargeBeam()],)
        if name is None:
            name = "Can Damage Stabilizer"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanDamageAnyGeron(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([CanPowerBomb(), HasScrewAttack()],)
        if name is None:
            name = "Can Damage Any Geron"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        return not options.NerfGeronWeaknesses

class CanDamageToughEnemy(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([HasMissile(), HasChargeBeam()],)
        if name is None:
            name = "Can Damage Tough Enemy"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanDamageToughEnemyThroughWalls(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([CanChargedWaveShot(), CanPowerBomb()],)
        if name is None:
            name = "Can Damage Tough Enemy Through Walls"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

#endregion

#region Boss Requirements
class CanDamageCoreX(HasMissile):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Damage Core X"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanFightEarlyGameBoss(CanDamageCoreX):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Fight Early Game Boss"
        super().__init__(name, items_needed, max(energy_tanks_needed, level_1_e_tanks), *requirements)

class CanFightMidGameBoss(CanFightEarlyGameBoss, CanUseSuperMissile, HasChargeBeam):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Fight Mid Game Boss"
        super().__init__(name, items_needed, max(energy_tanks_needed, level_2_e_tanks), *requirements)

class CanFightLateGameBoss(CanFightMidGameBoss, HasPlasmaBeam, HasSpaceJump):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Fight Late Game Boss"
        super().__init__(name, items_needed, max(energy_tanks_needed, level_3_e_tanks), *requirements)

#endregion

#region Trick Options Requirements

class CanDoBeginnerShinespark(HasSpeedBooster):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Do Beginner Shinespark"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.ShinesparkTrickDifficulty.value >= options.ShinesparkTrickDifficulty.option_beginner

class CanDoAdvancedShinespark(HasSpeedBooster):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Do Advanced Shinespark"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.ShinesparkTrickDifficulty >= options.ShinesparkTrickDifficulty.option_advanced

class CanDoSimpleWallJump(HasWallJump):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Do Simple Wall Jump"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_beginner

class CanDoAdvancedWallJump(HasWallJump):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Do Advanced Wall Jump"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.WallJumpTrickDifficulty >= options.WallJumpTrickDifficulty.option_advanced

class CanDoAdvancedCombat(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Do Advanced Combat"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanDoExpertCombat(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Do Expert Combat"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_expert

class CanFightMidGameBossOnAdvanced(CanFightEarlyGameBoss, HasChargeBeam):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Fight Mid Game Boss On Advanced"
        super().__init__(name, items_needed, max(energy_tanks_needed, level_1_e_tanks), *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanFightLateGameBossOnAdvanced(CanFightMidGameBoss):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Fight Late Game Boss on Advanced"
        super().__init__(name, items_needed, max(energy_tanks_needed, level_2_e_tanks), *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_advanced

class CanFightBossOnExpert(CanDamageCoreX, HasChargeBeam):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Can Fight Boss on Expert"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions") -> bool:
        return options.CombatDifficulty >= options.CombatDifficulty.option_expert

class SectorHubLevel1KeycardRequirement(HasKeycard1):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Sector Hub Level 1 Keycard Requirement"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

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
                 energy_tanks_needed = 0,
                 *requirements):
        if name is None:
            name = "Sector Hub Level 1 and 2 Keycard Requirement"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

    @staticmethod
    def check_option_enabled(options: "MetroidFusionOptions"):
        if options.GameMode == options.GameMode.option_custom:
            return not options.OpenSectorElevators
        else:
            return options.GameMode == options.GameMode.option_vanilla

# endregion

#region Prefab Requirements

class CanCollectCrumbleCity(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([
            Requirement("Can Collect Crumble City Item",
                        [],
                        0,
                        [
                            HasScrewAttack("Break into Crumble City and Collect Item",
                                           [],
                                           0,
                                           [
                                               HasSpaceJump("Fly"),
                                               # Awaiting trick option evaluation. This is masochistic to perform.
                                               # [CanDoExpertCrumbleJank()]
                                           ]
                                           # MARS changes the door type to a Level 0 Security Door. This is the original door requirement.
                                           # , [HasKeycard4()]
                                           )
                        ])
        ],)
        if name is None:
            name = "Can Collect Crumble City"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)

class CanObtainRipperTower(Requirement):
    def __init__(self,
                 name = None,
                 items_needed = None,
                 energy_tanks_needed = 0,
                 *requirements):
        requirements += ([
            Requirement("Can Obtain Ripper Tower Item",
                        ["Morph Ball"],
                        0,
                        [CanFreezeEnemies()])
        ])
        if name is None:
            name = "Can Obtain Ripper Tower"
        super().__init__(name, items_needed, energy_tanks_needed, *requirements)
