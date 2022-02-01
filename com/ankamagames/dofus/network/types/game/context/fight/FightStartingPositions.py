from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FightStartingPositions(INetworkMessage):
    protocolId = 9707
    positionsForChallengers:int
    positionsForDefenders:int
    
    
