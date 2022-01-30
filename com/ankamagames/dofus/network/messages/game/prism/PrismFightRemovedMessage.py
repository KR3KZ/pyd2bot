from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismFightRemovedMessage(INetworkMessage):
    protocolId = 9563
    subAreaId:int
    
    
