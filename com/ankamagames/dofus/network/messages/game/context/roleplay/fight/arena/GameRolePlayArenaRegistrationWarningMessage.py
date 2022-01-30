from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationWarningMessage(NetworkMessage):
    protocolId = 1528
    battleMode:int
    
    
