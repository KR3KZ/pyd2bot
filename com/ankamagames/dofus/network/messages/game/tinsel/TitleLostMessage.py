from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TitleLostMessage(INetworkMessage):
    protocolId = 1427
    titleId:int
    
    
