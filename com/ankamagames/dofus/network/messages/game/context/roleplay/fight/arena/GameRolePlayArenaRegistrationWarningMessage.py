from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayArenaRegistrationWarningMessage(INetworkMessage):
    protocolId = 1528
    battleMode:int
    
    
