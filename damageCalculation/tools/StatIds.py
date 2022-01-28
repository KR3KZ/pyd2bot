
from enum import Enum


class StatIds(Enum):

    UNKNOWN:int = -1
      
    LIFE_POINTS:int = 0
      
    ACTION_POINTS:int = 1
      
    STATS_POINTS:int = 3
      
    SPELL_POINTS:int = 4
      
    LEVEL:int = 5
      
    STRENGTH:int = 10
      
    VITALITY:int = 11
      
    WISDOM:int = 12
      
    CHANCE:int = 13
      
    AGILITY:int = 14
      
    INTELLIGENCE:int = 15
      
    ALL_DAMAGES_BONUS:int = 16
      
    DAMAGES_FACTOR:int = 17
      
    CRITICAL_HIT:int = 18
      
    RANGE:int = 19
      
    DAMAGES_PHYSICAL_REDUCTION:int = 21
      
    EXPERIENCE_BOOST:int = 22
      
    MOVEMENT_POINTS:int = 23
      
    INVISIBILITY:int = 24
      
    DAMAGES_PERCENT:int = 25
      
    MAX_SUMMONED_CREATURES_BOOST:int = 26
      
    DODGE_PA_LOST_PROBABILITY:int = 27
      
    DODGE_PM_LOST_PROBABILITY:int = 28
      
    ENERGY_POINTS:int = 29
      
    ALIGNMENT_VALUE:int = 30
      
    WEAPON_DAMAGES_PERCENT:int = 31
      
    PHYSICAL_DAMAGES_BONUS:int = 32
      
    EARTH_ELEMENT_RESIST_PERCENT:int = 33
      
    FIRE_ELEMENT_RESIST_PERCENT:int = 34
      
    WATER_ELEMENT_RESIST_PERCENT:int = 35
      
    AIR_ELEMENT_RESIST_PERCENT:int = 36
      
    NEUTRAL_ELEMENT_RESIST_PERCENT:int = 37
      
    DIFFERENT_LOOK:int = 38
      
    CRITICAL_MISS:int = 39
      
    WEIGHT:int = 40
      
    RESTRICTION_ON_MYSELF:int = 41
      
    RESTRICTION_ON_OTHER:int = 42
      
    ALIGNMENT_SIDE:int = 43
      
    INITIATIVE:int = 44
      
    SHOP_REDUCTION_PERCENTAGE:int = 45
      
    ALIGNMENT_RANK:int = 46
      
    MAX_ENERGY_POINTS:int = 47
      
    MAGIC_FIND:int = 48
      
    HEAL_BONUS:int = 49
      
    REFLECT_DAMAGE:int = 50
      
    ENERGY_LOOSE:int = 51
      
    HONOUR_POINTS:int = 52
      
    DISHOUNOUR_POINTS:int = 53
      
    EARTH_ELEMENT_REDUCTION:int = 54
      
    FIRE_ELEMENT_REDUCTION:int = 55
      
    WATER_ELEMENT_REDUCTION:int = 56
      
    AIR_ELEMENT_REDUCTION:int = 57
      
    NEUTRAL_ELEMENT_REDUCTION:int = 58
      
    PVP_EARTH_ELEMENT_RESIST_PERCENT:int = 59
      
    PVP_FIRE_ELEMENT_RESIST_PERCENT:int = 60
      
    PVP_WATER_ELEMENT_RESIST_PERCENT:int = 61
      
    PVP_AIR_ELEMENT_RESIST_PERCENT:int = 62
      
    PVP_NEUTRAL_ELEMENT_RESIST_PERCENT:int = 63
      
    PVP_EARTH_ELEMENT_REDUCTION:int = 64
      
    PVP_FIRE_ELEMENT_REDUCTION:int = 65
      
    PVP_WATER_ELEMENT_REDUCTION:int = 66
      
    PVP_AIR_ELEMENT_REDUCTION:int = 67
      
    PVP_NEUTRAL_ELEMENT_REDUCTION:int = 68
      
    TRAP_DAMAGE_BONUS_PERCENT:int = 69
      
    TRAP_DAMAGE_BONUS:int = 70
      
    FAKE_SKILL_FOR_STATES:int = 71
      
    SOUL_CAPTURE_BONUS:int = 72
      
    RIDE_XP_BONUS:int = 73
      
    CONFUSION:int = 74
      
    PERMANENT_DAMAGE_PERCENT:int = 75
      
    UNLUCKY:int = 76
      
    MAXIMIZE_ROLL:int = 77
      
    TACKLE_EVADE:int = 78
      
    TACKLE_BLOCK:int = 79
      
    ALLIANCE_AUTO_AGGRESS_RANGE:int = 80
      
    ALLIANCE_AUTO_AGGRESS_RESISTANCE:int = 81
      
    AP_ATTACK:int = 82
      
    MP_ATTACK:int = 83
      
    PUSH_DAMAGE_BONUS:int = 84
      
    PUSH_DAMAGE_REDUCTION:int = 85
      
    CRITICAL_DAMAGE_BONUS:int = 86
      
    CRITICAL_DAMAGE_REDUCTION:int = 87
      
    EARTH_DAMAGE_BONUS:int = 88
      
    FIRE_DAMAGE_BONUS:int = 89
      
    WATER_DAMAGE_BONUS:int = 90
      
    AIR_DAMAGE_BONUS:int = 91
      
    NEUTRAL_DAMAGE_BONUS:int = 92
      
    MAX_BOMB_SUMMON:int = 93
      
    BOMB_COMBO_BONUS:int = 94
      
    MAX_LIFE:int = 95
      
    SHIELD:int = 96
      
    CUR_LIFE:int = 97
      
    DAMAGES_PERCENT_SPELL:int = 98
      
    EXTRA_SCALE_FLAT:int = 99
      
    PASS_TURN:int = 100
      
    RESIST_PERCENT:int = 101
      
    CUR_PERMANENT_DAMAGE:int = 102
      
    WEAPON_POWER:int = 103
      
    INCOMING_DAMAGE_PERCENT_MULTIPLICATOR:int = 104
      
    INCOMING_DAMAGE_HEAL_PERCENT_MULTIPLICATOR:int = 105
      
    GLYPH_POWER:int = 106
      
    DEALT_DAMAGE_MULTIPLIER:int = 107
      
    STOP_XP:int = 108
      
    HUNTER:int = 109
      
    RUNE_POWER:int = 110
      
    DEALT_DAMAGE_MULTIPLIER_MELEE:int = 125
      
    DEALT_DAMAGE_MULTIPLIER_DISTANCE:int = 120
      
    DEALT_DAMAGE_MULTIPLIER_WEAPON:int = 122
      
    RECEIVED_DAMAGE_MULTIPLIER_MELEE:int = 124
      
    DEALT_DAMAGE_MULTIPLIER_SPELLS:int = 123
      
    RECEIVED_DAMAGE_MULTIPLIER_DISTANCE:int = 121
      
    RECEIVED_DAMAGE_MULTIPLIER_WEAPON:int = 142
      
    RECEIVED_DAMAGE_MULTIPLIER_SPELLS:int = 141
      
    AGILITY_INITIAL_PERCENT:int = 126
      
    STRENGTH_INITIAL_PERCENT:int = 127
      
    CHANCE_INITIAL_PERCENT:int = 128
      
    INTELLIGENCE_INITIAL_PERCENT:int = 129
      
    VITALITY_INITIAL_PERCENT:int = 130
      
    WISDOM_INITIAL_PERCENT:int = 131
      
    TACKLE_EVADE_INITIAL_PERCENT:int = 132
      
    TACKLE_BLOCK_INITIAL_PERCENT:int = 133
      
    ACTION_POINTS_INITIAL_PERCENT:int = 134
      
    MOVEMENT_POINTS_INITIAL_PERCENT:int = 135
      
    AP_ATTACK_INITIAL_PERCENT:int = 136
      
    MP_ATTACK_INITIAL_PERCENT:int = 137
      
    DODGE_PA_LOST_PROBABILITY_INITIAL_PERCENT:int = 138
      
    DODGE_PM_LOST_PROBABILITY_INITIAL_PERCENT:int = 139
      
    EXTRA_SCALE_PERCENT:int = 140
      
    CHARAC_COUNT:int = 141
       
      

      
    def getStatIdFromStatName(param1:str) -> int:
        _loc2_ = param1
        if _loc2_ == "PAAttack":
        
            return 82
        
        if _loc2_ == "PMAttack":
        
            return 83
        
        if _loc2_ == "actionPoints":
        
            return 1
        
        if _loc2_ == "agility":
        
            return 14
        
        if _loc2_ == "airDamageBonus":
        
            return 91
        
        if _loc2_ == "airElementReduction":
        
            return 57
        
        if _loc2_ == "airElementResistPercent":
        
            return 36
        
        if _loc2_ == "allDamagesBonus":
        
            return 16
        
        if _loc2_ == "baseMaxLifePoints":
        
            return 0
        
        if _loc2_ == "bombCombo":
        
            return 94
        
        if _loc2_ == "chance":
        
            return 13
        
        if _loc2_ == "confusion":
        
            return 74
        
        if _loc2_ == "criticalDamageBonus":
        
            return 86
        
        if _loc2_ == "criticalDamageReduction":
        
            return 87
        
        if _loc2_ == "criticalHit":
        
            return 18
        
        if _loc2_ == "criticalMiss":
        
            return 39
        
        if _loc2_ == "curPermanentDamages":
        
            return 102
        
        if _loc2_ == "damagesBonusPercent":
        
            return 25
        
        if _loc2_ == "dealtDamagesMultiplicator":
        
            return 107
        
        if _loc2_ == "dodgePALostProbability":
        
            return 27
        
        if _loc2_ == "dodgePMLostProbability":
        
            return 28
        
        if _loc2_ == "earthDamageBonus":
        
            return 88
        
        if _loc2_ == "earthElementReduction":
        
            return 54
        
        if _loc2_ == "earthElementResistPercent":
        
            return 33
        
        if _loc2_ == "energyPoints":
        
            return 29
        
        if _loc2_ == "fireDamageBonus":
        
            return 89
        
        if _loc2_ == "fireElementReduction":
        
            return 55
        
        if _loc2_ == "fireElementResistPercent":
        
            return 34
        
        if _loc2_ == "glyphPower":
        
            return 106
        
        if _loc2_ == "healBonus":
        
            return 49
        
        if _loc2_ == "incomingPercentDamageMultiplicator":
        
            return 104
        
        if _loc2_ == "incomingPercentHealMultiplicator":
        
            return 105
        
        if _loc2_ == "initiative":
        
            return 44
        
        if _loc2_ == "intelligence":
        
            return 15
        
        if _loc2_ == "invisibilityState":
        
            return 24
        
        if _loc2_ == "lifePoints":
        
            return 97
        
        if _loc2_ == "maxBomb":
        
            return 93
        
        if _loc2_ == "maxEnergyPoints":
        
            return 47
        
        if _loc2_ == "maxLifePoints":
        
            return 95
        
        if _loc2_ == "maximizeRoll":
        
            return 77
        
        if _loc2_ == "meleeDamageDonePercent":
        
            return 125
        
        if _loc2_ == "meleeDamageReceivedPercent":
        
            return 124
        
        if _loc2_ == "movementPoints":
        
            return 23
        
        if _loc2_ == "neutralDamageBonus":
        
            return 92
        
        if _loc2_ == "neutralElementReduction":
        
            return 58
        
        if _loc2_ == "neutralElementResistPercent":
        
            return 37
        
        if _loc2_ == "percentResist":
        
            return 101
        
        if _loc2_ == "permanentDamagePercent":
        
            return 75
        
        if _loc2_ == "physicalDamagesBonus":
        
            return 32
        
        if _loc2_ == "pushDamageBonus":
        
            return 84
        
        if _loc2_ == "pushDamageFixedResist":
        
            return 85
        
        if _loc2_ == "pvpAirElementPercentResist":
        
            return 62
        
        if _loc2_ == "pvpAirElementReduction":
        
            return 67
        
        if _loc2_ == "pvpEarthElementPercentResist":
        
            return 59
        
        if _loc2_ == "pvpEarthElementReduction":
        
            return 64
        
        if _loc2_ == "pvpFireElementReduction":
        
            return 65
        
        if _loc2_ == "pvpFireElementResistPercent":
        
            return 60
        
        if _loc2_ == "pvpNeutralElementPercentResist":
        
            return 63
        
        if _loc2_ == "pvpNeutralElementReduction":
        
            return 68
        
        if _loc2_ == "pvpWaterElementPercentResist":
        
            return 61
        
        if _loc2_ == "pvpWaterElementReduction":
        
            return 66
        
        if _loc2_ == "range":
        
            return 19
        
        if _loc2_ == "rangedDamageDonePercent":
        
            return 120
        
        if _loc2_ == "rangedDamageReceivedPercent":
        
            return 121
        
        if _loc2_ == "reflect":
        
            return 50
        
        if _loc2_ == "runePower":
        
            return 110
        
        if _loc2_ == "shieldPoints":
        
            return 96
        
        if _loc2_ == "spellDamageDonePercent":
        
            return 123
        
        if _loc2_ == "spellDamageReceivedPercent":
        
            return 141
        
        if _loc2_ == "spellPercentDamages":
        
            return 98
        
        if _loc2_ == "strength":
        
            return 10
        
        if _loc2_ == "summonableCreaturesBoost":
        
            return 26
        
        if _loc2_ == "tackleBlock":
        
            return 79
        
        if _loc2_ == "tackleEvade":
        
            return 78
        
        if _loc2_ == "trapBonusPercent":
        
            return 69
        
        if _loc2_ == "unlucky":
        
            return 76
        
        if _loc2_ == "vitality":
        
            return 11
        
        if _loc2_ == "waterDamageBonus":
        
            return 90
        
        if _loc2_ == "waterElementReduction":
        
            return 56
        
        if _loc2_ == "waterElementResistPercent":
        
            return 35
        
        if _loc2_ == "weaponDamageDonePercent":
        
            return 122
        
        if _loc2_ == "weaponDamageReceivedPercent":
        
            return 142
        
        if _loc2_ == "weaponDamagesBonusPercent":
        
            return 31
        
        if _loc2_ == "weaponPower":
        
            return 103
        
        if _loc2_ == "wisdom":
        
            return 12
        
        return -1