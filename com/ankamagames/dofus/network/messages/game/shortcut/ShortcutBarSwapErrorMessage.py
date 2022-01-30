from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ShortcutBarSwapErrorMessage(INetworkMessage):
    protocolId = 3330
    error:int
    
    
