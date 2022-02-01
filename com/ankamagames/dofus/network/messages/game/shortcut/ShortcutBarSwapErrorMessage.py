from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ShortcutBarSwapErrorMessage(INetworkMessage):
    protocolId = 3330
    error:int
    
    
