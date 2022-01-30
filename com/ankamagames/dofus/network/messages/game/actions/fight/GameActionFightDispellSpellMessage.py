from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellMessage import GameActionFightDispellMessage


class GameActionFightDispellSpellMessage(GameActionFightDispellMessage):
    protocolId = 6878
    spellId:int
    
    
