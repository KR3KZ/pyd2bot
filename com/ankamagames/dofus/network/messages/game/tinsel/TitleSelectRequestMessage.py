from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TitleSelectRequestMessage(INetworkMessage):
    protocolId = 8025
    titleId:int
    
    
