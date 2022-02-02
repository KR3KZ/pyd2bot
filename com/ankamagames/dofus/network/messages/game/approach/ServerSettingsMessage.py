from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ServerSettingsMessage(NetworkMessage):
    lang:str
    community:int
    gameType:int
    arenaLeaveBanTime:int
    itemMaxLevel:int
    isMonoAccount:bool
    hasFreeAutopilot:bool
    
    
    def __post_init__(self):
        super().__init__()
    