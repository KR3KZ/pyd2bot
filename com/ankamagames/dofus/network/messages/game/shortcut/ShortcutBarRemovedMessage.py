from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarRemovedMessage(NetworkMessage):
    protocolId = 5087
    barType:int
    slot:int
    
    
