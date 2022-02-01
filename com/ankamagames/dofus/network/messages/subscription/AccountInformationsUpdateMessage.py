from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AccountInformationsUpdateMessage(INetworkMessage):
    protocolId = 3664
    subscriptionEndDate:int
    
    
