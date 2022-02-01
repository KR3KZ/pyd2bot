from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AbstractPartyMessage(INetworkMessage):
    protocolId = 3299
    partyId:int
    
    
