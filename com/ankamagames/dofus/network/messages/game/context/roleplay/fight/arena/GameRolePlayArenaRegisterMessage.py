from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegisterMessage(NetworkMessage):
    protocolId = 5010
    battleMode:int
    
