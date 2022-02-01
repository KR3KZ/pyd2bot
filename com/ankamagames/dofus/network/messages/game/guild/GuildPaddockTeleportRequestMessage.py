from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildPaddockTeleportRequestMessage(INetworkMessage):
    protocolId = 7914
    paddockId:int
    
    
