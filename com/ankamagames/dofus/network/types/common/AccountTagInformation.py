from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AccountTagInformation(NetworkMessage):
    protocolId = 7636
    nickname:str
    tagNumber:str
    
    
