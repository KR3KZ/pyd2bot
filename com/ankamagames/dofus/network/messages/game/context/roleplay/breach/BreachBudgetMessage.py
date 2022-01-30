from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachBudgetMessage(NetworkMessage):
    protocolId = 1903
    bugdet:int
    
    
