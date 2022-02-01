from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FightLoot(NetworkMessage):
    objects:list[int]
    kamas:int
    
    
