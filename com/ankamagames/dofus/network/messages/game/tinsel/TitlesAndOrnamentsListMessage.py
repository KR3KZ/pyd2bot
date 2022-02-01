from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TitlesAndOrnamentsListMessage(NetworkMessage):
    titles:list[int]
    ornaments:list[int]
    activeTitle:int
    activeOrnament:int
    
    
