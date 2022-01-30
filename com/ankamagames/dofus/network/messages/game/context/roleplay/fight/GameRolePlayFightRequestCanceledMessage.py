from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayFightRequestCanceledMessage(INetworkMessage):
    protocolId = 4478
    fightId:int
    sourceId:int
    targetId:int
    
    
