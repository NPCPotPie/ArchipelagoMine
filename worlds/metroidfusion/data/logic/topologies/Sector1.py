from ..Connection import Connection
from ..Requirement import PONRRequirement
from ..VariableConnection import VariableConnection
from ..Requirements import *
from ..FusionLocation import FusionLocation

from ..regions.MainDeck import SectorHubElevator1Top
from ..regions.Sector1 import *
from ..regions.Sector2 import Sector2TubeLeft
from ..regions.Sector3 import Sector3TubeRight
from ..regions.Sector6 import Sector6RestrictedZoneElevatorToTourian

# Region Connections
Sector1AfterChargeCoreZone.connections = [
    Connection(Sector1FirstStabilizerZone, [Requirement("Shutter Gate")], one_way=True)
]

Sector1Antechamber.connections = [
    Connection(Sector1Hub, [
        HasKeycard2("Enter Antechamber - Bottom Half and Open Door", ["Screw Attack"])
    ], one_way=True),
    Connection(Sector1TubeRight, [HasMorph("Secret Tunnel")], one_way=True)
]

Sector1ChargeCoreZone.connections = [
    Connection(Sector1AfterChargeCoreZone, [HasMissile("Have to Kill Beam Core X")])
]

Sector1FirstStabilizerZone.connections = [
    Connection(Sector1SecondStabilizerZone, []),
    Connection(Sector1AfterChargeCoreZone, [HasWaveBeam("Backwards Travel")]),
]

Sector1FourthStabilizerZone.connections = [
    Connection(Sector1ChargeCoreZone, [
        Requirement("Enter Charge Core Zone",
                    ["Morph Ball"],
                    0,
                    [
                        HasMissile("License to Kill"),
                        PONRRequirement("PONR - Enter Charge Core Zone", ["Charge Beam"])
                    ])
    ], one_way=True),
]

Sector1Hub.connections = [
    VariableConnection(SectorHubElevator1Top, [Requirement("Use Elevator")]),
    Connection(Sector1Antechamber, [
        HasKeycard2("Enter Antechamber - Top Half",
                    ["Screw Attack"],
                    0,
                    [
                        HasSpaceJump("Fly"),
                        CanDoAdvancedWallJump("Jump Good", ["Hi-Jump"])
                    ])
    ]),
    Connection(Sector1TubeLeft, [
        HasKeycard1("Can Approach West Tube from Top Door",
                    ["Morph Ball", "Screw Attack"]
                    )
    ]),
    Connection(Sector1FirstStabilizerZone, [
        CanDamageSmallGeron("Atmospheric Stabilizer NW - Vanilla Kill"),
        CanDamageAnyGeron("Atmospheric Stabilizer NW - Alternate Kill"),
        CanDoAdvancedShinespark("Atmospheric Stabilizer NW - Shinespark Kill")
    ]),
    Connection(Sector1SecondStabilizerZone, [
        CanLavaDive("Cut Through Lava Pool",["Level 1 Keycard", "Level 2 Keycard"])
    ]),
]

Sector1SecondStabilizerZone.connections = [
    Connection(Sector1ThirdStabilizerZone, [CanDamageStabilizer(), CanDamageAnyGeron()])
]

Sector1ThirdStabilizerZone.connections = [
    Connection(Sector1FourthStabilizerZone, [CanDamageStabilizer(), CanDamageAnyGeron()]),
    Connection(Sector1TourianExit, [
        Requirement("Enter Tourian Exit from Stabilizers",
                       ["Morph Ball", "Screw Attack"],
                       level_4_e_tanks,
                       [
                           PONRRequirement("PONR - Enter Tourian Exit from Stabilizers",
                                           [],
                                           0,
                                           [CanFreezeEnemies("Use Rippers as platforms")]),
                           HasSpaceJump("Fly")
                       ]),
    ], one_way=True)
]

Sector1TourianExit.connections = [
    Connection(Sector1ThirdStabilizerZone, [
        Requirement("Break Out of Tourian Exit toward Stabilizers",
                    ["Space Jump", "Wave Beam", "Morph Ball"],
                    level_4_e_tanks,
                    [
                        # Must defeat SW or SE Stabilizers
                        CanDamageStabilizer(),
                        CanDamageAnyGeron()
                    ]),
    ], one_way=True),
    Connection(Sector1TourianHub, [
        Requirement("Break Into Tourian from Exit",
                    ["Missile Data", "Screw Attack", "Morph Ball"],
                    level_3_e_tanks,
                    [
                        HasSpaceJump("Fly"),
                        CanDoSimpleWallJump()
                    ], [
                        HasWaveBeam("Can Open Shutter Gate Backwards"),
                        PONRRequirement("PONR - Break Into Tourian from Exit")
                    ])
    ], one_way=True)
]

Sector1TourianHub.connections = [
    Connection(Sector1TourianExit, [
        HasMissile("Open and Enter Tunnel to Tourian Exit",
                   ["Morph Ball", "Screw Attack", "Wave Beam"],
                   level_4_e_tanks,
                   [
                       HasSpaceJump(),
                       CanDoAdvancedWallJump()
                   ])
    ]),
    Connection(Sector1TourianHubElevatorTop, [
        Requirement("Traverse Tourian Hub to/from Tourian Elevator",
                    [],
                    level_4_e_tanks,
                    [
                        HasSpaceJump(),
                        CanDoSimpleWallJump()
                    ], [
                        # Pinnacle of Movement and Avoidance
                        CanDoExpertCombat(),
                        CanDoAdvancedCombat(None,
                                            [],
                                            0,
                                            [
                                                CanDamageToughEnemy("Kill Pirate and Kill/Stun Gerubus")
                                            ], [
                                                HasIceBeam("Freeze Ripper")
                                            ]),
                        Requirement("Trickless Combat",
                                    ["Missile Data"],
                                    0,
                                    [
                                        CanFreezeEnemies(),
                                        HasScrewAttack("Kill Everything")
                                    ])
                    ])
    ])
]

Sector1TourianHubElevatorTop.connections = [
    VariableConnection(Sector6RestrictedZoneElevatorToTourian, [Requirement("Use Elevator")]),
    Connection(Sector1TourianHub, [
        PONRRequirement("PONR - Leaving Tourian Elevator", [], level_4_e_tanks)
    ], one_way=True)
]

Sector1TubeLeft.connections = [
    VariableConnection(Sector3TubeRight, [])
]

Sector1TubeRight.connections = [
    Connection(Sector1Antechamber, [CanBallJump("Jump Into Tunnel")]),
    VariableConnection(Sector2TubeLeft, [])
]

# Item Locations
Sector1AfterChargeCoreZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Crab Rave", False, [
        HasMorph("Enter Crab Rave", ["Missile Data"])
    ])
]

Sector1Antechamber.locations = [
    FusionLocation("Sector 1 (SRX) -- Antechamber", False, [])
]

Sector1ChargeCoreZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Charge Core Arena -- Core X", True, [
        CanFightEarlyGameBoss()
    ]),
    FusionLocation("Sector 1 (SRX) -- Charge Core Arena -- Upper Item", False, [
        Requirement("Obtain Charge Core Upper Item",
                    ["Speed Booster"],
                    0,
                    [
                        CanFightEarlyGameBoss("Kill the Core X First"),
                        PONRRequirement("PONR - Obtain Charge Core Upper Item")
                    ])
    ]),
    FusionLocation("Sector 1 (SRX) -- Watering Hole", False, [
        CanBallJump("Grab Watering Hole Item",
                    [],
                    0,
                    [
                        CanSpeedBoosterUnderwater(),
                        # When new trick level is ready
                        # Video proof: https://www.youtube.com/watch?v=7CrmoeqlIUk
                        # CanDoExpertShinespark("Watering Hole - The 7 Frame Window", ["Charge Beam", "Speed Booster"])
                    ], [
                        CanDoAdvancedShinespark("Avoid the Crab"),
                        CanDoBeginnerShinespark("Alternate Kill the Crab",
                                                [],
                                                0,
                                                [
                                                    HasWaveBeam(),
                                                    HasMissile(),
                                                    CanPowerBomb()
                                                ]),
                        Requirement("Trickless - Kill the Crab",
                                    [],
                                    0,
                                    [
                                        HasScrewAttack(),
                                        HasChargeBeam(),
                                        HasPlasmaBeam()
                                    ])
                    ])
    ])
]

Sector1FirstStabilizerZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Atmospheric Stabilizer Northeast", False, [
        Requirement("Collect Atmospheric Stabilizer NE Item",
                    [],
                    0,
                    [
                        PONRRequirement("PONR - Collect Atmospheric Stabilizer NE Item"),
                        CanDamageStabilizer("Atmospheric Stabilizer NE - Vanilla Kill"),
                        CanDamageAnyGeron("Atmospheric Stabilizer NE - Alternate Kill"),
                        CanDoAdvancedShinespark("Atmospheric Stabilizer NE - Shinespark Kill"),
                    ])
    ]),
    FusionLocation("Sector 1 (SRX) -- Hornoad Hole", False, [HasMorph("Secret Tunnel")]),
    FusionLocation("Sector 1 (SRX) -- Wall Jump Tutorial", False, [
        HasMorph("Enter Wall Jump Tutorial",
                 [],
                 0,
                 [HasWallJump(), HasSpaceJump()]),
        CanBallJump("Enter Wall Jump Tutorial - Skill Issue",
                    [],
                    0,
                    [HasWallJump(), HasSpaceJump()])
    ])
]

Sector1FourthStabilizerZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Stabilizer Storage", False, [
        CanDamageStabilizer("Can Kill Atmospheric Stabilizer SE - Vanilla"),
        CanDamageAnyGeron("Can Kill Atmospheric Stabilizer SE - Alternate",
                          [],
                          0,
                          [
                              HasHiJump(),
                              CanDoSimpleWallJump(),
                              CanPowerBomb()
                          ])
    ])
]

Sector1SecondStabilizerZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Lower Item", False, [
        CanLavaDive("Lava Bath - Enter Tunnel", ["Morph Ball"])
    ]),
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Upper Left Item", False, [
        HasSpaceJump("Lava Lake Far Shelf - Fly"),
        CanDoBeginnerShinespark("Lava Lake Far Shelf - Shinespark")
    ]),
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Upper Right Item", False, []),
]

Sector1TourianHub.locations = [
    FusionLocation("Sector 1 (SRX) -- Animorphs Cache", False, [
        CanDamageToughEnemyThroughWalls("Kill the Yard",
                                        [],
                                        0,
                                        [
                                            # Awaiting ammo requirement implementation
                                            # HasMissile()
                                            CanUseSuperMissile("Kill the Gerubus and Golden Pirate"),
                                            HasScrewAttack("Kill the Gerubus and Golden Pirate")
                                        ], [
                                            PONRRequirement("PONR - Enter and Collect Animorphs"),
                                            HasSpaceJump("Fly out of Animorphs Cache"),
                                            CanDoSimpleWallJump("Wall Jump out of Animorphs Cache", ["Hi-Jump"])
                                        ])
    ]),
    FusionLocation("Sector 1 (SRX) -- Neo-Ridley Arena", True, [
        Requirement("Enter Neo-Ridley Arena",
                    [],
                    0,
                    [
                        # Destroy Bomb Wall
                        CanBomb(),
                        CanPowerBomb()
                    ], [
                        # Can Kill Genesis under floor
                        HasWaveBeam(),
                        CanPowerBomb()
                    ], [
                        # Can Kill Golden Pirates
                        CanDamageToughEnemy(),
                        HasScrewAttack()
                    ], [
                        # Do Ridley Fight
                        CanFightMidGameBoss("Ridley Trickless",
                                             [],
                                             level_4_e_tanks,
                                             [CanUseAllMissileUpgrades()],
                                             [CanUseAllBeamUpgrades()]),
                        CanFightLateGameBossOnAdvanced("Ridley On Advanced",["Plasma Beam"]),
                        CanFightBossOnExpert("Ridley On Expert")
                    ], [
                        HasSpaceJump("Can Leave Neo-Ridley Arena"),
                        PONRRequirement("PONR - Neo-Ridley Arena")
                    ])
    ]),
    FusionLocation("Sector 1 (SRX) -- Ripper Maze", False, [
        Requirement("Collect Ripper Maze Item",
                    ["Missile Data", "Morph Ball"],
                    0,
                    [
                        CanBallJump("Can Leave after Ripper Maze Item"),
                        PONRRequirement("PONR - Ripper Maze Item")
                    ], [
                        # Mobility Requirements
                        HasSpaceJump(),
                        CanDoSimpleWallJump()
                    ], [
                        # Dealing with Rippers
                        CanFreezeEnemies(),
                        HasScrewAttack()
                    ], [
                        CanUseDiffusionMissile(),
                        # Can be done without Diffusion. Awaiting trick identity
                        # HasMissile()
                    ])
    ])
]
