from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismUseRequestMessage(INetworkMessage):
    protocolId = 8164
    moduleToUse:int
    
    
