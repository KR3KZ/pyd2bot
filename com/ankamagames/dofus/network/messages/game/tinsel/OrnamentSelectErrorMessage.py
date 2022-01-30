from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class OrnamentSelectErrorMessage(INetworkMessage):
    protocolId = 4098
    reason:int
    
    
