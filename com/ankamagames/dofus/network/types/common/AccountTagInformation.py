from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AccountTagInformation(INetworkMessage):
    protocolId = 7636
    nickname:str
    tagNumber:str
    
    
