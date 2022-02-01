from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ShortcutBarAddErrorMessage(INetworkMessage):
    protocolId = 1782
    error:int
    
    
