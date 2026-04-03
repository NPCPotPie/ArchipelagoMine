from ..Connection import Connection
from ..FusionLocation import FusionLocation
from ..regions.MainDeck import *
from ..regions.Sector1 import Sector1Hub
from ..regions.Sector2 import Sector2Hub, Sector2NettoriZone
from ..regions.Sector3 import Sector3Hub
from ..regions.Sector4 import Sector4Hub
from ..regions.Sector5 import Sector5Hub
from ..regions.Sector6 import Sector6Hub
from ..Requirement import PONRRequirement
from ..Requirements import *
from ..VariableConnection import VariableConnection

# Region Connections
AuxiliaryReactor.connections = [
    Connection(ReactorZone, [], one_way=True),
    Connection(YakuzaZone, [PONRRequirement()], one_way=True)
]

HabitationDeckElevatorBottom.connections = [
    VariableConnection(HabitationDeckElevatorTop, [Requirement("Use Elevator")])
]

HabitationDeckElevatorTop.connections = [
    VariableConnection(HabitationDeckElevatorBottom, [Requirement("Use Elevator")]),
    Connection(HabitationDeck, [HasKeycard2("Open Door with Level 2 Keycard")])
]

MainDeckHub.connections = [
    Connection(OperationsDeckElevatorBottom, [Requirement("Traverse to Elevator")]),
    Connection(VentilationZone, [
        CanDamageSmallGeron("Kill Lower Vent Geron"),
        CanDamageAnyGeron("Kill Lower Vent Geron with NerfGeronWeakness Disabled")
    ]),
    Connection(LowerArachnusArena, [HasMorph("Can Enter and Leave Arachnus Fight Arena")]),
    Connection(UpperArachnusArena, [
        HasMorph("Use Hidden Screw Attack Tunnel",
                 ["Screw Attack"],
                 [CanJumpHigh(), CanDoSimpleWallJump()]
                 )
    ]),
    Connection(HabitationDeckElevatorBottom, [HasKeycard2("Open Elevator Door with Level 2 Keycard")]),
    Connection(SectorHubElevatorTop, [
        HasMorph("Use Morph Tunnel"),
        CanDoAdvancedShinespark("Can Shinespark to Sector Hub Elevator")
    ]),
    Connection(ReactorZone, [
        HasMorph("Can Enter Reactor Zone",
                 [],
                 [HasKeycard4("Open Door to Reactor Zone with Level 4 Keycard"),
                  CanPowerBomb("Can Blow Up Wall to Reactor Zone")],
                 [],
                 level_2_e_tanks
                 )
    ]),
    Connection(NexusStorage, [
        HasKeycard2("Can Enter Nexus Storage",[],[CanDamageLargeGeron(), CanDamageAnyGeron()])
    ])
]

OperationsDeckElevatorBottom.connections = [
    VariableConnection(OperationsDeckElevatorTop, [Requirement("Use Elevator")])
]

OperationsDeckElevatorTop.connections = [
    VariableConnection(OperationsDeckElevatorBottom, [Requirement("Use Elevator")]),
    Connection(OperationsDeck, [Requirement("Open Door")])
]

OperationsDeck.connections = [
    Connection(VentilationZone, [HasMissile("Can Break Ventilation Cap")], one_way=True)
]

ReactorZone.connections = [
    Connection(YakuzaZone, [
        PONRRequirement("PONR - Can Access Yakuza - Vanilla Route",
                        [],
                        [
                            CanDamageToughEnemy("Can Kill Kihunter, Pirate, and Eyedoor, and Enter Yakuza Arena",
                                                ["Morph Ball"],
                                                [CanBomb(), CanPowerBomb(), HasWaveBeam()])
                        ]),
        HasSpaceJump("Can Access Yakuza - Vanilla Route",
                     [],
                     [
                         CanDamageToughEnemy("Can Kill Kihunter, Pirate, and Eyedoor, and Enter Yakuza Arena",
                                             ["Morph Ball"],
                                             [CanBomb(), CanPowerBomb(), HasWaveBeam()])
                     ]),
    ], one_way=True),
    Connection(AuxiliaryReactor, [HasWaveBeam("Can Open Auxiliary Gate Backwards")]),
    Connection(Sector2NettoriZone, [
        HasSpaceJump("Can Get to Sector 2 Backdoor", [], [
            CanDamageToughEnemy("Can Kill Kihunter", [], [
                CanBomb("Traverse Tunnel with Bomb"),
                CanPowerBomb("Traverse Tunnel with Power Bomb")
            ])
        ])
    ], one_way=True)
]

SectorHubElevatorTop.connections = [
    Connection(MainDeckHub, [
        PONRRequirement("PONR - Enter Main Deck Hub with Speed Booster - Trickless",["Speed Booster"])
    ], one_way=True),
    VariableConnection(SectorHubElevatorBottom, [Requirement("Use Elevator")])
]

SectorHubElevatorBottom.connections = [
    VariableConnection(SectorHubElevatorTop, ["Use Central Elevator"]),
    Connection(SectorHubElevator1Top, ["Open Door"]),
    Connection(SectorHubElevator2Top, ["Open Door"]),
    Connection(SectorHubElevator3Top, [SectorHubLevel1KeycardRequirement("Open Door with Level 1 Keycard")]),
    Connection(SectorHubElevator4Top, [SectorHubLevel1KeycardRequirement("Open Door with Level 1 Keycard")]),
    Connection(SectorHubElevator5Top, [SectorHubLevel1And2KeycardRequirement("Open Door with Level 2 Keycard")]),
    Connection(SectorHubElevator6Top, [SectorHubLevel1And2KeycardRequirement("Open Door with Level 2 Keycard")])
]

SectorHubElevator1Top.connections = [
    VariableConnection(Sector1Hub, [Requirement("Use Elevator")])
]

SectorHubElevator2Top.connections = [
    VariableConnection(Sector2Hub, [Requirement("Use Elevator")])
]

SectorHubElevator3Top.connections = [
    VariableConnection(Sector3Hub, [Requirement("Use Elevator")])
]

SectorHubElevator4Top.connections = [
    VariableConnection(Sector4Hub, [Requirement("Use Elevator")])
]

SectorHubElevator5Top.connections = [
    VariableConnection(Sector5Hub, [Requirement("Use Elevator")])
]

SectorHubElevator6Top.connections = [
    VariableConnection(Sector6Hub, [Requirement("Use Elevator")])
]

UpperArachnusArena.connections = [
    Connection(LowerArachnusArena, [
        PONRRequirement("PONR - Vanilla Route"),
        HasMorph("Vanilla Route")
    ], one_way=True),
    Connection(MainDeckHub, [
        HasScrewAttack("Use Screw Attack Tunnel, then exit left", ["Morph Ball"])
    ], one_way=True)
]

VentilationZone.connections = [
    Connection(UpperArachnusArena, [
        PONRRequirement("PONR - Kill Eyedoor", [], [CanDamageToughEnemy()]),
        CanDamageToughEnemy("Kill Eyedoor", ["Morph Ball"])
    ], one_way=True)
]

YakuzaZone.connections = [
    Connection(AuxiliaryReactor, [HasSpaceJump("Leave Yakuza Arena")])
]

# Item Locations
AuxiliaryReactor.locations = [
    FusionLocation("Main Deck -- Auxiliary Power Station", True, [Requirement("Use Terminal")])
]

HabitationDeck.locations = [
    FusionLocation("Main Deck -- Habitation Deck -- Animals", True, [
        HasSpaceJump("Vanilla Route with Space Jump",
                     ["Speed Booster", "Level 2 Keycard"]),
        CanFreezeEnemies("Vanilla Route",
                         ["Level 2 Keycard", "Speed Booster"],
                         [HasHiJump(), CanDoAdvancedWallJump()]),
        CanFreezeEnemies("Backwards Gates on Lower Floor",
                         ["Level 2 Keycard", "Wave Beam"],
                         [HasHiJump(), CanDoSimpleWallJump()])
    ]),
    FusionLocation("Main Deck -- Habitation Deck -- Lower Item", False, [
        HasSpaceJump("Vanilla Route with Space Jump", ["Level 2 Keycard"]),
        HasWaveBeam("Backwards Gates on Lower Floor", ["Level 2 Keycard"]),
        CanFreezeEnemies("Vanilla Route",
                         ["Level 2 Keycard"],
                         [HasHiJump(), CanDoAdvancedWallJump()])
    ])
]

LowerArachnusArena.locations = [
    FusionLocation("Main Deck -- Arachnus Arena -- Core X", True, [CanDamageCoreX()])
]

MainDeckHub.locations = [
    FusionLocation("Main Deck -- Cubby Hole", False, [HasMorph()]),
    FusionLocation("Main Deck -- Genesis Speedway", False, [
        CanPowerBomb("Vanilla", [], [CanBallJump(), CanDoSimpleWallJump()])
    ]),
    FusionLocation("Main Deck -- Quarantine Bay", False, [Requirement("First X Kill")]),
    FusionLocation("Main Deck -- Station Entrance", False, [CanPowerBomb("Blow Up the Floor")]),
    FusionLocation("Main Deck -- Sub-Zero Containment", False, [
        HasKeycard3("Open Door with Level 3 Keycard", ["Varia Suit"])
    ])
]

NexusStorage.locations = [
    FusionLocation("Main Deck -- Nexus Storage", False, [
        CanBallJump("Enter Tunnel and Bomb Out", [], [CanBomb(), CanPowerBomb()])
    ])
]

OperationsDeck.locations = [
    FusionLocation("Main Deck -- Operations Deck Data Room", True, [Requirement("Download Missiles")])
]

ReactorZone.locations = [
    FusionLocation("Main Deck -- Silo Catwalk", False, [CanDamageToughEnemy("Kill Pirates")]),
    FusionLocation("Main Deck -- Silo Scaffolding", False, [
        PONRRequirement("Can't Jump Good",
                        ["Morph Ball"],
                        [CanDamageToughEnemy("Kill Pirates")]),
        CanDamageToughEnemy("Kill Pirates and Leave",
                            ["Morph Ball"],
                            [CanJumpHigh(), CanDoAdvancedWallJump()])
    ])
]

SectorHubElevatorTop.locations = [
    FusionLocation("Main Deck -- Main Elevator Cache", False, [HasSpeedBooster()])
]

UpperArachnusArena.locations = [
    FusionLocation("Main Deck -- Arachnus Arena -- Upper Item", False, [
        Requirement("Can't Miss It")
    ]),
    FusionLocation("Main Deck -- Attic", False, [HasMissile("Blast Open the Ceiling")]),
]

VentilationZone.locations = [
    FusionLocation("Main Deck -- Operations Ventilation", False, [
        Requirement("Can't Miss It")
    ]),
    FusionLocation("Main Deck -- Operations Ventilation Storage", False, [
        Requirement("In a Hidden Block")
    ])
]

YakuzaZone.locations = [
    FusionLocation("Main Deck -- Yakuza Arena", True, [
        CanFightMidGameBoss(),
        CanFightMidGameBossOnAdvanced()
    ])
]
