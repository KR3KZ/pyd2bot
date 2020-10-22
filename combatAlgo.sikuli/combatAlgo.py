from sikuli.Sikuli import *
import java.awt.Color as Color
from constants import *
from functions import *


def combatAlgo():
    nbrEchec = 0
    while (True):
        myTurn = False
        isDead = False
        spellNbr = 2
        pmNbr = 4
        spellRange = 13
        cnst.YOUR_TURN_R.wait(cnst.YOUR_TURN_P, FOREVER)
        # when the bot turn starts, get his location and mobs location.
        meLoc = getMeLoc()
        mobsLocs = getMobsLocs()
        print(len(mobsLocs), ' mobs where detected')
        myTurn = True
        # check if any mobs where found.
        if mobsLocs == None or meLoc == None:
            print('me or mobs detection failed!')
            nbrEchec += 1
            print('resigning in ', (4 - nbrEchec), ' turns...')
            # if no mobs where found in 4 tries abandone combat.
            if nbrEchec > 3:
                resign()
                'bot resigned !'
                isDead = True
                break
        # if some mobs where detected.
        else:
            # select the nearest target.
            tgtIndex = selectTarget(mobsLocs, meLoc)
            tgtLoc = mobsLocs.pop(tgtIndex)
            tgtColor = tgtLoc.getColor()
            sD = squareDistance(meLoc, tgtLoc)
            # while we still have spells to cast.
            while spellNbr > 0:
                # if the target is in range.
                if sD < spellRange:
                    # try to hit the target with a spell.
                    pa = Pattern(capture(cnst.PA_R))
                    useSpell("e", tgtLoc)
                    wait(0.5)
                    tgtNewColor = tgtLoc.getColor()
                    if tgtNewColor != tgtColor:
                        # if the spell hits the target.
                        spellNbr -= 1
                        if spellNbr == 0: break
                        # if the bot has no more spells break loop
                        wait(.8)
                        tgtNewColor = tgtLoc.getColor()
                        if tgtNewColor != tgtColor:
                            # if it dies and the combat didn't end select another target.
                            tgtIndex = selectTarget(mobsLocs, meLoc)
                            if tgtIndex is None: break
                            tgtLoc = mobsLocs.pop(tgtIndex)
                            tgtColor = tgtLoc.getColor()
                            sD = squareDistance(meLoc, tgtLoc)
                    else:
                        # if the spell didn't hit try to move towards target.
                        print('bot has ', pmNbr, ' pms')
                        if pmNbr == 0: break
                        meOldLoc = meLoc
                        meLoc = moveTowardsTarget(meLoc, tgtLoc, min(pmNbr, sD - 1))
                        if meLoc is None:
                            nbrEchec += 1
                            break
                        pmNbr = pmNbr - squareDistance(meLoc, meOldLoc)
                        sD = squareDistance(meLoc, tgtLoc)
                else:
                    # if the spell is not in range move towards target.
                    print('bot has ', pmNbr, ' pms')
                    if pmNbr == 0: break
                    meOldLoc = meLoc
                    meLoc = moveTowardsTarget(meLoc, tgtLoc, min((sD - spellRange), pmNbr))
                    if meLoc is None:
                        nbrEchec += 1
                        break
                    pmNbr = pmNbr - squareDistance(meLoc, meOldLoc)
                    sD = squareDistance(meLoc, tgtLoc)
                    # if we can't cast any spell pass.
        if END_R.exists(END_COMBAT_P):
            END_R.click(END_COMBAT_P)
            break
        else:
            type("f")
    return isDead, myTurn
