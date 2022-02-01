from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PlayerStatus(INetworkMessage):
    protocolId = 3077
    statusId:int
    
    
