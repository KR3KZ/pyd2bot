from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerSettingsMessage(NetworkMessage):
    lang:str
    community:int
    gameType:int
    arenaLeaveBanTime:int
    itemMaxLevel:int
    isMonoAccount:bool
    hasFreeAutopilot:bool
    
    
