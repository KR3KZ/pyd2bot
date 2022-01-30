from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class BreachBonusMessage(INetworkMessage):
    protocolId = 1689
    bonus:ObjectEffectInteger
    
    
