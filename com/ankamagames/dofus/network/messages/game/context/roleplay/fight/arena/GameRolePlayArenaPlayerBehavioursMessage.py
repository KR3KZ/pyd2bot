from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaPlayerBehavioursMessage(NetworkMessage):
    protocolId = 92
    flags:list[str]
    sanctions:list[str]
    banDuration:int
    
