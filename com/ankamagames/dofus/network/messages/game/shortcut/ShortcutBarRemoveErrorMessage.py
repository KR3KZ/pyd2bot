from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ShortcutBarRemoveErrorMessage(INetworkMessage):
    protocolId = 5661
    error:int
    
    
