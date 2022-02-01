from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class DebtsDeleteMessage(INetworkMessage):
    protocolId = 5619
    reason:int
    debts:int
    
    
