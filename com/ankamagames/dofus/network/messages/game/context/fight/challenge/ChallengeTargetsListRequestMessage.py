from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChallengeTargetsListRequestMessage(INetworkMessage):
    protocolId = 8411
    challengeId:int
    
    
