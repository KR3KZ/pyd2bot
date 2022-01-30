from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class KickHavenBagRequestMessage(INetworkMessage):
    protocolId = 188
    guestId:int
    
    
