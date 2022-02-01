from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AccountLoggingKickedMessage(INetworkMessage):
    protocolId = 7661
    days:int
    hours:int
    minutes:int
    
    
