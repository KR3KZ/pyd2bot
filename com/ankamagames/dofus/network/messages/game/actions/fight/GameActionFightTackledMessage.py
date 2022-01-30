from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightTackledMessage(AbstractGameActionMessage):
    protocolId = 4448
    tacklersIds:list[float]
    
