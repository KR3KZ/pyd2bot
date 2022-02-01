from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightTurnEndMessage(INetworkMessage):
    protocolId = 4443
    id:int
    
    
