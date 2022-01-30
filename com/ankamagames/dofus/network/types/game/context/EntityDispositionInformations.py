from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EntityDispositionInformations(INetworkMessage):
    protocolId = 7424
    cellId:int
    direction:int
    
    
