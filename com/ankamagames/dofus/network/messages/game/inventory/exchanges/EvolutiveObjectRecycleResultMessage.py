from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.inventory.exchanges.RecycledItem import RecycledItem


class EvolutiveObjectRecycleResultMessage(NetworkMessage):
    recycledItems:list[RecycledItem]
    
    
