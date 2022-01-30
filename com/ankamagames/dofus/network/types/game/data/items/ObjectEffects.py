from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ObjectEffects(INetworkMessage):
    protocolId = 5613
    effects:ObjectEffect
    
    
