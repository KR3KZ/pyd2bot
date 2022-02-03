from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


class TreasureHuntStepFollowDirectionToPOI(TreasureHuntStep):
    direction:int
    poiLabelId:int
    

    def init(self, direction:int, poiLabelId:int):
        self.direction = direction
        self.poiLabelId = poiLabelId
        
        super().__init__()
    
    