from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class BreachReward(NetworkMessage):
    id:int
    buyLocks:list[int]
    buyCriterion:str
    remainingQty:int
    price:int
    
    
    def __post_init__(self):
        super().__init__()
    