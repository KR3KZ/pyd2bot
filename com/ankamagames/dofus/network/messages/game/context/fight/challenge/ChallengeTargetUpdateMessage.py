from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChallengeTargetUpdateMessage(INetworkMessage):
    protocolId = 1613
    challengeId:int
    targetId:int
    
    
