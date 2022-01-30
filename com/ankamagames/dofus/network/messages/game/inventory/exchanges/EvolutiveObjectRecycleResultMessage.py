from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.inventory.exchanges.RecycledItem import RecycledItem


class EvolutiveObjectRecycleResultMessage(INetworkMessage):
    protocolId = 8805
    recycledItems:RecycledItem
    
    
