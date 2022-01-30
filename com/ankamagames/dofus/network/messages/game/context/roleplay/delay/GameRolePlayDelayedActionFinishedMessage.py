from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionFinishedMessage(NetworkMessage):
    protocolId = 6062
    delayedCharacterId:int
    delayTypeId:int
    
