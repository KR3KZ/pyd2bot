from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachSavedMessage(INetworkMessage):
    protocolId = 4537
    saved:bool
    
    
