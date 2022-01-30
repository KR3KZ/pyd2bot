from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayPlayerLifeStatusMessage(INetworkMessage):
    protocolId = 7689
    state:int
    phenixMapId:int
    
    
