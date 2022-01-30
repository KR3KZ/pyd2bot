from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AlmanachCalendarDateMessage(INetworkMessage):
    protocolId = 2577
    date:int
    
    
