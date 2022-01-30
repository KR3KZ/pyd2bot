from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ShortcutBarAddErrorMessage(INetworkMessage):
    protocolId = 1782
    error:int
    
    
