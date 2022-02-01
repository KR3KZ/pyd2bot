from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildGetInformationsMessage(INetworkMessage):
    protocolId = 5805
    infoType:int
    
    
