from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HavenBagRoomPreviewInformation(NetworkMessage):
    protocolId = 8913
    roomId:int
    themeId:int
    
    
