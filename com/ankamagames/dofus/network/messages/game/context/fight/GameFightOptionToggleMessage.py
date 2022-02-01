from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightOptionToggleMessage(INetworkMessage):
    protocolId = 2382
    option:int
    
    
