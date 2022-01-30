from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightVanishMessage(AbstractGameActionMessage):
    protocolId = 5414
    targetId:int
    
