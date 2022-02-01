from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChangeThemeRequestMessage(INetworkMessage):
    protocolId = 8958
    theme:int
    
    
