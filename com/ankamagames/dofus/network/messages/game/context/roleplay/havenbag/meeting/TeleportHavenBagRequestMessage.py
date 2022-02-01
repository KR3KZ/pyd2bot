from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TeleportHavenBagRequestMessage(INetworkMessage):
    protocolId = 5838
    guestId:int
    
    
