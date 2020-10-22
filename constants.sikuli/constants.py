from sikuli.Sikuli import *
import java.awt.Color as Color

# Regions
LVLUP_R = Region(326, 293, 626, 219)

MAPC1_R = Region(213, 607, 163, 119)
MAPC2_R = Region(209, 82, 152, 83)
MAP_R = Region(211, 82, 945, 645)
MAP_R2 = Region(217, 100, 915, 611)

PM_R = Region(1193, 117, 19, 19)
PA_R = Region(1180, 95, 13, 16)
END_R = Region(779, 143, 362, 287)
SPELL_R = Region(1158, 258, 49, 49)
READY_R = Region(270, 139, 98, 28)
YOUR_TURN_R = Region(550, 380, 91, 53)
RESIGNE_R = Region(1318, 99, 44, 38)
RESIGNE_CONFIRM_R = Region(498, 451, 180, 33)

FIRST_ITEM_R = Region(1152, 154, 59, 53)
USE_ITEM_R = Region(938, 118, 215, 33)
BRED_R = Region(1152, 259, 57, 45)
USE_MULT_R = Region(951, 184, 146, 21)
USE_MULTI_MAX_R = Region(957, 211, 63, 29)
USE_MULT_CONFIRM_R = Region(1130, 212, 32, 28)

# Patterns
MOB_P = Pattern(Pattern("1486119760235.png").similar(0.74).targetOffset(-3, -5))
ME_P = Pattern(Pattern("me-2.png").similar(0.59).targetOffset(1, -7))

ME_Ps = [ME_P]
READY_P = Pattern(Pattern("1485507775293.png").similar(0.79))
CHECK_BOX_P = Pattern("checkBox-1.png")
END_COMBAT_P = Pattern("1485459909387.png")
LVLUP_OK_P = Pattern("okBox.png")
YOUR_TURN_P = Pattern(Pattern("yourTurn.png").similar(0.90))
SMALL_RIVER_FISH_P = Pattern(Pattern("smallRiverFish.png").similar(0.40))

P1 = Pattern(Pattern("1486137755108.png").similar(0.80))
P2 = Pattern(Pattern("1486134404448.png").similar(0.85))
P3 = Pattern(Pattern("1486134386975.png").similar(0.80))
P4 = Pattern(Pattern("1486132823732.png").similar(0.80))
MOB_Ps = [P1, P2, P3, P4]

# Vars
u = 30
v = 15
CHANGE_MAP_DELAY = 2
CHANGE_MAP = '*'
SMALL_SPOT = '0'
NORMAL_SPOT = '1'
BIG_SPOT = '2'
GEANT_SPOT = '3'
EMPTY_SQUARE_COLOR = Color(103, 163, 70)