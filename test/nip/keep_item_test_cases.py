BNIP_KEEP_TESTS = {
    # monarch
    "PD2_0lR7EfbRGT": [
        {
            "expression": "[name] == Monarch && [quality] == magic && [flag] != ethereal # [sockets] >= 4 && [toblock] >= 20 && [fbr] >= 30",
            "should_keep": True
        },
        {
            "expression": "[name] == Monarch && [quality] == magic && [flag] != ethereal # [defense] > 150",
            "should_keep": False
        },
        {
            "expression": "[name] == Monarch && [quality] == magic",
            "should_keep": True
        },
        {
            "expression": "[name] == Monarch && [flag] == ethereal",
            "should_keep": False
        },
        {
            "expression": "[type] == anyshield",
            "should_keep": True
        },
        {
            "expression": "[type] == shield",
            "should_keep": True
        },
        {
            "expression": "[type] == assassinclaw",
            "should_keep": False
        },
    ],
    # ettin axe
    "PD2_1HfJDuUXhe": [
        {
            "expression": "[name] == EttinAxe && [quality] == normal && [flag] == ethereal",
            "should_keep": True
        },
        {
            "expression": "[type] == axe && [quality] == normal && [flag] == ethereal",
            "should_keep": True
        },
        {
            "expression": "[type] == assassinclaw && [quality] == normal && [flag] == ethereal",
            "should_keep": False
        },
        {
            "expression": "[type] == meleeweapon",
            "should_keep": True
        },
    ],
    # rare bec-de-corbin
    "PD2_1ZMKfTQO7Q": [
        {
            "expression": "[name] == BecdeCorbin && [quality] == rare && [flag] != ethereal # [enhanceddamage] >= 61 && [tohit] >= 71 && [lightresist] >= 8 && [plusmindamage] >= 18 && [manaleech] >= 9 && [itemchargedskill] == 126",
            "should_keep": True
        },
        {
            "expression": "[name] == BecdeCorbin # [enhanceddamage] >= 61",
            "should_keep": True
        },
        {
            "expression": "[name] == BecdeCorbin # [tohit] >= 71",
            "should_keep": True
        },
        {
            "expression": "[name] == BecdeCorbin # [plusmindamage] >= 18",
            "should_keep": True
        },
        {
            "expression": "[name] == BecdeCorbin # [manaleech] >= 9",
            "should_keep": True
        },
        {
            "expression": "[name] == BecdeCorbin # [enhanceddamage] >= 65",
            "should_keep": False
        },
        {
            "expression": "[name] == BecdeCorbin # [lightresist] >= 8",
            "should_keep": True
        },
        {
            "expression": "[name] == BecdeCorbin # [itemchargedskill] == 126",
            "should_keep": True
        },
        {
            "expression": "[name] == BecdeCorbin # [itemchargedskill] == 127",
            "should_keep": False
        },
    ],
    # white phase blade
    "PD2_3BGDpVHQQS": [
        {
            "expression": "[name] == PhaseBlade && [quality] == normal && [flag] != ethereal",
            "should_keep": True
        },
        {
            "expression": "[name] == PhaseBlade && [quality] == normal && [flag] == ethereal",
            "should_keep": False
        },
        {
            "expression": "[name] == PhaseBlade && [quality] == normal",
            "should_keep": True
        },
        {
            "expression": "[name] == PhaseBlade",
            "should_keep": True
        },
        {
            "expression": "[type] == shield",
            "should_keep": False
        },
    ],
    # shako
    "PD2_4IPy7u4fwt": [
        {
            "expression": "[Name] == Shako && [quality] == unique && [flag] != ethereal",
            "should_keep": True
        },
        {
            "expression": "[Name] == Shako && [quality] == unique # [itemmagicbonus] > 51",
            "should_keep": False
        },
        {
            "expression": "[Name] == Shako && [quality] == unique # [itemallskills] >= 2",
            "should_keep": True
        },
        {
            "expression": "[Name] == Shako && [quality] == unique # [allstats] >= 2",
            "should_keep": True
        },
        {
            "expression": "[Name] == Shako && [quality] == unique # [strength] == 2 && [dexterity] == 2 && [energy] == 2",
            "should_keep": True
        },
            {
            "expression": "[Name] == Shako && [quality] == unique # [damageresist] == 10",
            "should_keep": True
        },
    ],
    # rare ring
    "PD2_5vhnOkej0W": [
        {
            "expression": "[name] == Ring && [quality] == rare && [flag] != ethereal # [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 44 && [itemmagicbonus] >= 10 && [lightresist] >= 30 && [dexterity] >= 15 && [fcr] >= 10 && [maxhp] >= 40",
            "should_keep": True
        },
        {
            "expression": "[name] == Ring && [quality] == rare # [itemmagicbonus] >= 10 && [dexterity] >= 15 && [fcr] >= 10 && [maxhp] >= 40",
            "should_keep": True
        },
        {
            "expression": "[name] == Ring && [quality] == rare # [lightresist] >= 30 && [maxhp] >= 40",
            "should_keep": True
        },
        {
            "expression": "[name] == Ring && [quality] == rare && [flag] == ethereal",
            "should_keep": False
        },
        {
            "expression": "[name] == Ring && [quality] == unique",
            "should_keep": False
        },
    ],
    # magic feral claws
    "PD2_6AHfXLJO4l": [
        {
            "expression": "[name] == FeralClaws && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [ias] >= 40 && [skillLightningSentry] >= 3 && [skillDeathSentry] >= 3 && [skillFade] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == FeralClaws && [quality] == magic && [flag] != ethereal",
            "should_keep": True
        },
        {
            "expression": "[name] == FeralClaws # [itemaddskilltab] >= 4",
            "should_keep": False
        },
        {
            "expression": "[name] == FeralClaws && [quality] == magic && [flag] != ethereal # [ias] >= 40",
            "should_keep": True
        },
        {
            "expression": "[name] == FeralClaws && [quality] == magic && [flag] != ethereal # [ias] >= 41",
            "should_keep": False
        },
        {
            "expression": "[type] == assassinclaw && [class] == elite",
            "should_keep": True
        },
        {
            "expression": "[type] == assassinclaw && [class] == exceptional",
            "should_keep": False
        },
    ],
    # rare cantor trophy
    "PD2_7CAuD9VcLh": [
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [itemaddskilltab] >= 2 && [itemarmorperlevel] >= 4 && [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 80 && [itemreplenishdurability] >= 1 && [poisonmindam] >= 13 && [poisonmaxdam] >= 28 && [skillBoneSpirit] >= 3 && [skillBoneSpear] >= 3 && [skillBoneWall] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [skillBoneSpear] >= 3 && [skillBoneWall] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [itemaddskilltab] >= 2",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [itemreplenishdurability] >= 1",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [poisonmindam] >= 13 && [poisonmaxdam] >= 28",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 80",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [allres] >= 20",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [allres] >= 21",
            "should_keep": False
        },
    ],
    # magic matriarchal spear
    "PD2_7ov1FGVkvQ": [
        {
            "expression": "[name] == MatriarchalSpear && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 6 && [ias] >= 40",
            "should_keep": True
        },
        {
            "expression": "[type] == amazonspear",
            "should_keep": True
        },
    ],
    # rare arbalest
    "PD2_7wqOnPKCxN": [
        {
            "expression": "[name] == Arbalest && [quality] == rare && [flag] != ethereal # [coldmindam] >= 35 && [coldmaxdam] >= 116 && [lightresist] >= 26 && [poisonmindam] >= 150 && [plusmaxdamage] >= 1 && [lightmindam] >= 1 && [lightmaxdam] >= 29 && [itemchargedskill] == 12",
            "should_keep": True
        },
        {
            "expression": "[name] == Arbalest && [quality] == rare && [flag] != ethereal # [coldmindam] >= 35 && [coldmaxdam] >= 116",
            "should_keep": True
        },
        {
            "expression": "[name] == Arbalest && [quality] == rare && [flag] != ethereal # [plusmaxdamage] >= 1",
            "should_keep": True
        },
        {
            "expression": "[name] == Arbalest && [quality] == rare && [flag] != ethereal # [lightmindam] >= 1 && [lightmaxdam] >= 29 && [itemchargedskill] == 12",
            "should_keep": True
        },
        {
            "expression": "[name] == Arbalest && [quality] == rare && [flag] != ethereal # [itemchargedskill] == 12",
            "should_keep": True
        },
        {
            "expression": "[name] == Arbalest && [quality] == rare && [flag] != ethereal",
            "should_keep": True
        },
        {
            "expression": "[name] == Arbalest && [quality] == rare && [flag] != ethereal # [poisonmindam] >= 150",
            "should_keep": True
        },
    ],
    # giant thresher eth
    "PD2_60FdSnzNbq": [
        {
            "expression": "[name] == GiantThresher && [quality] <= superior && [flag] == ethereal",
            "should_keep": True
        },
    ],
    # blue mighty scepter
    "PD2_65KHCMvsK6": [
        {
            "expression": "[name] == MightyScepter && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [fcr] >= 10 && [skillHolyShock] >= 3 && [skillFistoftheHeavens] >= 3 && [skillConviction] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == MightyScepter && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == MightyScepter && [quality] == magic && [flag] != ethereal # [fcr] >= 10",
            "should_keep": True
        },
        {
            "expression": "[name] == MightyScepter && [quality] == magic && [flag] != ethereal # [skillHolyShock] >= 3 && [skillFistoftheHeavens] >= 3 && [skillConviction] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == MightyScepter && [quality] == magic && [flag] != ethereal # [skillHolyShock] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == MightyScepter && [quality] == magic && [flag] != ethereal # [skillFistoftheHeavens] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == MightyScepter && [quality] == magic && [flag] != ethereal # [skillConviction] >= 3",
            "should_keep": True
        },
    ],
    # riphook
    "PD2_a6D8Kmv3uT": [
        {
            "expression": "[Name] == Razorbow && [quality] == unique # [enhanceddamage] >= 220 && [lifeleech] >= 10",
            "should_keep": True
        },
        {
            "expression": "[Name] == Razorbow && [quality] == unique # [lifeleech] >= 10",
            "should_keep": True
        },
        {
            "expression": "[Name] == Razorbow && [quality] == unique # [enhanceddamage] >= 220",
            "should_keep": True
        },
    ],
    # white unearthed wand
    "PD2_ARmKCSdJnI": [
        {
            "expression": "[Name] == UnearthedWand && [quality] == normal && [flag] != ethereal",
            "should_keep": True
        },
    ],
    # chance guards
    "PD2_AUakVcxMGp": [
        {
            "expression": "[name] == ChainGloves && [quality] == unique # [itemgoldbonus] >= 200 && [itemmagicbonus] >= 40",
            "should_keep": True
        },
    ],
    # rare archon staff
    "PD2_bE0gVUl4R7": [
        {
            "expression": "[name] == ArchonStaff && [quality] == rare && [flag] != ethereal # [sorceressskills] >= 2 && [maxmana] >= 76 && [itemdamagetomana] >= 10 && [energy] >= 20 && [ias] >= 20 && [fcr] >= 20 && [skillGlacialSpike] >= 3 && [skillFrozenOrb] >= 3 && [skillColdMastery] >= 3",
            "should_keep": True
        },
    ],
    # rare amulet
    "PD2_cCgyl3NTq9": [
        {
            "expression": "[name] == Amulet && [quality] == rare && [flag] != ethereal # [fireresist] >= 10 && [coldresist] >= 30 && [itemmagicbonus] >= 10 && [itempoisonlengthresist] >= 25 && [magicdamagereduction] >= 3 && [fcr] >= 10",
            "should_keep": True
        },
    ],
    # rare amulet
    "PD2_cCgyl3NTq9": [
        {
            "expression": "[name] == Amulet && [quality] == rare && [flag] != ethereal # [fireresist] >= 10 && [coldresist] >= 30 && [itemmagicbonus] >= 10 && [itempoisonlengthresist] >= 25 && [magicdamagereduction] >= 3 && [fcr] >= 10",
            "should_keep": False
        },
        {
            "expression": "[name] == Amulet && [quality] == rare && [flag] != ethereal # [sorceressskills] >= 2 && [itemdamagetomana] >= 12 && [maxmana] >= 90 && [fcr] >= 10 && [strength] >= 26 && [energy] >= 20",
            "should_keep": True
        },
    ],
    # white flail
    "PD2_cPszZcBC81": [
        {
            "expression": "[name] == Flail && [quality] == normal && [flag] != ethereal",
            "should_keep": True
        },
    ],
    # white large siege bow
    "PD2_d7clAOFrFY": [
        {
            "expression": "[name] == LargeSiegeBow && [quality] == normal && [flag] != ethereal",
            "should_keep": True
        },
    ],
    # magic gladius
    "PD2_DaDAU5n7GJ": [
        {
            "expression": "[name] == Gladius && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [strength] >= 2",
            "should_keep": True
        },
    ],
    # rare ancient axe
    "PD2_dvAVQGnYzc": [
        {
            "expression": "[name] == AncientAxe && [quality] == rare && [flag] == ethereal # [enhanceddamage] >= 350 && [tohit] >= 550 && [ias] >= 40 && [plusmaxdamage] >= 20 && [itemreplenishdurability] >= 1",
            "should_keep": True
        },
    ],
    # magic lich wand
    "PD2_DyLF3Fj0FK": [
        {
            "expression": "[name] == LichWand && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [fcr] >= 20 && [skillBoneSpirit] >= 3 && [skillBoneWall] >= 3 && [skillBoneSpear] >= 3",
            "should_keep": True
        },
    ],
    # magic cloudy sphere
    "PD2_EYVbkOSvLp": [
        {
            "expression": "[name] == CloudySphere && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [fcr] >= 20 && [skillNova] >= 3 && [skillLightningMastery] >= 3 && [skillEnergyShield] >= 3",
            "should_keep": True
        },
    ],
    # white lochaber axe
    "PD2_fBh9PdCvNz": [
        {
            "expression": "[name] == LochaberAxe && [quality] == normal && [flag] != ethereal",
            "should_keep": True
        },
    ],
    # rare amulet
    "PD2_gE6A96ftDw": [
        {
            "expression": "[name] == Amulet && [quality] == rare && [flag] != ethereal # [sorceressskills] >= 2 && [itemdamagetomana] >= 12 && [maxmana] >= 90 && [fcr] >= 10 && [strength] >= 26 && [energy] >= 20",
            "should_keep": False
        },
        {
            "expression": "[name] == Amulet && [quality] == rare && [flag] != ethereal # [fireresist] >= 10 && [coldresist] >= 30 && [itemmagicbonus] >= 10 && [itempoisonlengthresist] >= 25 && [magicdamagereduction] >= 3 && [fcr] >= 10",
            "should_keep": True
        },
    ],
    # rare archon plate
    "PD2_Ghwf32hhjz": [
        {
            "expression": "[name] == ArchonPlate && [quality] == rare && [flag] != ethereal # [coldresist] >= 26 && [fireresist] >= 26 && [lightresist] >= 26 && [hpregen] >= 5 && [dexterity] >= 8 && [strength] >= 18",
            "should_keep": True
        },
    ],
    # ormus robes
    "PD2_gIVrKehVNq": [
        {
            "expression": "[name] == DuskShroud && [quality] == unique # [fcr] >= 20 && [Passivecoldmastery] >= 15 && [Skillfrozenorb] >= 3",
            "should_keep": True
        },
    ],
    # rare ceremonial javelin
    "PD2_GOnpYcQ539": [
        {
            "expression": "[name] == CeremonialJavelin && [quality] == rare && [flag] != ethereal # [enhanceddamage] >= 300 && [amazonskills] >= 2 && [itemmaxdamageperlevel] >= 1 && [itemtohitperlevel] >= 1 && [itemskillonhit] == 66 && [strength] >= 15 && [ias] >= 40 && [itemaddskilltab] >= 2",
            "should_keep": True
        },
    ],
    # magic grand matron bow
    "PD2_gxlIdIHuBX": [
        {
            "expression": "[name] == GrandMatronBow && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 6 && [ias] >= 20",
            "should_keep": True
        },
    ],
    # magic rondache
    "PD2_gZNEsYkfkj": [
        {
            "expression": "[name] == Rondache && [quality] == magic && [flag] != ethereal # [sockets] >= 4 && [toblock] >= 20 && [fbr] >= 30",
            "should_keep": True
        },
    ],
    # rare battle belt
    "PD2_h8bXDXTwYm": [
        {
            "expression": "[name] == BattleBelt && [quality] == rare && [flag] != ethereal # [lightresist] >= 30 && [fireresist] >= 30 && [maxmana] >= 20 && [fhr] >= 24 && [itemgoldbonus] >= 80 && [strength] >= 30",
            "should_keep": True
        },
    ],
    # crown of ages
    "PD2_HPHrNWjUkD": [
        {
            "expression": "[Name] == Corona && [quality] == unique # [sockets] >= 2 && [damageresist] >= 15",
            "should_keep": True
        },
    ],
    # magic gladius
    "PD2_HyHbbZZA1n": [
        {
            "expression": "[name] == Gladius && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [itemchargedskill] == 36",
            "should_keep": True
        },
    ],
    # reaper's toll
    "PD2_I5LbjVIYvy": [
        {
            "expression": "[name] == Thresher && [quality] == unique # [enhanceddamage] >= 220",
            "should_keep": True
        },
    ],
    # magic akaran targe
    "PD2_iEAZAhsn0m": [
        {
            "expression": "[name] == AkaranTarge && [quality] == magic && [flag] != ethereal # [sockets] >= 4 && [toblock] >= 20 && [fbr] >= 30 && [tohit] >= 111 && [enhanceddamage] >= 58",
            "should_keep": True
        },
    ],
    # rare akaran rondache
    "PD2_j91F4T3G0M": [
        {
            "expression": "[name] == AkaranRondache && [quality] == rare && [flag] != ethereal # [enhanceddefense] >= 200 && [sockets] >= 2 && [itemdamagetomana] >= 12 && [normaldamagereduction] >= 7 && [itemreplenishdurability] >= 1 && [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 120",
            "should_keep": True
        },
    ],
    # rare ancient armor
    "PD2_jdSojrLyHn": [
        {
            "expression": "[name] == AncientArmor && [quality] == rare && [flag] != ethereal # [itemarmorperlevel] >= 24 && [sockets] >= 2 && [fireresist] >= 10 && [dexterity] >= 3 && [normaldamagereduction] >= 3 && [fhr] >= 24",
            "should_keep": True
        },
    ],
    # swordback hold
    "PD2_jiUGpeejOO": [
        {
            "expression": "[Name] == Spikedshield && [quality] == unique && [flag] != ethereal # [enhanceddefense] >= 60",
            "should_keep": True
        },
    ],
    # white cedar staff
    "PD2_JKj1ONC0Qo": [
        {
            "expression": "[name] == CedarStaff && [quality] == normal && [flag] != ethereal",
            "should_keep": True
        },
    ],
    # rare alpha helm
    "PD2_JOTQPzIIre": [
        {
            "expression": "[name] == AlphaHelm && [quality] == rare && [flag] != ethereal # [itemtohitpercentperlevel] >= 2 && [enhanceddefense] >= 200 && [maxmana] >= 5 && [itempoisonlengthresist] >= 25 && [maxhp] >= 40 && [itemreplenishdurability] >= 1 && [skillVolcano] >= 3 && [skillFissure] >= 3 && [skillArmageddon] >= 3",
            "should_keep": True
        },
    ],
    # rare alpha helm
    "PD2_JOTQPzIIre": [
        {
            "expression": "[name] == AlphaHelm && [quality] == rare && [flag] != ethereal # [itemtohitpercentperlevel] >= 2 && [enhanceddefense] >= 200 && [maxmana] >= 5 && [itempoisonlengthresist] >= 25 && [maxhp] >= 40 && [itemreplenishdurability] >= 1 && [skillVolcano] >= 3 && [skillFissure] >= 3 && [skillArmageddon] >= 3",
            "should_keep": True
        },
    ],
    # rare antlers
    "PD2_JxJMLkkrcO": [
        {
            "expression": "[name] == Antlers && [quality] == rare && [flag] != ethereal # [druidskills] >= 2 && [sockets] >= 2 && [enhanceddefense] >= 100 && [energy] >= 9 && [maxhp] >= 36 && [fhr] >= 10 && [skillCycloneArmor] >= 3 && [skillRabies] >= 3 && [skillFeralRage] >= 3",
            "should_keep": True
        },
    ],
    # magic long staff
    "PD2_jYVm7kYbXA": [
        {
            "expression": "[name] == LongStaff && [quality] == magic && [flag] != ethereal # [sorceressskills] >= 2 && [fcr] >= 20 && [skillFireMastery] >= 3 && [skillMeteor] >= 3 && [skillFireBall] >= 3",
            "should_keep": True
        },
    ],
    # valkyrie wing
    "PD2_K0SM6iiTyD": [
        {
            "expression": "[name] == WingedHelm && [quality] == unique # [enhanceddefense] >= 200",
            "should_keep": True
        },
    ],
    # magic fury visor
    "PD2_LsXL0Ym8Ys": [
        {
            "expression": "[name] == FuryVisor && [quality] == magic && [flag] != ethereal # [barbarianskills] >= 2 && [maxhp] >= 36 && [skillBattleOrders] >= 3 && [skillWarCry] >= 3 && [skillBattleCommand] >= 3",
            "should_keep": True
        },
    ],
    # magic ring
    "PD2_lVJEBucdd8": [
        {
            "expression": "[name] == Ring && [quality] == magic && [flag] != ethereal # [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 60 && [fcr] >= 10",
            "should_keep": True
        },
        {
            "expression": "[name] == Ring && [quality] == magic && [flag] != ethereal # [allres] >= 15 && [fcr] >= 10",
            "should_keep": True
        },
        {
            "expression": "[name] == Ring && [quality] == magic && [flag] != ethereal # [allres] >= 16 && [fcr] >= 10",
            "should_keep": False
        },
    ],
    # magic maiden javelin
    "PD2_MJjAgKQABC": [
        {
            "expression": "[name] == MaidenJavelin && [quality] == magic && [flag] != ethereal # [amazonskills] >= 2 && [ias] >= 40 && [itemaddskilltab] >= 3",
            "should_keep": True
        },
    ],
    # rare ancient sword
    "PD2_MnN9IaI0NA": [
        {
            "expression": "[name] == AncientSword && [quality] == rare && [flag] != ethereal # [itemaddskilltab] >= 1 && [itemundeadtohit] >= 126 && [itemundeaddamagepercent] >= 101 && [tohit] >= 201 && [enhanceddamage] >= 126 && [ias] >= 40 && [firemindam] >= 15 && [firemaxdam] >= 48 && [itemchargedskill] == 144",
            "should_keep": True
        },
    ],
    # magic eldritch orb
    "PD2_MTB3TGtfgu": [
        {
            "expression": "[name] == EldritchOrb && [quality] == magic && [flag] != ethereal # [maxmana] >= 186 && [fcr] >= 20 && [skillEnergyShield] >= 3 && [skillLightningMastery] >= 3 && [skillChainLightning] >= 3",
            "should_keep": True
        },
    ],
    # rare eth blade talons
    "PD2_O0WUcFkvIA": [
        {
            "expression": "[name] == BladeTalons && [quality] == rare && [flag] == ethereal # [enhanceddamage] >= 350 && [tohit] >= 550 && [ias] >= 40 && [itemreplenishdurability] >= 1 && [plusmaxdamage] >= 20",
            "should_keep": True
        },
        {
            "expression": "[name] == BladeTalons && [quality] == rare && [flag] != ethereal",
            "should_keep": False
        },
    ],
    # magic coronet
    "PD2_o1NZtzmhmF": [
        {
            "expression": "[name] == Coronet && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [fcr] >= 20",
            "should_keep": True
        },
    ],
    # magic griffon headdress
    "PD2_OYgwehN2Ah": [
        {
            "expression": "[name] == GriffonHeaddress && [quality] == magic && [flag] != ethereal # [sockets] >= 3 && [maxhp] >= 40 && [skillVolcano] >= 3 && [skillFissure] >= 3 && [skillArmageddon] >= 3",
            "should_keep": True
        },
    ],
    # doombringer champion sword
    "PD2_PTvvNUuaHq": [
        {
            "expression": "[name] == ChampionSword && [quality] == unique # [enhanceddamage] >= 220",
            "should_keep": True
        },
    ],
    # magic socketed diadem
    "PD2_q45vGxNCeu": [
        {
            "expression": "[name] == Diadem && [quality] == magic && [flag] != ethereal # [sockets] >= 2 && [fcr] >= 20",
            "should_keep": True
        },
        {
            "expression": "[name] == Diadem && [quality] == magic && [flag] != ethereal # [sockets] >= 3",
            "should_keep": False
        },
    ],
    # rare ancient shield
    "PD2_QJo13V7ET2": [
        {
            "expression": "[name] == AncientShield && [quality] == rare && [flag] != ethereal # [enhanceddefense] >= 100 && [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 80 && [itemaddskilltab] >= 1 && [itemskillongethit] == 48 && [toblock] >= 20 && [fbr] >= 30 && [itemreplenishdurability] >= 1",
            "should_keep": True
        },
        {
            "expression": "[name] == AncientShield && [quality] == rare && [flag] != ethereal # [itemskillongethit] == 48",
            "should_keep": True
        },
        {
            "expression": "[name] == AncientShield && [quality] == rare && [flag] != ethereal # [fbr] >= 30",
            "should_keep": True
        },
        {
            "expression": "[name] == AncientShield && [quality] == rare && [flag] != ethereal # [toblock] >= 20",
            "should_keep": True
        },
        {
            "expression": "[name] == AncientShield && [quality] == rare && [flag] != ethereal # [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 80",
            "should_keep": True
        },
        {
            "expression": "[type] == assassinclaw",
            "should_keep": False
        },
    ],
    # wizardspike
    "PD2_qwgERVLYvQ": [
        {
            "expression": "[Name] == BoneKnife && [quality] == unique # [fcr] >= 50",
            "should_keep": True
        },
    ],
    # magic preserved head
    "PD2_tB0MNZqKsc": [
        {
            "expression": "[name] == PreservedHead && [quality] == magic && [flag] != ethereal # [sockets] >= 2 && [toblock] >= 20 && [fbr] >= 30 && [skillIronGolem] >= 3 && [skillPoisonNova] >= 3 && [skillPoisonExplosion] >= 3",
            "should_keep": True
        },
        {
            "expression": "[type] == necromanceritem",
            "should_keep": True
        },
        {
            "expression": "[type] == amazonitem",
            "should_keep": False
        },
    ],
    # magic heavy bracers
    "PD2_UIyDDtROVY": [
        {
            "expression": "[name] == HeavyBracers && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [ias] >= 20",
            "should_keep": True
        },
    ],
    # magic hydra bow
    "PD2_URqU8bUiyv": [
        {
            "expression": "[name] == HydraBow && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 3 && [ias] >= 20",
            "should_keep": True
        },
    ],
    # hellslayer
    "PD2_V4HkMaiIiI": [
        {
            "expression": "[name] == Decapitator && [quality] == unique && [flag] != ethereal # [enhanceddamage] >= 100",
            "should_keep": True
        },
    ],
    # rare cantor trophy
    "PD2_w7DvFnRl6c": [
        {
            "expression": "[name] == CantorTrophy && [quality] == rare && [flag] == ethereal # [itemaddskilltab] >= 2 && [itemarmorperlevel] >= 4 && [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 80 && [toblock] >= 10 && [fbr] >= 15 && [itemreplenishdurability] >= 1 && [itemhalffreezeduration] >= 1 && [skillBoneSpirit] >= 3 && [skillBoneSpear] >= 3 && [skillBoneWall] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy # [itemaddskilltab] >= 2 && [itemarmorperlevel] >= 4",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy # [fireresist]+[coldresist]+[lightresist]+[poisonresist] >= 80",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy # [toblock] >= 10 && [fbr] >= 15",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy # [itemreplenishdurability] >= 1 && [itemhalffreezeduration] >= 1",
            "should_keep": True
        },
        {
            "expression": "[name] == CantorTrophy # [skillBoneSpirit] >= 3 && [skillBoneSpear] >= 3 && [skillBoneWall] >= 3",
            "should_keep": True
        },
    ],
    # magic ballista
    "PD2_wASxol7GDr": [
        {
            "expression": "[name] == Ballista && [quality] == magic && [flag] != ethereal # [poisonresist] >= 26 && [itemchargedskill] == 6",
            "should_keep": True
        },
    ],
    # magefist
    "PD2_wYl0iQwct8": [
        {
            "expression": "[name] == LightGauntlets && [quality] == unique # [fcr] >= 20",
            "should_keep": True
        },
    ],
    # magic ghost glaive
    "PD2_XmiUAD2hC6": [
        {
            "expression": "[name] == GhostGlaive && [quality] == magic && [flag] == ethereal # [enhanceddamage] >= 300 && [itemreplenishquantity] >= 1",
            "should_keep": True
        },
    ],
    # 4os eth cryptic axe
    "PD2_Xmiw3PsbcD": [
        {
            "expression": "[name] == CrypticAxe && [quality] == normal && [flag] == ethereal",
            "should_keep": True
        },
        {
            "expression": "[name] == CrypticAxe && [quality] == normal # [sockets] >= 4",
            "should_keep": True
        },
        {
            "expression": "[name] == CrypticAxe && [quality] == normal && [flag] == ethereal # [sockets] >= 4",
            "should_keep": True
        },
    ],
    # vampgaze
    "PD2_xP50v8yBqQ": [
        {
            "expression": "[name] == GrimHelm && [quality] == unique # [lifeleech] >= 8 && [manaleech] >= 8",
            "should_keep": True
        },
    ],
    # andys
    "PD2_Xq0aFuN5cj": [
        {
            "expression": "[name] == Demonhead && [quality] == unique # [ias] >= 20",
            "should_keep": True
        },
    ],
    # superior mancatcher
    "PD2_YhXVS8Q4j6": [
        {
            "expression": "[name] == ManCatcher && [quality] == superior",
            "should_keep": True
        },
        {
            "expression": "[name] == ManCatcher && [quality] == normal",
            "should_keep": False
        },
    ],
    # rare bone wand
    "PD2_ZI6fzNFd3E": [
        {
            "expression": "[name] == BoneWand && [quality] == rare && [flag] != ethereal # [sockets] >= 2 && [maxmana] >= 76 && [necromancerskills] >= 2 && [fcr] >= 20 && [hpregen] >= 5 && [energy] >= 20 && [skillBoneSpirit] >= 3 && [skillIronGolem] >= 3 && [skillBoneSpear] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == BoneWand # [necromancerskills] >= 2",
            "should_keep": True
        },
        {
            "expression": "[name] == BoneWand # [hpregen] >= 5 && [energy] >= 20",
            "should_keep": True
        },
        {
            "expression": "[name] == BoneWand # [skillBoneSpirit] >= 3 && [skillIronGolem] >= 3 && [skillBoneSpear] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == BoneWand # [skillBoneSpirit] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == BoneWand # [skillIronGolem] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == BoneWand # [skillBoneSpear] >= 3",
            "should_keep": True
        },
    ],
    # griffs
    "PD2_zKf6cKX5gZ": [
        {
            "expression": "[Name] == Diadem && [quality] == unique && [flag] != ethereal",
            "should_keep": True
        },
    ],
    # rare battle boots
    "PD2_ZtRedtGBPB": [
        {
            "expression": "[name] == BattleBoots && [quality] == rare && [flag] != ethereal # [fireresist] >= 40 && [lightresist] >= 40 && [enhanceddefense] >= 200 && [fhr] >= 10 && [frw] >= 30 && [itemgoldbonus] >= 80",
            "should_keep": True
        },
    ],
    # sorc torch
    "hovered_item_20220504_160228": [
        {
            "expression": "[name] == largecharm && [quality] == unique # [itemaddsorceressskills] == 3 && [allstats] >= 10 && [allres] >= 10",
            "should_keep": True
        },
    ],
    # carrion wind
    "hovered_item_20220504_160419": [
        {
            "expression": "[type] == ring && [quality] == unique # [lifeleech] >= 8 // carrion wind",
            "should_keep": True,
            "should_id": True,
        },
    ],
    # burning essence of terror
    "hovered_item_20220504_161113": [
        {
            "expression": "[Name] == Burningessenceofterror",
            "should_keep": True,
            "should_id": False,
        },
        {
            "expression": "[Type] == quest",
            "should_keep": True
        },
    ],
    # thul rune
    "hovered_item_20220504_161131": [
        {
            "expression": "[Name] == Thulrune",
            "should_keep": True
        },
        {
            "expression": "[Type] == rune",
            "should_keep": True
        },
        {
            "expression": "[name] >= eldrune",
            "should_keep": True
        },
    ],
    # tal helm
    "hovered_item_20220504_161338": [
        {
            "expression": "[Name] == Deathmask && [Quality] == Set",
            "should_keep": True
        },
        {
            "expression": "[Name] == Deathmask # [defense] >= 100",
            "should_keep": True
        },
    ],
    # unidentified rare ring
    "positional_ring": [
        {
            "expression": "[Name] == ring && [Quality] == rare",
            "should_keep": True,
            "should_id": False,
        },
    ],
    # magic jewel
    "hovered_item_20220504_161003": [
        {
            "expression": "[Name] == jewel && [Quality] == magic # [ias] >= 15 && [enhanceddamage] >= 15",
            "should_keep": True
        },
    ],
    # magic large charm
    "PD2_0tY8VkpM8T": [
        {
            "expression": "[name] == LargeCharm && [quality] == magic && [flag] != ethereal # [plusmaxdamage] >= 2 && [fhr] >= 8",
            "should_keep": True
        },
    ],
    # rare jewel
    "PD2_1Iu96WxakK": [
        {
            "expression": "[name] == Jewel && [quality] == rare && [flag] != ethereal # [plusmindamage] >= 7 && [maxmana] >= 13 && [poisonresist] >= 23 && [lightmindam] >= 1 && [lightmaxdam] >= 81",
            "should_keep": True
        },
    ],
    # rare jewel
    "PD2_3sLDs3uUMd": [
        {
            "expression": "[name] == Jewel && [quality] == magic && [flag] != ethereal # [itemundeadtohit] >= 30 && [itemundeaddamagepercent] >= 38 && [strength] >= 3",
            "should_keep": True
        },
    ],
    # magic grand charm
    "PD2_Z7AVNV8X27": [
        {
            "expression": "[name] == GrandCharm && [quality] == magic && [flag] != ethereal # [itemaddskilltab] == 1 && [lightmindam] >= 1 && [lightmaxdam] >= 3",
            "should_keep": True
        },
        {
            "expression": "[name] == GrandCharm && [quality] == magic && [flag] != ethereal # [passiveandmagicskilltab] >= 1",
            "should_keep": True
        },
        {
            "expression": "[name] == GrandCharm && [quality] == magic && [flag] != ethereal # [itemaddskilltab] >= 1",
            "should_keep": True
        },
        {
            "expression": "[name] == GrandCharm && [quality] == magic && [flag] != ethereal # [passiveandmagicskilltab] >= 1",
            "should_keep": True
        },
        {
            "expression": "[name] == GrandCharm && [quality] == magic && [flag] != ethereal # [passiveandmagicskilltab] >= 5",
            "should_keep": False
        },
    ],
    # magic large charm
    "PD2_Y0YlR268P3": [
        {
            "expression": "[name] == LargeCharm && [quality] == magic && [flag] != ethereal # [itemmagicbonus] >= 6 && [frw] >= 5",
            "should_keep": True
        },
    ],
    # magic jewel
    "PD2_aOyb5TqkIm": [
        {
            "expression": "[name] == Jewel && [quality] == magic && [flag] != ethereal # [lightresist] >= 23 && [poisonmindam] >= 20",
            "should_keep": True
        },
        {
            "expression": "[name] == Jewel && [quality] == magic && [flag] != ethereal # [lightresist] >= 23",
            "should_keep": True
        },
    ],
    # magic grand charm
    "PD2_aXKcy7ITEB": [
        # TODO: I had to change from [defense] >= 47 to [plusdefense] >= 47. [defense] is probably a calculated property depending on base item type
        {
            "expression": "[name] == GrandCharm && [quality] == magic && [flag] != ethereal # [plusdefense] >= 47",
            "should_keep": True
        },
    ],
    # magic small charm
    "PD2_KKoeMHxUsp": [
        {
            "expression": "[name] == SmallCharm && [quality] == magic && [flag] != ethereal # [plusmaxdamage] >= 1 && [frw] >= 3",
            "should_keep": True
        },
    ],
    # rare jewel
    "PD2_lYkkSS0qCi": [
        {
            "expression": "[name] == Jewel && [quality] == rare && [flag] != ethereal # [itemlightradius] >= 1 && [tohit] >= 10 && [strength] >= 8 && [coldmindam] >= 1 && [coldmaxdam] >= 4 && [firemindam] >= 7 && [firemaxdam] >= 21",
            "should_keep": True
        },
    ],
    # rare jewel
    "PD2_vBBOGsinxA": [
        {
            "expression": "[name] == Jewel && [quality] == rare && [flag] != ethereal # [itemundeadtohit] >= 38 && [itemundeaddamagepercent] >= 38 && [strength] >= 3 && [itemmagicbonus] >= 8 && [itemreqpercent] <= -15",
            "should_keep": True
        },
    ],
    # rainbow facet, poison
    "PD2_nLSBZYixOe": [
        {
            "expression": "[Name] == jewel && [quality] == unique # [passivecoldpierce]+[passivecoldmastery] >= 10 || [passivepoispierce]+[passivepoismastery] >= 10 || [passiveltngpierce]+[passiveltngmastery] >= 10 || [passivefirepierce]+[passivefiremastery] >= 10",
            "should_keep": True
        },
        {
            "expression": "[Name] == jewel && [quality] == unique # [passivepoispierce]+[passivepoismastery] >= 10",
            "should_keep": True
        },
    ],
    # rainbow facet, fire
    "PD2_5ctnVauZr1": [
        {
            "expression": "[Name] == jewel && [quality] == unique # [passivefirepierce]+[passivefiremastery] >= 10",
            "should_keep": True
        },
        {
            "expression": "[idname] == rainbowfacet",
            "should_keep": True
        },
        {
            "expression": "[idname] == harlequincrest",
            "should_keep": False
        },
    ],
    # nightwing veil
    "nightwing": [
        {
            "expression": "[name] == spiredhelm && [quality] == unique && [flag] != ethereal # [dexterity] >= 10 && [passivecoldmastery] >= 8",
            "should_keep": True
        },
        {
            "expression": "[name] == spiredhelm && [quality] == unique && [flag] != ethereal # [dexterity] >= 10 && [itemabsorbcold] >= 8",
            "should_keep": True
        },
        {
            "expression": "[name] == spiredhelm && [quality] == unique && [flag] != ethereal # [dexterity] >= 10 && [itemabsorbcold] >= 9",
            "should_keep": False
        },
    ],
}