from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightTurnReadyRequestMessage(INetworkMessage):
    protocolId = 4389
    id:int
    
    
