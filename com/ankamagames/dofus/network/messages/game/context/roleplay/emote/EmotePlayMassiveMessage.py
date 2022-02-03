from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMassiveMessage(EmotePlayAbstractMessage):
    actorIds:list[int]
    

    def init(self, actorIds:list[int], emoteId:int, emoteStartTime:int):
        self.actorIds = actorIds
        
        super().__init__(emoteId, emoteStartTime)
    
    