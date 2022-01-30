from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChallengeResultMessage(NetworkMessage):
    protocolId = 7757
    challengeId:int
    success:bool
    
