from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ShortcutBarSwapRequestMessage(INetworkMessage):
    protocolId = 709
    barType:int
    firstSlot:int
    secondSlot:int
    
    
