from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DebugInClientMessage(INetworkMessage):
    protocolId = 6517
    level:int
    message:str
    
    
