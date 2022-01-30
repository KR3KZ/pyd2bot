from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CheckIntegrityMessage(INetworkMessage):
    protocolId = 1296
    data:int
    
    
