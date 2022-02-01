from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeInfoMessage(NetworkMessage):
    challengeId:int
    targetId:int
    xpBonus:int
    dropBonus:int
    
    
