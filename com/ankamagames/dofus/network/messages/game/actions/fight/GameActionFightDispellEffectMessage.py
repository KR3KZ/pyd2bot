from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellMessage import GameActionFightDispellMessage


class GameActionFightDispellEffectMessage(GameActionFightDispellMessage):
    protocolId = 1560
    boostUID:int
    
    
