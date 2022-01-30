from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AuthenticationTicketMessage(INetworkMessage):
    protocolId = 9517
    lang:str
    ticket:str
    
    
