from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChallengeFightJoinRefusedMessage(INetworkMessage):
    protocolId = 2066
    playerId:int
    reason:int
    
    
