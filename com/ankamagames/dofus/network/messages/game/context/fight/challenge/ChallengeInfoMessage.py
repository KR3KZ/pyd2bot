from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChallengeInfoMessage(NetworkMessage):
    protocolId = 638
    challengeId:int
    targetId:int
    xpBonus:int
    dropBonus:int
    
