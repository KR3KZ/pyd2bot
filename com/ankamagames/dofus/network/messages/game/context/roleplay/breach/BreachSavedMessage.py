from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachSavedMessage(INetworkMessage):
    protocolId = 4537
    saved:bool
    
    
