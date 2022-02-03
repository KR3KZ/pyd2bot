from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextSummonsInformation import GameContextSummonsInformation
    


class GameActionFightMultipleSummonMessage(AbstractGameActionMessage):
    summons:list['GameContextSummonsInformation']
    

    def init(self, summons:list['GameContextSummonsInformation'], actionId:int, sourceId:int):
        self.summons = summons
        
        super().__init__(actionId, sourceId)
    
    