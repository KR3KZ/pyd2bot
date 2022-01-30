from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayArenaPlayerBehavioursMessage(INetworkMessage):
    protocolId = 92
    flags:str
    sanctions:str
    banDuration:int
    
    
