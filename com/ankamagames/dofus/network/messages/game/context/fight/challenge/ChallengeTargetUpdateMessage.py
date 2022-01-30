from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChallengeTargetUpdateMessage(NetworkMessage):
    protocolId = 1613
    challengeId:int
    targetId:int
    
