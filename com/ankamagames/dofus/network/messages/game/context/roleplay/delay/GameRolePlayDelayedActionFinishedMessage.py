from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayDelayedActionFinishedMessage(INetworkMessage):
    protocolId = 6062
    delayedCharacterId:int
    delayTypeId:int
    
    
