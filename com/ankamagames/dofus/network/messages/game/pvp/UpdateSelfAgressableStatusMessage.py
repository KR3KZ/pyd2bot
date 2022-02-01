from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateSelfAgressableStatusMessage(NetworkMessage):
    status:int
    probationTime:int
    
    
