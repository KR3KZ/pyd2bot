from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BreachReward(INetworkMessage):
    protocolId = 2317
    id:int
    buyLocks:int
    buyCriterion:str
    remainingQty:int
    price:int
    
    
