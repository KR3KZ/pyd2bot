from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChallengeFightJoinRefusedMessage(NetworkMessage):
    playerId:int
    reason:int
    
    
