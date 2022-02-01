from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameActionSpamMessage(INetworkMessage):
    protocolId = 6276
    cells:int
    
    
