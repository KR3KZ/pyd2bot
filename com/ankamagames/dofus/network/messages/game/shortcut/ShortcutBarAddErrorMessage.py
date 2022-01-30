from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarAddErrorMessage(NetworkMessage):
    protocolId = 1782
    error:int
    
