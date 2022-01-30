from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.inventory.exchanges.RecycledItem import RecycledItem


class EvolutiveObjectRecycleResultMessage(NetworkMessage):
    protocolId = 8805
    recycledItems:RecycledItem
    
