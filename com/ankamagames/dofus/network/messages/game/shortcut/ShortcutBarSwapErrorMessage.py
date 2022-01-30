from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarSwapErrorMessage(NetworkMessage):
    protocolId = 3330
    error:int
    
