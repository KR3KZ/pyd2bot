from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationStatusMessage(NetworkMessage):
    protocolId = 4323
    registered:bool
    step:int
    battleMode:int
    
    
