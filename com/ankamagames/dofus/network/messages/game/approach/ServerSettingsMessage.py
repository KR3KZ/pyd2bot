from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ServerSettingsMessage(NetworkMessage):
    protocolId = 298
    lang:str
    community:int
    gameType:int
    arenaLeaveBanTime:int
    itemMaxLevel:int
    
