from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayArenaRegistrationStatusMessage(INetworkMessage):
    protocolId = 4323
    registered:bool
    step:int
    battleMode:int
    
    