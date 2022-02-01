from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AuthenticationTicketMessage(INetworkMessage):
    protocolId = 9517
    lang:str
    ticket:str
    
    
