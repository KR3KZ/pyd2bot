from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMessage(EmotePlayAbstractMessage):
    actorId:int
    accountId:int
    

    def init(self, actorId:int, accountId:int, emoteId:int, emoteStartTime:int):
        self.actorId = actorId
        self.accountId = accountId
        
        super().__init__(emoteId, emoteStartTime)
    
    