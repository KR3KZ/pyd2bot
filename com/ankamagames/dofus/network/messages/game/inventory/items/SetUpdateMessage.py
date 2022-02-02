from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


@dataclass
class SetUpdateMessage(NetworkMessage):
    setId:int
    setObjects:list[int]
    setEffects:list[ObjectEffect]
    
    
    def __post_init__(self):
        super().__init__()
    