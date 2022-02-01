from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ActivityHideRequestMessage(INetworkMessage):
    protocolId = 9127
    activityId:int
    
    
