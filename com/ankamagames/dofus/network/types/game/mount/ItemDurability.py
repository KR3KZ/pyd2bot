from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ItemDurability(INetworkMessage):
    protocolId = 2055
    durability:int
    durabilityMax:int
    
    
