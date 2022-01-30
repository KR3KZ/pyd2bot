from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger


class BreachBonusMessage(NetworkMessage):
    protocolId = 1689
    bonus:ObjectEffectInteger
    
    
