from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarRemoveRequestMessage(NetworkMessage):
    protocolId = 906
    barType:int
    slot:int
    
    
