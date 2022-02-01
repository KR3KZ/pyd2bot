from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonKeyRingMessage(NetworkMessage):
    availables:list[int]
    unavailables:list[int]
    
    
