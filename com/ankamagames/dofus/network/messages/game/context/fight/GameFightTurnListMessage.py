from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightTurnListMessage(NetworkMessage):
    ids:list[int]
    deadsIds:list[int]
    
    
