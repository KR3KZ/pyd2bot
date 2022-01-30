from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChangeThemeRequestMessage(INetworkMessage):
    protocolId = 8958
    theme:int
    
    
