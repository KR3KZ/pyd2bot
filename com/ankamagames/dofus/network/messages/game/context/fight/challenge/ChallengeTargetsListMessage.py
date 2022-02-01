from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChallengeTargetsListMessage(INetworkMessage):
    protocolId = 7386
    targetIds:int
    targetCells:int
    
    
