from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarSwapRequestMessage(NetworkMessage):
    protocolId = 709
    barType:int
    firstSlot:int
    secondSlot:int
    
