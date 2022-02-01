from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ChangeHavenBagRoomRequestMessage(INetworkMessage):
    protocolId = 7038
    roomId:int
    
    
