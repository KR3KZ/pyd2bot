from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachReward(NetworkMessage):
    protocolId = 2317
    id:int
    buyLocks:int
    buyCriterion:str
    remainingQty:int
    price:int
    
    
