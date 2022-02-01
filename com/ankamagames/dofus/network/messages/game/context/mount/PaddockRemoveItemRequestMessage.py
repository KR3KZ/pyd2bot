from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockRemoveItemRequestMessage(INetworkMessage):
    protocolId = 9863
    cellId:int
    
    
