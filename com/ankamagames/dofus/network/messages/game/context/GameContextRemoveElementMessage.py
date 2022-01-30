from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameContextRemoveElementMessage(INetworkMessage):
    protocolId = 5284
    id:int
    
    
