from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameContextRemoveElementMessage(INetworkMessage):
    protocolId = 5284
    id:int
    
    
