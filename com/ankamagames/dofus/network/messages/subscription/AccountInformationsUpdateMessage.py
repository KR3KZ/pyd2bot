from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AccountInformationsUpdateMessage(NetworkMessage):
    protocolId = 3664
    subscriptionEndDate:int
    
