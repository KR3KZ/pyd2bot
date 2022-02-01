from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ShortcutBarRemoveErrorMessage(INetworkMessage):
    protocolId = 5661
    error:int
    
    
