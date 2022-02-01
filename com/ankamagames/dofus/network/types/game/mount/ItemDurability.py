from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ItemDurability(INetworkMessage):
    protocolId = 2055
    durability:int
    durabilityMax:int
    
    
