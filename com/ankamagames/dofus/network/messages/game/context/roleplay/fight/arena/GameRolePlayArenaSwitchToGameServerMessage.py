from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToGameServerMessage(NetworkMessage):
    protocolId = 651
    validToken:bool
    ticket:int
    homeServerId:int
    
    
