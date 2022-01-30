from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage


class GameActionFightActivateGlyphTrapMessage(AbstractGameActionMessage):
    protocolId = 9234
    markId:int
    active:bool
    
    
