from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachReward(NetworkMessage):
    id:int
    buyLocks:list[int]
    buyCriterion:str
    remainingQty:int
    price:int
    

    def init(self, id:int, buyLocks:list[int], buyCriterion:str, remainingQty:int, price:int):
        self.id = id
        self.buyLocks = buyLocks
        self.buyCriterion = buyCriterion
        self.remainingQty = remainingQty
        self.price = price
        
        super().__init__()
    
    