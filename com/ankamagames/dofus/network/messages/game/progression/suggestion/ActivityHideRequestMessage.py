from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ActivityHideRequestMessage(INetworkMessage):
    protocolId = 9127
    activityId:int
    
    
