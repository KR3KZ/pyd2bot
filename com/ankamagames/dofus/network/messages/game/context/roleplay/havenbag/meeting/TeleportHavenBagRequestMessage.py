from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportHavenBagRequestMessage(INetworkMessage):
    protocolId = 5838
    guestId:int
    
    
