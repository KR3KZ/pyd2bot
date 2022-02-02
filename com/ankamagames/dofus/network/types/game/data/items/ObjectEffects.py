from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


@dataclass
class ObjectEffects(NetworkMessage):
    effects:list[ObjectEffect]
    
    
    def __post_init__(self):
        super().__init__()
    