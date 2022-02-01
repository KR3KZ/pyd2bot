from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChallengeResultMessage(INetworkMessage):
    protocolId = 7757
    challengeId:int
    success:bool
    
    
