from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ChangeThemeRequestMessage(NetworkMessage):
    protocolId = 8958
    theme:int
    
    
