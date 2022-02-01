from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AlmanachCalendarDateMessage(INetworkMessage):
    protocolId = 2577
    date:int
    
    
