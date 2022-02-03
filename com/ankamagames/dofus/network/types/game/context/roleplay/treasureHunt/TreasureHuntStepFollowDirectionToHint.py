from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


class TreasureHuntStepFollowDirectionToHint(TreasureHuntStep):
    direction:int
    npcId:int
    

    def init(self, direction:int, npcId:int):
        self.direction = direction
        self.npcId = npcId
        
        super().__init__()
    
    