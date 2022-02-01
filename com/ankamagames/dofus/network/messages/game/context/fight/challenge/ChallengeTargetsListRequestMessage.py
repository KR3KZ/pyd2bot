from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChallengeTargetsListRequestMessage(INetworkMessage):
    protocolId = 8411
    challengeId:int
    
    
