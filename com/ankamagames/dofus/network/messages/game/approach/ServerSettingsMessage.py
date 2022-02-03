from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerSettingsMessage(NetworkMessage):
    lang:str
    community:int
    gameType:int
    arenaLeaveBanTime:int
    itemMaxLevel:int
    isMonoAccount:bool
    hasFreeAutopilot:bool
    

    def init(self, lang:str, community:int, gameType:int, arenaLeaveBanTime:int, itemMaxLevel:int):
        self.lang = lang
        self.community = community
        self.gameType = gameType
        self.arenaLeaveBanTime = arenaLeaveBanTime
        self.itemMaxLevel = itemMaxLevel
        
        super().__init__()
    
    