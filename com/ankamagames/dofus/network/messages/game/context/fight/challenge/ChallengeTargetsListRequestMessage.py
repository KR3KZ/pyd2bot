from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChallengeTargetsListRequestMessage(NetworkMessage):
    protocolId = 8411
    challengeId:int
    
    
