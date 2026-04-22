from ..Connection import Connection
from ..Requirement import Requirement, PONRRequirement
from ..Requirements import HasScrewAttack
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator3Top
from ..regions.Sector1 import Sector1TubeLeft
from ..regions.Sector3 import *
from ..regions.Sector5 import Sector5TubeRight

Sector3Hub.connections = [
    VariableConnection(SectorHubElevator3Top, []),
    Connection(Sector3FieryStorageRight, [
        PONRRequirement("PONR - Shinespark to Fiery Storage", [
            CanDoBeginnerShinespark()
        ], [
            HasVaria()
        ]),
        HasVaria("Cross Monkey Bars of Fire", [
            CanDamageToughEnemy("Kill Ceiling Sidehoppers", enemy_hp=(24 * 2), immunities={"Beam"})
        ], [
            CanLavaDive(),
            CanJumpHigh()
                 ]),
        CanDoBeginnerShinespark("Shinespark Across Monkey Bars of Fire", [
            CanDestroyBombBlocks()
        ], [
            HasVaria()
                ])
    ], one_way=True),
    Connection(Sector3SecurityZone, [
        HasSpeedBooster()
    ]),
    Connection(Sector3MainShaft, [
        HasSpeedBooster("Enter Sector 3 Main Shaft", [
            CanDamageToughEnemy("Kill the Fune/Namihe"),
            CanDoBeginnerShinespark("Kill the Fune/Namihe - Alternate"),
            HasMorph("Avoid the Fune/Namihe"),
            HasWaveBeam("Open the Gate Backwards")
        ], [
            PONRRequirement("PONR - Enter Sector 3 Main Shaft"),
            CanDestroyBombBlocks(None, [
                HasMorph()
            ]),
            HasKeycard2()
        ])
    ], one_way=True),
    Connection(Sector3BobZone, [
        HasKeycard2("Enter Bob's Abode", [
            CanDamageMediumGeron(),
            CanDamageAnyGeron()
        ], [
            PONRRequirement("PONR - Enter Bob's Abode"),
            CanDestroyBombBlocks(),
            HasHiJump("Shoot Blocks and Spring Ball Out")
        ], [
            HasMorph()
        ])
    ]),
    Connection(Sector3BOXZone, [
        HasKeycard2("Enter BOX's Zone", [
            CanDamageMediumGeron(),
            CanDamageAnyGeron()
        ]),
    ]),
    Connection(Sector3LowerAttic, [
        HasMorph("Enter Attic from Sector 3 Entrance", [
            HasSpaceJump(),
            CanDoBeginnerShinespark()
        ], [
            HasScrewAttack()
        ])
    ])
]

Sector3TubeLeft.connections = [
    VariableConnection(Sector5TubeRight, []),
    Connection(Sector3FieryStorageLeft, [
        HasScrewAttack("Exit Sector 3 West Tube", [
            CanJumpHigh(),
            CanDoSimpleWallJump()
        ])
    ])
]

Sector3TubeRight.connections = [
    VariableConnection(Sector1TubeLeft, []),
    Connection(Sector3UpperAttic, [
        PONRRequirement("PONR - Drop from Sector 3 East Tube", [
            HasScrewAttack()
        ])
    ], one_way=True)
]

Sector3FieryStorageRight.connections = [
    Connection(Sector3FieryStorageLeft, [
        CanDestroyBombBlocks()
    ]),
    Connection(Sector3Hub, [
        HasVaria("Cross Monkey Bars of Fire", [
            CanDamageToughEnemy(),
            HasScrewAttack()
        ], [
            CanLavaDive(),
            CanJumpHigh()
        ]),
        CanDoBeginnerShinespark("Shinespark Across Monkey Bars of Fire", [
            CanDestroyBombBlocks()
        ], [
            HasVaria()
        ])
    ],one_way=True)
]

Sector3FieryStorageLeft.connections = [
    Connection(Sector3TubeLeft, [
        PONRRequirement("PONR - Drop to Sector 3 West Tube", [
            HasScrewAttack()
        ])
    ], one_way=True)
]

Sector3MainShaft.connections = [
    # Connecting to Sector 3 Hub is not possible without connecting to other Zones first.

    # Connection(Sector3Hub, [
    #     PONRRequirement(["Morph Ball"], [CanDestroyBombBlocks]),
    #     Requirement(["Morph Ball", "Speed Booster"], [CanDestroyBombBlocks]),
    #     CanDamageMediumGeron(["Morph Ball", "Level 2 Keycard"], [CanDestroyBombBlocks]),
    #     CanDamageAnyGeron(["Morph Ball", "Level 2 Keycard"], [CanDestroyBombBlocks])
    # ], one_way=True),
    Connection(Sector3BoilerZone, [
        HasKeycard2(None, [
            HasVaria()
        ])
    ]),
    Connection(Sector3BobZone, [
        HasScrewAttack("Break Into Bob's Abode", [
            HasMorph()
        ])
    ], one_way=True),
    Connection(Sector3SovaProcessing, [
        HasKeycard2("Enter Sova Processing", [
            CanDestroyBombBlocks()
        ], [
            HasSpaceJump("Fly to Upper Door"),
            HasWaveBeam("Open Gate Backwards"),
            CanDoBeginnerShinespark("Shinespark to Upper Door", [
                CanDamageToughEnemy()
            ]),
            CanFreezeEnemies("Developer Intended Route", [
                HasHiJump()
            ])
        ], [
            HasVaria()
        ], energy_tanks_needed=level_2_e_tanks)
    ])
]

Sector3BobZone.connections = [
    Connection(Sector3BOXZone, [
        HasKeycard2("Leave Bob's Abode to BOX Zone", [
            CanBomb(),
            HasHiJump("Destroy Blocks to Ascend Tunnel", [
                HasWaveBeam(),
                CanUseDiffusionMissile(),
                CanPowerBomb()
            ])
        ], [
            HasMorph()
        ]),
    ]),
    Connection(Sector3Hub, [
        PONRRequirement("PONR - Drop Down Bob's Poop Chute", [
            CanDestroyBombBlocks()
        ], [
            HasMorph()
        ]),
    ], one_way=True),
    Connection(Sector3MainShaft, [
        CanBomb(),
        CanPowerBomb()
    ])
]

Sector3BOXZone.connections = [
    Connection(Sector3BobZone, [
        PONREnterBobsTunnelFromAbove()
    ], one_way=True),
    Connection(Sector3MainShaft, [
        PONREnterBobsTunnelFromAbove()
    ], one_way=True),
    Connection(Sector3UpperAttic, [
        PONRRequirement("PONR - Skip BOX Fight with Space Jump", [
            HasSpaceJump()
        ])
    ], one_way=True)
]

Sector3LowerAttic.connections = [
    Connection(Sector3Hub, [
        CanDestroyBombBlocks("Sector 3 Lower Attic - Exit Left", [
            HasMorph()
        ])
    ], one_way=True),
    Connection(Sector3UpperAttic, [
        CanClimbSector3Attic()
    ])
]

Sector3UpperAttic.connections = [
    Connection(Sector3BOXZone, [
        CanFightBOX()
    ]),
    Connection(Sector3TubeRight, [
        HasScrewAttack("Climb to Sector 3 East Tube", [
            CanJumpHigh(),
            CanDoBeginnerShinespark()
        ])
    ]),
    Connection(Sector3LowerAttic, [
        PONRRequirement("PONR - Sector 3 Upper Attic - Shinespark", [
            CanDestroyBombBlocks()
        ], [
            HasSpeedBooster()
        ]),
        PONRRequirement("PONR - Sector 3 Upper Attic - Drop to Lower Path", [
            CanDestroyBombBlocks()
        ], [
            HasMorph()
        ])
    ], one_way=True),
]

Sector3SovaProcessing.connections = [
    Connection(Sector3UpperAttic, [
        CanLavaDive("Ascend Sector 3 Garbage Chute", [
            HasScrewAttack()
        ], [
            HasSpeedBooster()
        ])
    ], one_way=True)
]

Sector3FieryStorageRight.locations = [
    FusionLocation("Sector 3 (PYR) -- Fiery Storage -- Lower Item", False, []),
]

Sector3FieryStorageLeft.locations = [
    FusionLocation("Sector 3 (PYR) -- Fiery Storage -- Upper Item", False, [
        CanDestroyBombBlocks("Can Obtain Upper Fiery Storage Item", [
            CanActivatePillar(),
            HasSpaceJump(),
            CanDoAdvancedShinespark("Charge from below and Wall Jump up before Shinespark", [
                CanDoAdvancedWallJump()
            ]),
            # It is possible to wall jump up where the pillar is without extending it.
            # #future CanDoExpertWallJump()
        ], [
            HasSpeedBooster()
        ]),
    ])
]

Sector3TubeLeft.locations = [
    FusionLocation("Sector 3 (PYR) -- Sector 3 (PYR) Westbound Glass Tube", False, [
        CanBomb("Spring Ball and Bomb", [
            HasHiJump()
        ]),
        CanPowerBomb(),
        HasScrewAttack()
    ])
]

Sector3SecurityZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Level 2 Security Room", True, [
        HasKeycard2(),
        PONRRequirement("PONR - Vanilla Path to Level 2 Security", [
            CanBomb()
        ], [
            HasSpeedBooster()
        ])
    ]),
    FusionLocation("Sector 3 (PYR) -- Security Access", False, [
        CanDamageToughEnemy("Kill Sidehoppers then Jump Up", [
            CanJumpHigh(),
            CanDoSimpleWallJump()
        ]),
        CanDoAdvancedShinespark("Charge from above then go below")
    ])
]

Sector3MainShaft.locations = [
    FusionLocation("Sector 3 (PYR) -- Namihe's Lair", False, [
        CanPowerBomb("Enter Namihe's Lair and Grab Item", [
            HasHiJump(),
            CanFreezeEnemies(),
            # PONRRequirement("PONR - Namihe's Lair - No Witnesses", [
            #     HasScrewAttack(),
            #     CanDamageToughEnemy()
            # ], [
            #     #future CanDoAdvancedJumpBombJump()
            # ]),
            PONRRequirement("PONR - Namihe's Lair - Shinespark", [
                CanDoAdvancedShinespark()
            ])
        ])
    ]),
    FusionLocation("Sector 3 (PYR) -- Processing Access", False, [
        HasKeycard2("Grab Hidden Block Item")
    ]),
]

Sector3BoilerZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Lava Maze", False, [
        CanPowerBomb("Grab Lava Maze Item", [
            CanLavaDive()
        ])
    ]),
    FusionLocation("Sector 3 (PYR) -- Main Boiler Control Room -- Boiler", True, [
        CanDoBoiler()
    ]),
    FusionLocation("Sector 3 (PYR) -- Main Boiler Control Room -- Core X", True, [
        CanDoBoiler()
    ]),
]

Sector3BobZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Bob's Abode", False, []),
]

Sector3BOXZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Data Room", True, [
        CanFightBOX(None, [
            HasKeycard2()
        ])
    ]),
    FusionLocation("Sector 3 (PYR) -- Geron's Treasure", False, [
        CanDamageMediumGeron(),
        CanDamageAnyGeron()
    ])
]

Sector3LowerAttic.locations = [
    FusionLocation("Sector 3 (PYR) -- Alcove -- Lower Item", False, [
        CanClimbSector3Attic()
    ]),
    FusionLocation("Sector 3 (PYR) -- Alcove -- Upper Item", False, [
        CanPowerBomb()
    ]),
]

Sector3UpperAttic.locations = [
    FusionLocation("Sector 3 (PYR) -- Deserted Runway", False, [
        HasSpeedBooster()
    ]),
]

Sector3SovaProcessing.locations = [
    FusionLocation("Sector 3 (PYR) -- Sova Processing -- Left Item", False, [
        CanGetSovaProcessingItem(None, [
            CanBallJump()
        ])
    ]),
    FusionLocation("Sector 3 (PYR) -- Sova Processing -- Right Item", False, [
        CanGetSovaProcessingItem()
    ]),
    FusionLocation("Sector 3 (PYR) -- Garbage Chute -- Lower Item", False, [
        CanLavaDive("Ascend Sector 3 Garbage Chute", [
            CanScrewAttackUnderwater()
        ], [
            CanSpeedBoosterUnderwater()
        ])
    ]),
    FusionLocation("Sector 3 (PYR) -- Garbage Chute -- Upper Item", False, [
        CanLavaDive("Ascend Sector 3 Garbage Chute", [
            CanScrewAttackUnderwater()
        ], [
            CanSpeedBoosterUnderwater()
        ])
    ])
]
