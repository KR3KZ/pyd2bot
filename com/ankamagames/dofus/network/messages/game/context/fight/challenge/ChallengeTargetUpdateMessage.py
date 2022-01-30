from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChallengeTargetUpdateMessage(INetworkMessage):
    protocolId = 1613
    challengeId:int
    targetId:int
    
    
