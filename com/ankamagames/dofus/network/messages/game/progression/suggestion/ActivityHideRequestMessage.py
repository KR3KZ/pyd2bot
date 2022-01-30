from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ActivityHideRequestMessage(NetworkMessage):
    protocolId = 9127
    activityId:int
    
