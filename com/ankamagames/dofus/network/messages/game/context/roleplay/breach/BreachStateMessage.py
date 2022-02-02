from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


@dataclass
class BreachStateMessage(NetworkMessage):
    owner:CharacterMinimalInformations
    bonuses:list[ObjectEffectInteger]
    bugdet:int
    saved:bool
    
    
    def __post_init__(self):
        super().__init__()
    