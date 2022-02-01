from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StartupActionFinishedMessage(NetworkMessage):
    actionId:int
    success:bool
    automaticAction:bool
    
    
