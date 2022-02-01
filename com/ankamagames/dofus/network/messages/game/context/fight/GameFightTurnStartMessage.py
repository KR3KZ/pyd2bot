from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightTurnStartMessage(INetworkMessage):
    protocolId = 3772
    id:int
    waitTime:int
    
    
