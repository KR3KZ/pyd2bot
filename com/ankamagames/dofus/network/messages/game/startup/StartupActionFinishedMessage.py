from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class StartupActionFinishedMessage(INetworkMessage):
    protocolId = 6394
    actionId:int
    success:bool
    automaticAction:bool
    
    
