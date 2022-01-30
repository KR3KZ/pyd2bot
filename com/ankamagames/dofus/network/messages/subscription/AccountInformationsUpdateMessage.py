from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AccountInformationsUpdateMessage(INetworkMessage):
    protocolId = 3664
    subscriptionEndDate:int
    
    
