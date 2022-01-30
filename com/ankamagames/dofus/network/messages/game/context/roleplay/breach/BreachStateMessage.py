from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class BreachStateMessage(NetworkMessage):
    protocolId = 5776
    owner:CharacterMinimalInformations
    bonuses:list[ObjectEffectInteger]
    bugdet:int
    saved:bool
    
