from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayArenaRegisterMessage(INetworkMessage):
    protocolId = 5010
    battleMode:int
    
    
