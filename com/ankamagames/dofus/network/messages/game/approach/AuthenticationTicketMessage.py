from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AuthenticationTicketMessage(NetworkMessage):
    protocolId = 9517
    lang:str
    ticket:str
    
