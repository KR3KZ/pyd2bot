from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DebtInformation(INetworkMessage):
    protocolId = 9735
    id:int
    timestamp:int
    
    
