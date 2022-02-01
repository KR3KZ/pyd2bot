from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameContextCreateMessage(INetworkMessage):
    protocolId = 4950
    context:int
    
    
