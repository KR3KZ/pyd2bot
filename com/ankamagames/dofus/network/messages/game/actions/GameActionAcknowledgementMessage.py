from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameActionAcknowledgementMessage(INetworkMessage):
    protocolId = 3561
    valid:bool
    actionId:int
    
    
