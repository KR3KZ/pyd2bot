from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionAcknowledgementMessage(NetworkMessage):
    valid:bool
    actionId:int
    
    
