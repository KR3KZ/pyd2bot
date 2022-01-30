from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BufferInformation(INetworkMessage):
    protocolId = 3684
    id:int
    amount:int
    
    
