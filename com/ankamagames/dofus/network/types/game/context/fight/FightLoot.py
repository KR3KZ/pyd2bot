from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FightLoot(NetworkMessage):
    protocolId = 7224
    objects:list[int]
    kamas:float
    
