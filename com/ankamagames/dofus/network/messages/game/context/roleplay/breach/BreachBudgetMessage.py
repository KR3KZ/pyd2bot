from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachBudgetMessage(INetworkMessage):
    protocolId = 1903
    bugdet:int
    
    
