from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerLifeStatusMessage(NetworkMessage):
    protocolId = 7689
    state:int
    phenixMapId:int
    
