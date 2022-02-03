from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionEmote(HumanOption):
    emoteId:int
    emoteStartTime:int
    

    def init(self, emoteId:int, emoteStartTime:int):
        self.emoteId = emoteId
        self.emoteStartTime = emoteStartTime
        
        super().__init__()
    
    