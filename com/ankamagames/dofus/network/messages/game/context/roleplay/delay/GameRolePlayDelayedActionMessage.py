from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionMessage(NetworkMessage):
    protocolId = 1161
    delayedCharacterId:int
    delayTypeId:int
    delayEndTime:int
    
