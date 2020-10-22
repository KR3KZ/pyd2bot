from sikuli.Sikuli import *
import java.awt.Color as Color



# Regions
MAP_R = Region(2,29,1918,1002)
MAP_INFO_R = Region(4,856,306,172)
COMBAT_R = Region(332,28,1257,1004)
PM_R = Region(793,993,27,34)
PA_R = Region(740,997,34,24)
END_COMBAT_R = Region(841,701,244,66)

READY_R = Region(1312,925,145,66)
YOUR_TURN_R = Region(1312,925,145,66)
END_COMBAT_CLOSE_R = Region(1231,721,22,18)



# Patterns

READY_P = Pattern("1603357824947.png")
END_COMBAT_P = "END_COMBAT_P.png"
YOUR_TURN_P = "YOUR_TURN_P.png"


ME_P = [Pattern(Pattern("1603355813879.png").targetOffset(1,-15))]
MOB_P = [Pattern(Pattern("1603354858366.png").targetOffset(-4,-11)), 
        Pattern(Pattern("1603354790380.png").targetOffset(-3,-15)), 
        Pattern(Pattern("1603354897698.png").targetOffset(0,-10)), 
        Pattern(Pattern("1603354963013.png").targetOffset(-3,-11))]

# Vars
CELL_W = 100
CELL_H = 50
CHANGE_MAP_DELAY = 2
EMPTY_SQUARE_COLOR = Color(120,159,61)

# timers
CHANGE_MAP_TIMEOUT = 60

# shortcuts
cnst.RAPPEL_POTION_SHORTCUT = "e"
cnst.FARM_SPELL = {
        "shortcut": "z",
        "range": 7,
        "nbr": 2
        }


