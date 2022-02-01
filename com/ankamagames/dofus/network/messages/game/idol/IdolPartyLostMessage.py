from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class IdolPartyLostMessage(INetworkMessage):
    protocolId = 7502
    idolId:int
    
    
