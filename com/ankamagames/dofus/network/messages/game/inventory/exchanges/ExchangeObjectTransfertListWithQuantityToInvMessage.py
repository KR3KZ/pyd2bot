from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ExchangeObjectTransfertListWithQuantityToInvMessage(NetworkMessage):
    ids:list[int]
    qtys:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    