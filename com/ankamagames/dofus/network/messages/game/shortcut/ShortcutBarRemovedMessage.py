from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ShortcutBarRemovedMessage(INetworkMessage):
    protocolId = 5087
    barType:int
    slot:int
    
    
