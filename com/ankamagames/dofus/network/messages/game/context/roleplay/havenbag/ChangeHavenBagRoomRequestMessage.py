from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChangeHavenBagRoomRequestMessage(INetworkMessage):
    protocolId = 7038
    roomId:int
    
    
