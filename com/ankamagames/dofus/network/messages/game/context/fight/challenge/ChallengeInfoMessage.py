from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChallengeInfoMessage(INetworkMessage):
    protocolId = 638
    challengeId:int
    targetId:int
    xpBonus:int
    dropBonus:int
    
    
