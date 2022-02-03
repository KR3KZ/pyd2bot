from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


class TreasureHuntStepFollowDirection(TreasureHuntStep):
    direction:int
    mapCount:int
    

    def init(self, direction:int, mapCount:int):
        self.direction = direction
        self.mapCount = mapCount
        
        super().__init__()
    
    