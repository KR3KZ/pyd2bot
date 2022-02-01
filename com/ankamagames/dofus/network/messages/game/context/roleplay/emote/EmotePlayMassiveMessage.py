from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import EmotePlayAbstractMessage


class EmotePlayMassiveMessage(EmotePlayAbstractMessage):
    actorIds:list[int]
    
    
