from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMassiveMessage(EmotePlayAbstractMessage):
    protocolId = 7780
    actorIds:int
    
