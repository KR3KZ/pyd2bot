from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount


@dataclass
class GameActionUpdateEffectTriggerCountMessage(NetworkMessage):
    targetIds:list[GameFightEffectTriggerCount]
    
    
    def __post_init__(self):
        super().__init__()
    