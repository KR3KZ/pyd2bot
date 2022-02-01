from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount


class GameActionUpdateEffectTriggerCountMessage(NetworkMessage):
    targetIds:list[GameFightEffectTriggerCount]
    
    
