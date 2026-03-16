from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator6Top
from ..regions.Sector1 import Sector1TourianHubElevatorTop
from ..regions.Sector4 import Sector4TubeRight
from ..regions.Sector5 import Sector5TubeLeft
from ..regions.Sector6 import *


Sector6Hub.connections = [
    VariableConnection(SectorHubElevator6Top, []),
    Connection(Sector6Crossroads, [CanDefeatMediumGeron, CanDefeatAnyGeron, CanDoBeginnerShinespark]),
    Connection(Sector6TubeLeft, [
        PONRRequirement([], [HasScrewAttack])
    ], one_way=True)
]

Sector6TubeLeft.connections = [
    VariableConnection(Sector4TubeRight, []),
    Connection(Sector6Hub, [
        HasScrewAttack([], [CanJumpHigh, CanDoSimpleWallJump, CanDoBeginnerShinespark])
    ])
]

Sector6TubeRight.connections = [
    VariableConnection(Sector5TubeLeft, []),
    Connection(Sector6Crossroads, [HasScrewAttack])
]

Sector6Crossroads.connections = [
    Connection(Sector6BeforeXBOXZone, [
        Requirement(["Varia Suit", "Level 4 Keycard"], [CanPowerBomb])
    ]),
    Connection(Sector6Catacombs, [
        PONRRequirement([], [HasSpeedBooster]),
        CanFightBoss(["Speed Booster", "Level 2 Keycard", "Varia Suit"], [CanBombOrPowerBomb])
    ], one_way=True),
    Connection(Sector6AfterVariaCoreXZone, [
        PONRRequirement(["Morph Ball"], [HasScrewAttack]),
        Requirement(["Morph Ball", "Varia Suit"], [HasScrewAttack]),
        CanFightBoss(["Level 2 Keycard", "Morph Ball", "Power Bomb Data", "Screw Attack"], [HasSpaceJump, CanDoAdvancedWallJump])
    ], one_way=True)
]

Sector6Catacombs.connections = [
    Connection(Sector6Crossroads, [
        CanDoBeginnerShinespark(["Hi-Jump"], [HasSpaceJump], level_1_e_tanks),
        CanDoAdvancedShinespark([], [], level_1_e_tanks)
    ]),
    Connection(Sector6BeforeVariaCoreXZone, [
        PONRRequirement([], [CanBombOrPowerBomb]),
        CanFightBoss(["Level 2 Keycard", "Varia Suit"], [CanBombOrPowerBomb])
    ], one_way=True)
]

Sector6BeforeXBOXZone.connections = [
    Connection(Sector6XBOXZone, [
        PONRRequirement(["Nothing"], [], level_4_e_tanks),
        HasScrewAttack([], [HasSpaceJump, CanDoSimpleWallJump], level_4_e_tanks),
        CanFreezeEnemies(["Hi-Jump"], [HasScrewAttack], level_4_e_tanks)
    ], one_way=True)
]

Sector6XBOXZone.connections = [
    Connection(Sector6AfterXBOXZone, [
        CanFightLateGameBoss,
        CanFightLategameBossOnAdvanced,
        CanFightBossOnExpert
    ])
]

Sector6AfterXBOXZone.connections = [
    Connection(Sector6BeforeXBOXZone, [
        HasScrewAttack([], [HasSpaceJump, CanDoSimpleWallJump]),
        CanFreezeEnemies(["Hi-Jump"], [HasScrewAttack])
    ], one_way=True),
    Connection(Sector6XBOXSave, [
        PONRRequirement(["Nothing"], []),
        Requirement([], [HasSpaceJump, CanFreezeEnemies, CanDoSimpleWallJumpWithHiJump, CanDoAdvancedWallJump], level_4_e_tanks),
        CanDoBeginnerShinespark([], [CanDoSimpleWallJumpWithScrewAttack], level_4_e_tanks)
    ], one_way=True)
]

Sector6XBOXSave.connections = [
    Connection(Sector6XBOXZone, [
        Requirement([], [HasSpaceJump, CanFreezeEnemies, CanDoSimpleWallJumpWithHiJump, CanDoAdvancedWallJump], level_4_e_tanks),
        CanDoBeginnerShinespark([], [CanDoSimpleWallJumpWithScrewAttack], level_4_e_tanks)
    ], one_way=True),
    Connection(Sector6RestrictedZone, [
        PONRRequirement([], [HasWaveBeam])
    ], one_way=True)
]

Sector6RestrictedZone.connections = [
    Connection(Sector6XBOXSave, [
        HasScrewAttack(["Wave Beam"], [HasSpaceJump, CanDoSimpleWallJump])
    ]),
    Connection(Sector6RestrictedZoneElevatorToTourian, [HasSpeedBooster], one_way=True)
    #One day, elevator shuffle PONR pathing logic. One day.
]

Sector6RestrictedZoneElevatorToTourian.connections = [
    VariableConnection(Sector1TourianHubElevatorTop, [HasKeycard4])
]

Sector6BeforeVariaCoreXZone.connections = [
    Connection(Sector6Catacombs, [
        CanPowerBomb([], [HasSpaceJump, CanDoAdvancedWallJump])
    ]),
    Connection(Sector6VariaCoreXZone, [
        Requirement(["Level 2 Keycard"], [CanFightBoss])
    ])
]

Sector6VariaCoreXZone.connections = [
    Connection(Sector6CavernsSave, [CanFightBoss])
]

Sector6AfterVariaCoreXZone.connections = [
    Connection(Sector6Crossroads, [
        PONRRequirement([], [HasMorph]),
        HasVaria(["Morph Ball"], [HasScrewAttack]),
        CanFightBoss(["Speed Booster", "Level 2 Keycard", "Varia Suit"], [CanBombOrPowerBomb])
    ], one_way=True),
    Connection(Sector6VariaCoreXZone, [
        PONRRequirement([], [CanFightBoss]),
        CanFightBoss(["Level 2 Keycard", "Morph Ball", "Power Bomb Data", "Screw Attack"], [HasSpaceJump, CanDoAdvancedWallJump]),
    ], one_way=True)
]

Sector6CavernsSave.connections = [
    Connection(Sector6AfterVariaCoreXZone, [HasVaria])
]

Sector6Hub.locations = [
    FusionLocation("Sector 6 (NOC) -- Entrance Lobby", False, [
        CanBallJump([], [CanDestroyBombBlocks, CanDoBeginnerShinespark])
    ])
]

Sector6Crossroads.locations = [
    FusionLocation("Sector 6 (NOC) -- Missile Mimic Lodge", False, [
        HasVaria([], [CanBombOrPowerBomb])
    ]),
    FusionLocation("Sector 6 (NOC) -- Pillar Highway", False, [
        HasVaria(["Screw Attack", "Speed Booster"], [CanBomb, HasWaveBeam])
    ]),
    FusionLocation("Sector 6 (NOC) -- Vault", False, [CanBallJumpAndBomb])
]

Sector6Catacombs.locations = [
    FusionLocation("Sector 6 (NOC) -- Catacombs", False, [])
]

Sector6BeforeXBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Spaceboost Alley -- Lower Item", False, [
        Requirement(["Level 4 Keycard", "Space Jump", "Screw Attack"], [HasSpeedBooster])
    ]),
    FusionLocation("Sector 6 (NOC) -- Spaceboost Alley -- Upper Item", False, [
        Requirement(["Level 4 Keycard", "Screw Attack"], [HasSpeedBooster])
    ])
]

Sector6XBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Arena", True, [
        CanFightLateGameBoss,
        CanFightLategameBossOnAdvanced,
        CanFightBossOnExpert
    ])
]

Sector6AfterXBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Garage -- Lower Item", False, [HasWaveBeam]),
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Garage -- Upper Item", False, [
        CanFreezeEnemies(["Morph Ball", "Bomb Data", "Screw Attack"], [HasSpaceJump, CanDoSimpleWallJump]),
    ])
]

Sector6RestrictedZone.locations = [
    FusionLocation("Main Deck -- Restricted Airlock", False, [HasSpeedBooster])
]

Sector6BeforeVariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Zozoro Wine Cellar", False, [
        CanBombOrPowerBomb([], [CanJumpHigh, CanFreezeEnemies])
    ])
]

Sector6VariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Varia Core-X Arena", True, [CanFightBoss])
]

Sector6AfterVariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Twin Caverns West -- Lower Item", False, [
        HasMorph([], [CanJumpHigh])
    ]),
    FusionLocation("Sector 6 (NOC) -- Twin Caverns West -- Upper Item", False, [])
]
