from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DebtInformation(INetworkMessage):
    protocolId = 9735
    id:int
    timestamp:int
    
    
