from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BreachBudgetMessage(INetworkMessage):
    protocolId = 1903
    bugdet:int
    
    
