from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ShortcutBarRemoveRequestMessage(INetworkMessage):
    protocolId = 906
    barType:int
    slot:int
    
    
