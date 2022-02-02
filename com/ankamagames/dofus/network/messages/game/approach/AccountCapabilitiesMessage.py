from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AccountCapabilitiesMessage(NetworkMessage):
    accountId:int
    breedsVisible:int
    breedsAvailable:int
    status:int
    tutorialAvailable:bool
    canCreateNewCharacter:bool
    
    
    def __post_init__(self):
        super().__init__()
    