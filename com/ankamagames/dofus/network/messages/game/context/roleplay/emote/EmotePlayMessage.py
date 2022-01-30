from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMessage(EmotePlayAbstractMessage):
    protocolId = 9462
    actorId:float
    accountId:int
    
