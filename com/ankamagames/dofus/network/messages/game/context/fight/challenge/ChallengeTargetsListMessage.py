from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeTargetsListMessage(NetworkMessage):
    targetIds:list[int]
    targetCells:list[int]
    
    
