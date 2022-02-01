from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class BreachStateMessage(INetworkMessage):
    protocolId = 5776
    owner:CharacterMinimalInformations
    bonuses:ObjectEffectInteger
    bugdet:int
    saved:bool
    
    
