from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SelectedServerRefusedMessage(NetworkMessage):
    serverId:int
    error:int
    serverStatus:int
    
    
