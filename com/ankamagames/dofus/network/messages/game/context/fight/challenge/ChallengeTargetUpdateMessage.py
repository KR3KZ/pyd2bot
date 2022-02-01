from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeTargetUpdateMessage(NetworkMessage):
    challengeId:int
    targetId:int
    
    
