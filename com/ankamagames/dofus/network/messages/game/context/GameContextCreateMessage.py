from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameContextCreateMessage(INetworkMessage):
    protocolId = 4950
    context:int
    
    
