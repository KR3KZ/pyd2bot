from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightNewRoundMessage(INetworkMessage):
    protocolId = 1656
    roundNumber:int
    
    
