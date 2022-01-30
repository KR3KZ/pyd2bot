from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarRemoveErrorMessage(NetworkMessage):
    protocolId = 5661
    error:int
    
