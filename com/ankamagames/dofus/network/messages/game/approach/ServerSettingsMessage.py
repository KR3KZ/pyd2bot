from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ServerSettingsMessage(INetworkMessage):
    protocolId = 298
    lang:str
    community:int
    gameType:int
    arenaLeaveBanTime:int
    itemMaxLevel:int
    isMonoAccount:bool
    hasFreeAutopilot:bool
    
    
