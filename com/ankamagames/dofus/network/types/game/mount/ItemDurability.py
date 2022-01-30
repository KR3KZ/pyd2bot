from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ItemDurability(NetworkMessage):
    protocolId = 2055
    durability:int
    durabilityMax:int
    
    
