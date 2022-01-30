from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


class TreasureHuntStepFollowDirectionToHint(TreasureHuntStep):
    protocolId = 4752
    direction:int
    npcId:int
    
