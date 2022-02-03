from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
    


class GameActionUpdateEffectTriggerCountMessage(NetworkMessage):
    targetIds:list['GameFightEffectTriggerCount']
    

    def init(self, targetIds:list['GameFightEffectTriggerCount']):
        self.targetIds = targetIds
        
        super().__init__()
    
    