from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShortcutBarSwapRequestMessage(NetworkMessage):
    barType:int
    firstSlot:int
    secondSlot:int
    
    
