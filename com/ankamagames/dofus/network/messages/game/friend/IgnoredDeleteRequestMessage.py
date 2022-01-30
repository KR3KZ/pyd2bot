from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class IgnoredDeleteRequestMessage(INetworkMessage):
    protocolId = 2264
    accountId:int
    session:bool
    
    
