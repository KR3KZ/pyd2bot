from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FightStartingPositions(NetworkMessage):
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    
    
