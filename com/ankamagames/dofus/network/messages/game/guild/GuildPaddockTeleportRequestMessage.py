from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildPaddockTeleportRequestMessage(INetworkMessage):
    protocolId = 7914
    paddockId:int
    
    
