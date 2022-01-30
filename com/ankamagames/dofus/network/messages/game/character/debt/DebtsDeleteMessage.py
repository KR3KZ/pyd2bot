from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class DebtsDeleteMessage(INetworkMessage):
    protocolId = 5619
    reason:int
    debts:int
    
    
