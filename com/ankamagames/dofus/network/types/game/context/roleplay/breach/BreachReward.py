from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachReward(NetworkMessage):
    id:int
    buyLocks:list[int]
    buyCriterion:str
    remainingQty:int
    price:int
    
    
