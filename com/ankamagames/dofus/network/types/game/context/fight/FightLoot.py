from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FightLoot(INetworkMessage):
    protocolId = 7224
    objects:int
    kamas:int
    
    
