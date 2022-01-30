from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class UpdateMapPlayersAgressableStatusMessage(INetworkMessage):
    protocolId = 3658
    playerIds:int
    enable:int
    
    
