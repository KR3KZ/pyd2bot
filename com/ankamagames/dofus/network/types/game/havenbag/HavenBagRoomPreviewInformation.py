from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HavenBagRoomPreviewInformation(INetworkMessage):
    protocolId = 8913
    roomId:int
    themeId:int
    
    
