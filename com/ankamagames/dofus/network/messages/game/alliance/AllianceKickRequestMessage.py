from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceKickRequestMessage(INetworkMessage):
    protocolId = 1648
    kickedId:int
    
    
