from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


class TreasureHuntStepFollowDirectionToPOI(TreasureHuntStep):
    protocolId = 2093
    direction:int
    poiLabelId:int
    
    
