from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ShortcutBarSwapRequestMessage(INetworkMessage):
    protocolId = 709
    barType:int
    firstSlot:int
    secondSlot:int
    
    
