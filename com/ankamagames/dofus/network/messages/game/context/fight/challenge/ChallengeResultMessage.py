from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeResultMessage(NetworkMessage):
    challengeId:int
    success:bool
    
    
