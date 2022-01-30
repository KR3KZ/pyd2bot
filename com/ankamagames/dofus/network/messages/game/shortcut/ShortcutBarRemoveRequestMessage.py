from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ShortcutBarRemoveRequestMessage(INetworkMessage):
    protocolId = 906
    barType:int
    slot:int
    
    
