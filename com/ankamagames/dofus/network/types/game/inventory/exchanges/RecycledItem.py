from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class RecycledItem(NetworkMessage):
    protocolId = 161
    id:int
    qty:int
    
    
