from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AlmanachCalendarDateMessage(NetworkMessage):
    protocolId = 2577
    date:int
    
