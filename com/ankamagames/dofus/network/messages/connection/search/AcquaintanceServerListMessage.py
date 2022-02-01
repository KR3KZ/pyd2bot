from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AcquaintanceServerListMessage(INetworkMessage):
    protocolId = 8752
    servers:int
    
    
