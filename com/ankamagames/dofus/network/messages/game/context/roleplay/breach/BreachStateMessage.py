from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class BreachStateMessage(NetworkMessage):
    owner:CharacterMinimalInformations
    bonuses:list[ObjectEffectInteger]
    bugdet:int
    saved:bool
    
    
