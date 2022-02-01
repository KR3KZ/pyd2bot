from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismFightStateUpdateMessage(INetworkMessage):
    protocolId = 7379
    state:int
    
    
