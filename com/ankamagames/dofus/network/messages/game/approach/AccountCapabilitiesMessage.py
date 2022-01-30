from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AccountCapabilitiesMessage(NetworkMessage):
    protocolId = 8644
    accountId:int
    breedsVisible:int
    breedsAvailable:int
    status:int
    
