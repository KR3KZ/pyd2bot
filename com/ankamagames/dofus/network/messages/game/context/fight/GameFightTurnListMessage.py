from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightTurnListMessage(INetworkMessage):
    protocolId = 7238
    ids:int
    deadsIds:int
    
    
