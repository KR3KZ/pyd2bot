from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismFightRemovedMessage(NetworkMessage):
    protocolId = 9563
    subAreaId:int
    
    
