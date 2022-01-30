from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class Shortcut(INetworkMessage):
    protocolId = 5511
    slot:int
    
    
