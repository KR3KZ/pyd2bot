from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HavenBagRoomPreviewInformation(INetworkMessage):
    protocolId = 8913
    roomId:int
    themeId:int
    
    
