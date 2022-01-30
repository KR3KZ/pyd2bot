from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TitleGainedMessage(INetworkMessage):
    protocolId = 3386
    titleId:int
    
    
