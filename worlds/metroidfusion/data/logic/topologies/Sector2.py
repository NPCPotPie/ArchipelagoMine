from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator2Top
from ..regions.Sector1 import Sector1TubeRight
from ..regions.Sector2 import *
from ..regions.Sector4 import Sector4TubeLeft

Sector2Hub.connections = [
    VariableConnection(SectorHubElevator2Top, []),
    Connection(Sector2TubeLeft, [HasScrewAttack()]),
    Connection(Sector2TubeRight, [HasScrewAttack()]),
    Connection(Sector2LeftSide, [
        Requirement("Traverse from Data Room to Zig-Zag-Zone",
                    ["Morph Ball"],
                    0,
                    [
                        CanDestroyBombBlocks()
                    ], [
                        CanBallJump(),
                        PONRRequirement("PONR - To Zig-Zag-Zone")
                    ])
    ], one_way=True),
    Connection(Sector2ZazabiZoneUpper, [CanBomb(), CanPowerBomb()]),
    Connection(Sector2NettoriZone, [
        Requirement("Can Enter Hub Power Bomb Tunnel",
                    ["Morph Ball"],
                    0,
                    [
                        CanPowerBomb()
                    ], [
                        CanJumpHigh(),
                        CanDoSimpleWallJump()
                    ])
    ])
]

Sector2TubeLeft.connections = [
    VariableConnection(Sector1TubeRight, [])
]

Sector2TubeRight.connections = [
    VariableConnection(Sector4TubeLeft, [])
]

Sector2LeftSide.connections = [
    Connection(Sector2Hub, [
        Requirement("Climb Zig-Zag-Zone from Maintenance Wing",
                    ["Morph Ball"],
                    0,
                    [
                        CanBomb(),
                        CanPowerBomb()
                    ], [
                        HasSpaceJump(None,
                                     [],
                                     0,
                                     [
                                         HasScrewAttack(),
                                         CanPowerBomb()
                                     ]),
                        CanDoAdvancedWallJump(None, ["Hi-Jump"])
                    ])
    ]),
    Connection(Sector2ZazabiZone, [CanBomb(), CanPowerBomb()], one_way=True)
]

Sector2ZazabiZone.connections = [
    Connection(Sector2LeftSide, [
        Requirement("Climb Maintenance Wing",
                    [],
                    0,
                    [
                        CanBomb(),
                        CanPowerBomb(),
                        HasScrewAttack()
                    ], [
                        HasSpaceJump(),
                        CanDoSimpleWallJump(None, ["Hi-Jump"]),
                        CanDoAdvancedWallJump()
                    ], [
                        # Required if coming from Cathedral
                        CanFreezeEnemies(),
                        CanJumpHigh()
                    ])
    ]),
    Connection(Sector2NettoriZone, [HasSpaceJump()]),
    Connection(Sector2ZazabiZoneUpper, [
        Requirement("Climb Cathedral",
                    [],
                    0,
                    [
                        CanBomb(),
                        CanPowerBomb()
                    ], [
                        CanJumpHigh()
                    ])
    ]),
]

Sector2ZazabiZoneUpper.connections = [
    Connection(Sector2ZazabiZone, [
        PONRRequirement("PONR - Drop Down Cathedral",
                        [],
                        0,
                        [
                            CanBomb(),
                            CanPowerBomb()
                        ]),
    ], one_way=True)
]

Sector2Hub.locations = [
    FusionLocation("Sector 2 (TRO) -- Crumble City -- Lower Item", False, [
        CanCollectCrumbleCity()
    ]),
    FusionLocation("Sector 2 (TRO) -- Crumble City -- Upper Item", False, [
        CanCollectCrumbleCity()
    ]),
    FusionLocation("Sector 2 (TRO) -- Data Courtyard", False, [CanBomb(), CanPowerBomb()]),
    FusionLocation("Sector 2 (TRO) -- Data Room", True, [HasKeycard1()]),
    FusionLocation("Sector 2 (TRO) -- Kago Room", False, [
        CanJumpHigh(), HasScrewAttack(), CanFreezeEnemies(), CanDoBeginnerShinespark()
    ]),
    FusionLocation("Sector 2 (TRO) -- Level 1 Security Room", True, [
        Requirement("Use the Security Terminal",
                    [],
                    0,
                    [
                        HasSpaceJump("Fly"),
                        HasKeycard1("Open the Door"),
                        PONRRequirement("PONR - Level 1 Security Room")
                    ])
    ]),
    FusionLocation("Sector 2 (TRO) -- Lobby Cache", False, [
        HasKeycard1("Can Collect Lobby Cache",
                    [],
                    0,
                    [
                        CanBomb(),
                        CanPowerBomb()
                    ])
    ]),
]

Sector2LeftSide.locations = [
    FusionLocation("Sector 2 (TRO) -- Zig-Zag-Zone", False, [
        Requirement("Can Obtain Zig-Zag-Zone Item",
                    ["Morph Ball"],
                    0,
                    [
                        CanActivatePillar(),
                        CanJumpHigh()
                    ])
    ])
]

Sector2ZazabiZone.locations = [
    FusionLocation("Sector 2 (TRO) -- Cultivation Station", False, [
        Requirement("Can Obtain Cultivation Station Item",
                    [],
                    0,
                    [
                        # Need to break a chain of bomb blocks. Satisfies CanActivatePillar
                        CanBomb(),
                        CanPowerBomb()
                    ], [
                        # Required when coming from Cathedral
                        CanFreezeEnemies(),
                        CanJumpHigh()
                    ])
    ]),
    FusionLocation("Sector 2 (TRO) -- Oasis", False, [CanJumpHigh(), CanFreezeEnemies()]),
    FusionLocation("Sector 2 (TRO) -- Oasis Storage", False, [
        Requirement("Can Obtain Oasis Storage Item",
                    ["Morph Ball"],
                    0,
                    [
                        CanPowerBomb("Power Bomb the Block and Use the Pillar"),
                        CanBomb("Use the Pillar to Bomb the Block",
                                [],
                                0,
                                [
                                    HasHiJump(),
                                    # Good movement from pillar can be used to barely be able to bomb the block.
                                    # CanDoAdvancedMovement()
                                ]),
                        HasGravity("Move Underwater",
                                   [],
                                   0,
                                   [
                                       CanBomb("Bomb Jump from Pillar"),
                                       HasWaveBeam("Screw Attack from the Pillar", ["Screw Attack"]),
                                       CanJumpHigh("Screw Attack from the Ground", ["Screw Attack"])
                                   ])
                    ], [
                        # Getting into the room from Oasis
                        CanActivatePillar(),
                        CanFreezeEnemies("Freeze the Fish")
                    ])
    ]),
    FusionLocation("Sector 2 (TRO) -- Ripper Tower -- Lower Item", False, [
        PONRRequirement("PONR - Ripper Tower Lower Item",
                        [],
                        0,
                        [CanObtainRipperTower()]),
        CanDestroyBombBlocks("Grab Ripper Tower Items and Leave",
                             ["Morph Ball"],
                             0,
                             [CanObtainRipperTower()]),
    ]),
    FusionLocation("Sector 2 (TRO) -- Ripper Tower -- Upper Item", False, [
        PONRRequirement("PONR - Ripper Tower Upper Item",
                        [],
                        0,
                        [CanObtainRipperTower()]),
        CanDestroyBombBlocks("Grab Ripper Tower Items and Leave",
                             ["Morph Ball"],
                             0,
                             [CanObtainRipperTower()]),
    ]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Arena", True, [
        PONRRequirement("PONR - Fight Zazabi", [],0, [CanFightEarlyGameBoss()]),
        CanJumpHigh("Fight Zazabi", [],0, [CanFightEarlyGameBoss()]),
    ]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Arena Access", False, []),
    FusionLocation("Sector 2 (TRO) -- Zazabi Speedway -- Lower Item", False, [
        CanFightEarlyGameBoss("Kill Zazabi and Enter Zazabi Speedway",
                              ["Space Jump", "Screw Attack", "Speed Booster"]),
    ]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Speedway -- Upper Item", False, [
        CanFightEarlyGameBoss("Kill Zazabi and Enter Zazabi Speedway",
                              ["Space Jump", "Screw Attack", "Speed Booster"]),
    ])
]

Sector2ZazabiZoneUpper.locations = [
    FusionLocation("Sector 2 (TRO) -- Dessgeega Dorm", False, [
        HasScrewAttack("Get Stuck in Dessgeega Dorm Item Alcove",
                       ["Morph Ball"],
                       0,
                       [PONRRequirement("PONR - Dessgeega Dorm")]),
        CanBomb(),
        CanPowerBomb()
    ])
]

Sector2NettoriZone.locations = [
    FusionLocation("Sector 2 (TRO) -- Nettori Arena", True, [
        CanFightMidGameBoss(),
        CanFightMidGameBossOnAdvanced()
    ]),
    FusionLocation("Sector 2 (TRO) -- Overgrown Cache", False, [HasMorph()]),
    FusionLocation("Sector 2 (TRO) -- Puyo Palace", False, [
        Requirement("Obtain Puyo Palace Item from Above",
                    [],
                    0,
                    [
                        PONRRequirement("PONR - Puyo Palace Item from Above"),
                        HasSpaceJump("Obtain Puyo Palace Item and Return")
                    ])
    ])
]
