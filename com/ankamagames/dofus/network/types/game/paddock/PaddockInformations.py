from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockInformations(INetworkMessage):
    protocolId = 1965
    maxOutdoorMount:int
    maxItems:int
    
    
