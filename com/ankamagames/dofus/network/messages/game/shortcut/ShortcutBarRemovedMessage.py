from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ShortcutBarRemovedMessage(INetworkMessage):
    protocolId = 5087
    barType:int
    slot:int
    
    
