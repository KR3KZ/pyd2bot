from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PurchasableDialogMessage(NetworkMessage):
    purchasableId:int
    purchasableInstanceId:int
    price:int
    buyOrSell:bool
    secondHand:bool
    
    
    def __post_init__(self):
        super().__init__()
    