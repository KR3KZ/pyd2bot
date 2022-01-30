from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChallengeTargetsListMessage(INetworkMessage):
    protocolId = 7386
    targetIds:int
    targetCells:int
    
    
