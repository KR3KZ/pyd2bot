from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FightLoot(INetworkMessage):
    protocolId = 7224
    objects:int
    kamas:int
    
    
