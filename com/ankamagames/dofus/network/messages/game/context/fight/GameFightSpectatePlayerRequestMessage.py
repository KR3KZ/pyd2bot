from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightSpectatePlayerRequestMessage(INetworkMessage):
    protocolId = 9098
    playerId:int
    
    
