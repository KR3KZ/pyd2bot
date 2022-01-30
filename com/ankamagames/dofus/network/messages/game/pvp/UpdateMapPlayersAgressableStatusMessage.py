from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class UpdateMapPlayersAgressableStatusMessage(NetworkMessage):
    protocolId = 3658
    playerIds:list[float]
    enable:list[int]
    
