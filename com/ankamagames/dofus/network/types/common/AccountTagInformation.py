from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AccountTagInformation(INetworkMessage):
    protocolId = 7636
    nickname:str
    tagNumber:str
    
    
