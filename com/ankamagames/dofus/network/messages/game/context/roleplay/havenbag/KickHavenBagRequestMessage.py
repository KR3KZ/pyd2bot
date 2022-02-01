from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class KickHavenBagRequestMessage(INetworkMessage):
    protocolId = 188
    guestId:int
    
    
