from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChallengeResultMessage(INetworkMessage):
    protocolId = 7757
    challengeId:int
    success:bool
    
    
